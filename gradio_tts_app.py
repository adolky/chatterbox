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

# Désactiver les warnings pour une génération plus propre
warnings.filterwarnings('ignore')
logging.getLogger('chatterbox').setLevel(logging.ERROR)
logging.getLogger('transformers').setLevel(logging.ERROR)


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
    model = ChatterboxMultilingualTTS.from_pretrained(DEVICE)
    return model


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


def generate(model, text, language, audio_prompt_path, exaggeration, temperature, seed_num, cfgw, min_p, top_p, repetition_penalty, batch_size, max_tokens):
    if model is None:
        model = ChatterboxMultilingualTTS.from_pretrained(DEVICE)
    if seed_num != 0:
        set_seed(int(seed_num))
    if not text or text.strip() == "":
        raise gr.Error("⚠️ Veuillez entrer du texte ou charger un fichier !")
    
    # Optimisation spéciale pour le français : désactiver la détection de répétition
    use_analyzer = False if language == "fr" else None  # False pour français, None pour autres
    
    # Ajustement automatique de max_tokens selon la langue
    # Pour le français en mode optimisé, on utilise des valeurs plus basses
    if language == "fr":
        # Français optimisé : max_tokens plus bas car pas de détection de répétition
        if max_tokens > 400:
            adjusted_max_tokens = min(int(max_tokens * 0.7), 350)  # Réduire pour vitesse
            print(f"⚡ Français mode RAPIDE - réduction max_tokens: {max_tokens} → {adjusted_max_tokens}")
            max_tokens = adjusted_max_tokens
    elif language in ["de", "pl", "ru", "fi", "el"] and max_tokens < 600:
        adjusted_max_tokens = int(max_tokens * 1.5)  # +50% pour ces langues
        print(f"⚠️ Langue {language} détectée - augmentation max_tokens: {max_tokens} → {adjusted_max_tokens}")
        max_tokens = adjusted_max_tokens
    
    print(f"📝 Text: {len(text)} chars | Language: {language} | Batch: {batch_size} | Max tokens: {max_tokens} | Analyzer: {use_analyzer}")
    
    # Split long text into sentences to avoid memory issues
    sentences = re.split(r'(?<=[.!?])\s+', text)
    
    # For very long texts, process in smaller batches
    MAX_CHARS_PER_BATCH = int(batch_size)
    batches = []
    current_batch = []
    current_length = 0
    
    for sentence in sentences:
        if not sentence.strip():
            continue
        sentence_len = len(sentence)
        if current_length + sentence_len > MAX_CHARS_PER_BATCH and current_batch:
            batches.append(" ".join(current_batch))
            current_batch = [sentence]
            current_length = sentence_len
        else:
            current_batch.append(sentence)
            current_length += sentence_len
    
    if current_batch:
        batches.append(" ".join(current_batch))
    
    print(f"📦 Processing {len(batches)} batches")
    
    all_wavs = []
    
    # Use ChatterboxTTS for English, ChatterboxMultilingualTTS for other languages
    if language == "en":
        print("Using ChatterboxTTS (English)")
        tts_model = ChatterboxTTS.from_pretrained(DEVICE)
        
        for i, batch_text in enumerate(batches):
            print(f"🔊 Batch {i+1}/{len(batches)}: {len(batch_text)} chars")
            
            wav = tts_model.generate(
                text=batch_text,
                audio_prompt_path=audio_prompt_path,
                exaggeration=exaggeration,
                temperature=temperature,
                cfg_weight=cfgw,
                min_p=min_p,
                top_p=top_p,
                repetition_penalty=repetition_penalty,
                max_new_tokens=int(max_tokens),
            )
            all_wavs.append(wav.squeeze(0))
            
            # Nettoyage mémoire seulement tous les 3 lots pour gagner du temps
            if (i + 1) % 3 == 0:
                if torch.cuda.is_available():
                    torch.cuda.empty_cache()
                gc.collect()
        
        del tts_model
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        gc.collect()
        
        combined_wav = torch.cat(all_wavs, dim=-1)
        sr = 24000
        
    else:
        print(f"Using ChatterboxMultilingualTTS ({language})")
        
        for i, batch_text in enumerate(batches):
            print(f"🔊 Batch {i+1}/{len(batches)}: {len(batch_text)} chars")
            
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
                max_new_tokens=int(max_tokens),
                use_alignment_analyzer=use_analyzer,  # False pour français = RAPIDE!
            )
            all_wavs.append(wav.squeeze(0))
            
            # Nettoyage mémoire seulement tous les 3 lots pour gagner du temps
            if (i + 1) % 3 == 0:
                if torch.cuda.is_available():
                    torch.cuda.empty_cache()
                gc.collect()
        
        combined_wav = torch.cat(all_wavs, dim=-1)
        sr = model.sr
    
    print(f"✅ Generated {len(batches)} batches, total: {combined_wav.shape[-1] / sr:.2f}s")
    
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
                    100, 1000, step=50, 
                    label="🚀 Max Tokens", 
                    value=350,
                    info="🇫🇷 Français: 300-350 (RAPIDE!) | 🇬🇧 Anglais: 400-500 | Autres: 600-800"
                )
                batch_size = gr.Slider(
                    200, 800, step=50, 
                    label="⚡ Taille des lots (caractères)", 
                    value=300,
                    info="🇫🇷 Français: 250-300 | 🇬🇧 Anglais: 350-400 | Optimal pour vitesse"
                )
                seed_num = gr.Number(value=0, label="Graine aléatoire (0 = aléatoire)")
                temp = gr.Slider(0.05, 5, step=.05, label="Température", value=.8)
                min_p = gr.Slider(0.00, 1.00, step=0.01, label="min_p (Recommandé 0.02-0.1, 0 = désactivé)", value=0.05)
                top_p = gr.Slider(0.00, 1.00, step=0.01, label="top_p (1.0 = désactivé recommandé)", value=1.00)
                repetition_penalty = gr.Slider(1.00, 2.00, step=0.01, label="Pénalité de répétition", value=1.00, info="1.00 = désactivé")
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
    demo.queue(max_size=50, default_concurrency_limit=1).launch(share=True, server_name="0.0.0.0", server_port=7860, inbrowser=True)
