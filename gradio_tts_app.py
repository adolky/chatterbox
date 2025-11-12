import random
import numpy as np
import torch
import gradio as gr
from chatterbox.tts import ChatterboxTTS
from chatterbox.mtl_tts import ChatterboxMultilingualTTS, SUPPORTED_LANGUAGES
import os
from datetime import datetime
import shutil
import re
import gc
import warnings
import logging
import time
import sys

# Configuration du logging production
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Créer un nom de fichier de log avec timestamp
log_timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
log_file = os.path.join(LOG_DIR, f"gradio_app_{log_timestamp}.log")

# Configuration du logger
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
    handlers=[
        logging.FileHandler(log_file, encoding='utf-8'),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)
logger.info("="*60)
logger.info("CHATTERBOX TTS - MODE PRODUCTION")
logger.info(f"Fichier de log: {log_file}")
logger.info("="*60)

# Désactiver les warnings pour les autres bibliothèques
warnings.filterwarnings('ignore')
logging.getLogger('chatterbox').setLevel(logging.WARNING)
logging.getLogger('transformers').setLevel(logging.WARNING)
logging.getLogger('gradio').setLevel(logging.INFO)


DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
SAVED_VOICES_DIR = "voix_sauvegardees"

os.makedirs(SAVED_VOICES_DIR, exist_ok=True)


def set_seed(seed: int):
    torch.manual_seed(seed)
    torch.cuda.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    random.seed(seed)
    np.random.seed(seed)


def load_model():
    logger.info("Chargement du modèle multilingue...")
    try:
        model = ChatterboxMultilingualTTS.from_pretrained(DEVICE)
        logger.info(f"Modèle chargé avec succès sur {DEVICE}")
        return model
    except Exception as e:
        logger.error(f"Erreur lors du chargement du modèle: {e}", exc_info=True)
        raise


def load_text_file(file):
    if file is None:
        return "", "ℹ️ Aucun texte"
    try:
        with open(file.name, 'r', encoding='utf-8') as f:
            content = f.read()
        return content, estimate_duration(content)
    except Exception as e:
        return f"Error loading file: {str(e)}", "⚠️ Erreur"


def estimate_duration(text):
    if not text or text.strip() == "":
        return "ℹ️ Aucun texte"
    words = len(text.split())
    minutes = words / 150
    hours = minutes / 60
    if hours >= 1:
        return f"📊 **Estimation** : ~{hours:.1f}h ({words:,} mots, {len(text):,} caractères)"
    elif minutes >= 1:
        return f"📊 **Estimation** : ~{minutes:.0f} min ({words:,} mots, {len(text):,} caractères)"
    else:
        return f"📊 **Estimation** : ~{minutes*60:.0f}s ({words:,} mots, {len(text):,} caractères)"


def get_saved_voices():
    voices = []
    if os.path.exists(SAVED_VOICES_DIR):
        for file in os.listdir(SAVED_VOICES_DIR):
            if file.endswith(('.wav', '.mp3', '.flac')):
                voices.append(file)
    return voices


def save_voice(audio_file, voice_name):
    if audio_file is None:
        return "❌ Aucun fichier audio à sauvegarder", gr.update(choices=get_saved_voices())
    if not voice_name or voice_name.strip() == "":
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        voice_name = f"voix_{timestamp}"
    voice_name = voice_name.strip()
    ext = os.path.splitext(audio_file)[1]
    if not ext:
        ext = ".wav"
    filename = f"{voice_name}{ext}"
    save_path = os.path.join(SAVED_VOICES_DIR, filename)
    shutil.copy2(audio_file, save_path)
    return f"✅ Voix sauvegardée : {filename}", gr.update(choices=get_saved_voices(), value=filename)


def load_saved_voice(voice_filename):
    if not voice_filename:
        return None
    voice_path = os.path.join(SAVED_VOICES_DIR, voice_filename)
    if os.path.exists(voice_path):
        return voice_path
    return None


def generate(model, text, language, audio_prompt_path, exaggeration, temperature, seed_num, cfgw, min_p, top_p, repetition_penalty, batch_size, max_tokens, progress=gr.Progress()):
    logger.info(f"Nouvelle génération - Langue: {language}, Longueur texte: {len(text)} caractères")
    
    if model is None:
        logger.info("Modèle non chargé, chargement en cours...")
        model = ChatterboxMultilingualTTS.from_pretrained(DEVICE)
    if seed_num != 0:
        set_seed(int(seed_num))
    if not text or text.strip() == "":
        logger.warning("Tentative de génération avec texte vide")
        raise gr.Error("⚠️ Veuillez entrer du texte ou charger un fichier !")
    
    # DÉSACTIVER la détection de répétition pour TOUTES les langues = qualité + vitesse
    # C'est la clé pour éviter la troncature prématurée du texte
    use_analyzer = False
    
    # Optimisations spécifiques par langue pour maximiser vitesse ET qualité
    # NOUVELLE RÈGLE: Max tokens ≤ 650 pour garantir texte complet
    
    if language == "en":
        # 🇬🇧 Anglais : mots courts, phonétique simple
        if max_tokens > 650:
            max_tokens = 650
            print(f"🇬🇧 Optimisation anglais - max_tokens ajusté à {max_tokens}")
        if batch_size < 400:
            batch_size = 400
            print(f"🇬🇧 Optimisation anglais - batch_size ajusté à {batch_size}")
            
    elif language == "fr":
        # 🇫🇷 Français : liaisons, phonétique complexe
        if max_tokens > 650:
            max_tokens = 650
            print(f"🇫🇷 Optimisation français - max_tokens ajusté à {max_tokens}")
        if batch_size > 300 or batch_size < 250:
            batch_size = 280
            print(f"🇫🇷 Optimisation français - batch_size ajusté à {batch_size}")
            
    elif language in ["es", "it", "pt"]:
        # 🇪🇸🇮🇹🇵🇹 Langues romanes
        if max_tokens > 650:
            max_tokens = 650
            print(f"🌍 Optimisation {language.upper()} - max_tokens ajusté à {max_tokens}")
        if batch_size < 350:
            batch_size = 350
            print(f"🌍 Optimisation {language.upper()} - batch_size ajusté à {batch_size}")
            
    elif language in ["de", "nl"]:
        # 🇩🇪🇳🇱 Allemand/Néerlandais : mots très longs
        if max_tokens > 650:
            max_tokens = 650
            print(f"🇩🇪 Optimisation {language.upper()} - max_tokens ajusté à {max_tokens}")
        if batch_size > 320:
            batch_size = 320
            print(f"🇩🇪 Optimisation {language.upper()} - batch_size ajusté à {batch_size}")
            
    elif language in ["ja", "zh", "ko"]:
        # 🇯🇵🇨🇳🇰🇷 Langues asiatiques : caractères complexes
        if max_tokens > 650:
            max_tokens = 650
            print(f"🌏 Optimisation {language.upper()} - max_tokens ajusté à {max_tokens}")
        if batch_size > 250:
            batch_size = 250
            print(f"🌏 Optimisation {language.upper()} - batch_size ajusté à {batch_size}")
            
    elif language in ["ar", "he"]:
        # 🇸🇦🇮🇱 Langues sémitiques : écriture RTL
        if max_tokens > 650:
            max_tokens = 650
            print(f"🕌 Optimisation {language.upper()} - max_tokens ajusté à {max_tokens}")
        if batch_size > 280:
            batch_size = 280
            print(f"🕌 Optimisation {language.upper()} - batch_size ajusté à {batch_size}")
            
    elif language in ["ru", "pl"]:
        # 🇷🇺🇵🇱 Langues slaves : phonétique complexe
        if max_tokens > 650:
            max_tokens = 650
            print(f"🇷🇺 Optimisation {language.upper()} - max_tokens ajusté à {max_tokens}")
        if batch_size > 300:
            batch_size = 300
            print(f"🇷🇺 Optimisation {language.upper()} - batch_size ajusté à {batch_size}")
            
    else:
        # 🌍 Autres langues : paramètres par défaut
        if max_tokens > 650:
            max_tokens = 650
            print(f"🌍 Optimisation {language.upper()} - max_tokens ajusté à {max_tokens}")
        if batch_size < 300:
            batch_size = 300
            print(f"🌍 Optimisation {language.upper()} - batch_size ajusté à {batch_size}")
    
    print(f"📝 Text: {len(text)} chars | Language: {language} | Batch: {batch_size} | Max tokens: {max_tokens} | Analyzer: DISABLED")
    
    # Split long text into sentences to avoid memory issues
    # 🎯 DÉCOUPAGE SIMPLE ET FIABLE PAR PHRASES COMPLÈTES
    # RÈGLE ABSOLUE: Ne JAMAIS couper avant un point (.)
    
    # Étape 1: Découper en phrases complètes
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    batches = []
    current_batch = []
    current_length = 0
    
    BATCH_LIMIT = int(batch_size)
    
    for sentence in sentences:
        sentence = sentence.strip()
        if not sentence:
            continue
        
        sentence_len = len(sentence)
        
        # Si ajouter cette phrase dépasse la limite ET on a déjà du contenu
        if current_length + sentence_len > BATCH_LIMIT and current_batch:
            # Sauvegarder le batch actuel (phrases complètes)
            batches.append(" ".join(current_batch))
            # Démarrer un nouveau batch avec cette phrase
            current_batch = [sentence]
            current_length = sentence_len
        else:
            # Ajouter la phrase au batch actuel
            current_batch.append(sentence)
            current_length += sentence_len
    
    # Ajouter le dernier batch
    if current_batch:
        batches.append(" ".join(current_batch))
    
    # 🕐 CALCUL DU TEMPS ESTIMÉ
    # Estimation basée sur le nombre de batches et la longueur totale
    total_chars = len(text)
    num_batches = len(batches)
    
    logger.info(f"Texte divisé en {num_batches} batches ({total_chars} caractères)")
    
    # Temps par batch: ~75-90 secondes en moyenne (varie selon GPU)
    estimated_time_per_batch = 80  # secondes
    total_estimated_seconds = num_batches * estimated_time_per_batch
    
    # Convertir en minutes
    estimated_minutes = total_estimated_seconds / 60
    
    print(f"\n⏱️  ESTIMATION DE TEMPS:")
    print(f"   📝 Texte: {total_chars} caractères")
    print(f"   📦 Batches: {num_batches}")
    print(f"   ⏰ Temps estimé: {estimated_minutes:.1f} minutes ({total_estimated_seconds//60:.0f}min {total_estimated_seconds%60:.0f}s)")
    print(f"   🚀 Démarrage de la génération...\n")
    
    # Initialiser la progression
    progress(0, desc=f"🎙️ Préparation... {num_batches} batches à générer")
    
    # Afficher les détails des batches
    print(f"📦 Processing {len(batches)} batches")
    print(f"📋 Batch details:")
    for idx, batch in enumerate(batches):
        words = len(batch.split())
        sentences_count = batch.count('.') + batch.count('!') + batch.count('?')
        print(f"\n   Batch {idx+1}: {len(batch)} chars, ~{words} words, {sentences_count} sentences")
        print(f"      Starts: {batch[:70]}...")
        print(f"      Ends:   ...{batch[-70:]}")
        # Vérifier que le batch se termine bien par . ! ou ?
        if batch and batch[-1] not in '.!?':
            print(f"      ⚠️ WARNING: Batch ne se termine PAS par un point!")
    
    print(f"\n")
    all_wavs = []
    
    # Utiliser ChatterboxMultilingualTTS pour TOUTES les langues (y compris anglais)
    # Paramètres unifiés pour cohérence et qualité
    print(f"Using ChatterboxMultilingualTTS ({language}) - Unified settings")
    
    # 🎯 Système de génération par groupe pour réduire le cleanup GPU
    # Cleanup seulement tous les 8 batches au lieu de 3
    BATCHES_PER_GROUP = 8  # Traiter 8 batches avant de cleanup (au lieu de 3)
    
    # Timer pour le temps réel
    import time
    start_time = time.time()
    
    for i, batch_text in enumerate(batches):
        # Mettre à jour la progression avec détails
        batch_progress = (i / len(batches))
        elapsed = time.time() - start_time
        elapsed_min = elapsed / 60
        
        # Calculer temps restant basé sur le progrès réel
        if i > 0:
            avg_time_per_batch = elapsed / i
            remaining_batches = len(batches) - i
            estimated_remaining = (avg_time_per_batch * remaining_batches) / 60
            progress_desc = (
                f"🎙️ Batch {i+1}/{len(batches)} | ⏱️ {elapsed_min:.1f}min écoulées | ~{estimated_remaining:.1f}min restantes\n"
                f"⏰ Temps estimé total: {estimated_minutes:.1f} minutes"
            )
            progress(batch_progress, desc=progress_desc)
        else:
            progress_desc = (
                f"🎙️ Batch {i+1}/{len(batches)} | Démarrage...\n"
                f"⏰ Temps estimé total: {estimated_minutes:.1f} minutes"
            )
            progress(batch_progress, desc=progress_desc)
        
        print(f"🔊 Batch {i+1}/{len(batches)}: {len(batch_text)} chars")
        print(f"   Preview: {batch_text[:80]}..." if len(batch_text) > 80 else f"   Text: {batch_text}")
        
        # Skip empty batches
        if not batch_text or not batch_text.strip():
            print(f"   ⚠️ Skipping empty batch")
            continue
        
        # 🎯 AJUSTEMENT DYNAMIQUE DES TOKENS basé sur la longueur
        # Formule: Plus le batch est long, plus on donne de tokens
        # Range: 500 (batch court) → 650 (batch long) - MAX 650
        
        batch_length_ratio = min(len(batch_text) / batch_size, 1.0)
        # Calculer tokens: 500 + (150 × ratio) = 500 à 650
        batch_max_tokens = int(500 + (150 * batch_length_ratio))
        
        # Garantir entre 500 et 650
        batch_max_tokens = max(500, min(650, batch_max_tokens))
        
        print(f"   🎯 Tokens dynamiques: {batch_max_tokens} (longueur: {len(batch_text)}/{batch_size} = {batch_length_ratio*100:.0f}%)")
        
        try:
            wav = model.generate(
                language_id=language,
                text=batch_text,
                audio_prompt_path=audio_prompt_path,
                exaggeration=exaggeration,
                temperature=temperature,
                cfg_weight=cfgw,
                min_p=min_p,
                top_p=top_p,
                repetition_penalty=repetition_penalty,
                max_new_tokens=int(batch_max_tokens),
                use_alignment_analyzer=use_analyzer,  # DISABLED pour toutes les langues
            )
            
            # Vérifier que l'audio a été généré
            if wav is None or wav.numel() == 0:
                print(f"   ❌ WARNING: Batch {i+1} generated empty audio!")
                continue
                
            audio_duration = wav.shape[-1] / model.sr
            print(f"   ✅ Generated {audio_duration:.2f}s of audio")
            all_wavs.append(wav.squeeze(0))
            
            # 🧹 Cleanup GPU RÉDUIT: Seulement tous les 8 batches
            # Gain de vitesse significatif en réduisant les cleanups
            if (i + 1) % BATCHES_PER_GROUP == 0:
                print(f"   🧹 GPU cleanup (every {BATCHES_PER_GROUP} batches)")
                if torch.cuda.is_available():
                    torch.cuda.empty_cache()
                gc.collect()
            
        except Exception as e:
            print(f"   ❌ ERROR generating batch {i+1}: {str(e)}")
            print(f"   Skipping this batch and continuing...")
            continue
    
    # 🧹 Cleanup final après tous les batches
    progress(0.99, desc="🧹 Nettoyage final de la mémoire GPU...")
    print(f"\n🧹 Final GPU cleanup")
    if torch.cuda.is_available():
        torch.cuda.empty_cache()
    gc.collect()
    
    # Calculer le temps total écoulé
    total_elapsed = time.time() - start_time
    total_elapsed_min = total_elapsed / 60
    
    # Vérifier qu'on a bien généré tous les batches
    if len(all_wavs) == 0:
        raise gr.Error("❌ Aucun audio généré ! Vérifiez les paramètres et les logs.")
    
    if len(all_wavs) < len(batches):
        print(f"⚠️ WARNING: Seulement {len(all_wavs)}/{len(batches)} batches générés avec succès")
        print(f"   → Certaines parties du texte peuvent manquer dans l'audio")
    
    progress(1.0, desc="✅ Assemblage final de l'audio...")
    combined_wav = torch.cat(all_wavs, dim=-1)
    sr = model.sr
    
    total_duration = combined_wav.shape[-1] / sr
    expected_duration = len(text) / 15  # Approximation: 15 caractères par seconde
    
    # Afficher le résumé final avec temps réel vs estimé
    print(f"\n{'='*60}")
    print(f"✅ GÉNÉRATION TERMINÉE !")
    print(f"{'='*60}")
    print(f"📊 Statistiques:")
    print(f"   ✅ Batches générés: {len(all_wavs)}/{len(batches)}")
    print(f"   🎵 Audio généré: {total_duration:.2f}s ({total_duration/60:.2f} min)")
    print(f"   ⏱️  Temps de génération: {total_elapsed_min:.2f} min")
    print(f"   ⚡ Vitesse: {total_duration/60 / total_elapsed_min:.2f}x temps réel")
    print(f"   📝 Texte: {len(text)} caractères")
    
    # Comparer estimation vs réalité
    accuracy = (total_elapsed_min / estimated_minutes) * 100
    print(f"\n🎯 Précision de l'estimation:")
    print(f"   Estimé: {estimated_minutes:.1f} min")
    print(f"   Réel: {total_elapsed_min:.1f} min")
    print(f"   Précision: {accuracy:.0f}%")
    
    # Logger les statistiques
    logger.info(f"Génération terminée - {len(all_wavs)} batches, {total_duration:.2f}s audio, {total_elapsed_min:.2f}min")
    print(f"{'='*60}\n")
    
    if total_duration < expected_duration * 0.7:
        print(f"⚠️ WARNING: L'audio semble trop court - vérifiez si du texte a été sauté")
    
    return (sr, combined_wav.numpy())


with gr.Blocks(title="Chatterbox TTS - Longue Durée Multilingue") as demo:
    model_state = gr.State(None)
    gr.Markdown("""
    # 🎙️ Chatterbox TTS - Générateur Audio Longue Durée Multilingue
    ### Générez des audios de 1-2h+ à partir de texte ou de fichiers dans 24 langues
    """)
    with gr.Row():
        with gr.Column():
            gr.Markdown("### 📝 Entrée de Texte")
            text_file = gr.File(
                label="📁 Option 1 : Charger un fichier texte (.txt, .md, etc.)",
                file_types=[".txt", ".md", ".text"],
                type="filepath"
            )
            text = gr.Textbox(
                value="Now let's make my mum's favourite. So three mars bars into the pan. Then we add the tuna and just stir for a bit, just let the chocolate and fish infuse. A sprinkle of olive oil and some tomato ketchup. Now smell that. Oh boy this is going to be incredible.",
                label="✍️ Option 2 : Saisir ou coller le texte directement",
                max_lines=50,
                lines=15,
                placeholder="Entrez votre texte ici (capacité illimitée - parfait pour 1-2h d'audio)..."
            )
            language = gr.Dropdown(
                choices=[(f"{name} ({code})", code) for code, name in sorted(SUPPORTED_LANGUAGES.items(), key=lambda x: x[1])],
                value="en",
                label="🌍 Langue du texte",
                info="Sélectionnez la langue du texte à synthétiser"
            )
            duration_info = gr.Markdown("📊 **Estimation** : ~1 min (57 mots)")
            gr.Markdown("""
            💡 **Conseils pour les longs textes** :
            - Divisez en paragraphes naturels pour de meilleurs résultats
            - ~18,000 mots = ~2h d'audio
            - ~9,000 mots = ~1h d'audio
            """)
            gr.Markdown("### 🎵 Paramètres Audio")
            with gr.Row():
                with gr.Column():
                    ref_wav = gr.Audio(
                        sources=["upload", "microphone"], 
                        type="filepath", 
                        label="🎤 Fichier Audio de Référence (optionnel)", 
                        value=None
                    )
                with gr.Column():
                    saved_voices = gr.Dropdown(
                        choices=get_saved_voices(),
                        value=None,
                        label="💾 Charger une voix sauvegardée",
                        info="Sélectionnez une voix précédemment sauvegardée",
                        interactive=True
                    )
            with gr.Row():
                voice_name = gr.Textbox(
                    label="📝 Nom de la voix (optionnel)",
                    placeholder="Ex: voix_homme_1, voix_femme_claire, etc.",
                    scale=3
                )
                save_btn = gr.Button("💾 Sauvegarder cette voix", scale=1, size="sm")
            save_status = gr.Markdown("")
            exaggeration = gr.Slider(0.25, 2, step=.05, label="Exagération (Neutre = 0.5)", value=.5)
            cfg_weight = gr.Slider(0.0, 1, step=.05, label="CFG/Rythme", value=0.5)
            with gr.Accordion("⚙️ Options Avancées", open=False):
                max_tokens = gr.Slider(
                    100, 1500, step=50, 
                    label="🚀 Max Tokens", 
                    value=650,
                    info="Auto-ajusté: 500-650 selon longueur batch | MAX 650 toutes langues | Cleanup GPU: 8 batches"
                )
                batch_size = gr.Slider(
                    200, 800, step=50, 
                    label="⚡ Taille des lots (caractères)", 
                    value=400,
                    info="Auto-optimisé par langue : 🇬🇧 EN=400 | 🇫🇷 FR=280 | 🇪🇸 ES/IT/PT=350 | Plus grand = plus rapide"
                )
                seed_num = gr.Number(value=0, label="Graine aléatoire (0 = aléatoire)")
                temp = gr.Slider(0.05, 5, step=.05, label="Température", value=.8)
                min_p = gr.Slider(0.00, 1.00, step=0.01, label="min_p (Recommandé 0.02-0.1, 0 = désactivé)", value=0.05)
                top_p = gr.Slider(0.00, 1.00, step=0.01, label="top_p (1.0 = désactivé recommandé)", value=1.00)
                repetition_penalty = gr.Slider(1.00, 2.00, step=0.01, label="Pénalité de répétition", value=1.15, info="1.15 recommandé pour vitesse, 1.00 = désactivé")
            run_btn = gr.Button("🎬 Générer l'Audio", variant="primary", size="lg")
        with gr.Column():
            gr.Markdown("### 🔊 Sortie Audio")
            audio_output = gr.Audio(label="Audio Généré")
            gr.Markdown("""
            ℹ️ **Informations** :
            - La génération peut prendre du temps pour de longs textes
            - Pour les textes de 1-2h, cela peut prendre plusieurs minutes
            - L'audio sera téléchargeable une fois la génération terminée
            
            🌍 **Langues supportées** : Arabe, Chinois, Danois, Néerlandais, Anglais, Finnois, 
            Français, Allemand, Grec, Hébreu, Hindi, Italien, Japonais, Coréen, Malais, 
            Norvégien, Polonais, Portugais, Russe, Espagnol, Swahili, Suédois, Turc
            """)
    demo.load(fn=load_model, inputs=[], outputs=model_state)
    text_file.change(fn=load_text_file, inputs=[text_file], outputs=[text, duration_info])
    text.change(fn=estimate_duration, inputs=[text], outputs=duration_info)
    save_btn.click(fn=save_voice, inputs=[ref_wav, voice_name], outputs=[save_status, saved_voices])
    saved_voices.change(fn=load_saved_voice, inputs=[saved_voices], outputs=ref_wav)
    run_btn.click(
        fn=generate,
        inputs=[model_state, text, language, ref_wav, exaggeration, temp, seed_num, cfg_weight, min_p, top_p, repetition_penalty, batch_size, max_tokens],
        outputs=audio_output,
    )

if __name__ == "__main__":
    try:
        # Obtenir l'adresse IP locale
        import socket
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)
        
        logger.info("="*60)
        logger.info("Démarrage de l'interface Gradio...")
        logger.info(f"Device: {DEVICE}")
        logger.info(f"Hostname: {hostname}")
        logger.info("="*60)
        logger.info("📡 ACCÈS À L'APPLICATION:")
        logger.info(f"   🏠 Localhost: http://localhost:7860")
        logger.info(f"   🌐 Réseau local: http://{local_ip}:7860")
        logger.info(f"   💻 Depuis autre PC: http://{local_ip}:7860")
        logger.info("="*60)
        
        print("\n" + "="*60)
        print("🚀 CHATTERBOX TTS - MODE PRODUCTION")
        print("="*60)
        print(f"📡 Accès local: http://localhost:7860")
        print(f"🌐 Accès réseau: http://{local_ip}:7860")
        print(f"💻 Depuis autre PC: http://{local_ip}:7860")
        print("="*60 + "\n")
        
        demo.queue(max_size=50, default_concurrency_limit=1).launch(
            share=True, 
            server_name="0.0.0.0", 
            server_port=7860, 
            inbrowser=True
        )
    except KeyboardInterrupt:
        logger.info("Arrêt demandé par l'utilisateur (Ctrl+C)")
        sys.exit(0)
    except Exception as e:
        logger.error(f"Erreur fatale: {e}", exc_info=True)
        sys.exit(1)

