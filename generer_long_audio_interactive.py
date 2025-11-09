#!/usr/bin/env python3
"""
Générateur d'audios longs INTERACTIF (5-15 minutes)
Version améliorée avec choix de langue et voix
"""

import torch
import numpy as np
from pathlib import Path
import re
import argparse
from pydub import AudioSegment
from chatterbox.tts import ChatterboxTTS

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Voix de référence disponibles (vous pouvez ajouter les vôtres)
VOIX_PREDEFINES = {
    "defaut": None,  # Voix par défaut de Chatterbox
    "exemple_fr": "examples/reference_fr.wav",  # Si vous avez des exemples
    "exemple_en": "examples/reference_en.wav",
    # Ajoutez vos propres voix ici:
    # "ma_voix": "mes_voix/ma_voix.wav",
}

# Langues supportées par Chatterbox (auto-détection)
LANGUES_INFO = {
    "fr": "Français (French)",
    "en": "Anglais (English)",
    "es": "Espagnol (Spanish)",
    "de": "Allemand (German)",
    "it": "Italien (Italian)",
    "pt": "Portugais (Portuguese)",
    "pl": "Polonais (Polish)",
    "tr": "Turc (Turkish)",
    "ru": "Russe (Russian)",
    "nl": "Néerlandais (Dutch)",
    "cs": "Tchèque (Czech)",
    "ar": "Arabe (Arabic)",
    "zh-cn": "Chinois simplifié (Chinese simplified)",
    "ja": "Japonais (Japanese)",
    "ko": "Coréen (Korean)",
    "hi": "Hindi",
}

# Presets de tons/styles pour différents types de contenu
PRESETS_TONS = {
    "journaliste": {
        "nom": "📰 Journaliste TV/Radio",
        "description": "Ton professionnel, neutre et autoritaire. Pour actualités, reportages.",
        "exaggeration": 0.5,
        "temperature": 0.7,
        "cfg_weight": 0.6,
        "segment_size": 400,
        "pause_between_segments": 0.6,
    },
    "narrateur": {
        "nom": "📖 Narrateur audiobook",
        "description": "Ton calme et posé. Pour livres audio, histoires, contes.",
        "exaggeration": 0.4,
        "temperature": 0.7,
        "cfg_weight": 0.6,
        "segment_size": 450,
        "pause_between_segments": 0.8,
    },
    "podcast_info": {
        "nom": "🎙️ Podcast informatif",
        "description": "Ton conversationnel et accessible. Pour podcasts éducatifs.",
        "exaggeration": 0.6,
        "temperature": 0.8,
        "cfg_weight": 0.5,
        "segment_size": 400,
        "pause_between_segments": 0.7,
    },
    "podcast_dynamique": {
        "nom": "⚡ Podcast énergique",
        "description": "Ton dynamique et engageant. Pour podcasts divertissants.",
        "exaggeration": 0.7,
        "temperature": 0.9,
        "cfg_weight": 0.4,
        "segment_size": 350,
        "pause_between_segments": 0.6,
    },
    "publicite": {
        "nom": "📢 Publicité/Promo",
        "description": "Ton vendeur et enthousiaste. Pour pubs, annonces commerciales.",
        "exaggeration": 0.8,
        "temperature": 0.9,
        "cfg_weight": 0.3,
        "segment_size": 300,
        "pause_between_segments": 0.5,
    },
    "documentaire": {
        "nom": "🎬 Documentaire",
        "description": "Ton sérieux et contemplatif. Pour documentaires, analyses.",
        "exaggeration": 0.5,
        "temperature": 0.7,
        "cfg_weight": 0.6,
        "segment_size": 450,
        "pause_between_segments": 0.9,
    },
    "tutoriel": {
        "nom": "🎓 Tutoriel/Formation",
        "description": "Ton pédagogique et clair. Pour tutos, cours en ligne.",
        "exaggeration": 0.5,
        "temperature": 0.75,
        "cfg_weight": 0.5,
        "segment_size": 400,
        "pause_between_segments": 0.8,
    },
    "meditation": {
        "nom": "🧘 Méditation/Relaxation",
        "description": "Ton très calme et apaisant. Pour méditation guidée, ASMR.",
        "exaggeration": 0.3,
        "temperature": 0.6,
        "cfg_weight": 0.7,
        "segment_size": 500,
        "pause_between_segments": 1.2,
    },
    "storytelling": {
        "nom": "✨ Storytelling/Histoire",
        "description": "Ton expressif et captivant. Pour histoires, anecdotes.",
        "exaggeration": 0.7,
        "temperature": 0.85,
        "cfg_weight": 0.4,
        "segment_size": 400,
        "pause_between_segments": 0.7,
    },
    "enfant": {
        "nom": "🧒 Contenu pour enfants",
        "description": "Ton joyeux et animé. Pour histoires pour enfants.",
        "exaggeration": 0.8,
        "temperature": 0.9,
        "cfg_weight": 0.3,
        "segment_size": 350,
        "pause_between_segments": 0.8,
    },
    "personnalise": {
        "nom": "⚙️ Personnalisé",
        "description": "Choisir manuellement tous les paramètres.",
        "exaggeration": None,  # Sera demandé
        "temperature": None,
        "cfg_weight": None,
        "segment_size": None,
        "pause_between_segments": None,
    },
}

def split_text_smart(text, max_chars=500):
    """
    Découpe intelligente du texte en segments naturels
    Respecte les phrases, paragraphes, et ponctuation
    """
    # Diviser par paragraphes d'abord
    paragraphs = text.split('\n\n')
    segments = []
    current_segment = ""
    
    for para in paragraphs:
        # Diviser par phrases si le paragraphe est trop long
        sentences = re.split(r'(?<=[.!?])\s+', para)
        
        for sentence in sentences:
            if len(current_segment) + len(sentence) < max_chars:
                current_segment += sentence + " "
            else:
                if current_segment:
                    segments.append(current_segment.strip())
                current_segment = sentence + " "
        
        # Ajouter un marqueur de paragraphe
        if current_segment and current_segment not in segments:
            segments.append(current_segment.strip())
            current_segment = ""
    
    if current_segment:
        segments.append(current_segment.strip())
    
    return segments

def lire_fichier_texte(fichier_path):
    """Lit un fichier texte et retourne son contenu"""
    try:
        with open(fichier_path, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"❌ Erreur lecture fichier: {e}")
        return None

def generate_long_audio(
    text,
    output_path="output_long.wav",
    voice_reference=None,
    language=None,
    exaggeration=0.5,
    temperature=0.8,
    cfg_weight=0.5,
    segment_size=500,
    pause_between_segments=0.5
):
    """
    Génère un audio long en segments puis assemble
    
    Args:
        text: Texte complet (peut être très long)
        output_path: Fichier de sortie
        voice_reference: Fichier audio de référence pour cloner la voix
        language: Code langue (fr, en, etc.) - info seulement, détection auto
        exaggeration: Niveau d'expression (0.25-2.0)
        temperature: Créativité (0.05-5.0, recommandé: 0.7-1.0)
        cfg_weight: Contrôle du rythme (0.0-1.0)
        segment_size: Taille max de chaque segment (chars)
        pause_between_segments: Pause entre segments (secondes)
    """
    
    print(f"\n{'='*70}")
    print(f"🎙️  GÉNÉRATION AUDIO LONG - CHATTERBOX TTS")
    print(f"{'='*70}")
    print(f"📝 Texte: {len(text)} caractères (~{len(text)//6} mots)")
    print(f"⚙️  Device: {DEVICE}")
    if language:
        lang_name = LANGUES_INFO.get(language, language)
        print(f"🌍 Langue: {lang_name} (auto-détection par le modèle)")
    if voice_reference:
        print(f"🎤 Voix référence: {voice_reference}")
    else:
        print(f"🎤 Voix: Défaut Chatterbox")
    print(f"😊 Expression: {exaggeration}")
    print(f"🌡️  Température: {temperature}")
    print(f"⚡ CFG Weight: {cfg_weight}")
    print(f"✂️  Taille segments: {segment_size} caractères")
    print()
    
    # Découper le texte
    segments = split_text_smart(text, max_chars=segment_size)
    print(f"✂️  Texte découpé en {len(segments)} segments")
    
    # Charger le modèle
    print("🔄 Chargement du modèle Chatterbox...")
    model = ChatterboxTTS.from_pretrained(DEVICE)
    print(f"✅ Modèle chargé sur {DEVICE}")
    
    # Générer chaque segment
    audio_segments = []
    total_duration = 0
    
    print(f"\n{'─'*70}")
    print("🎵 GÉNÉRATION DES SEGMENTS")
    print(f"{'─'*70}")
    
    for i, segment in enumerate(segments, 1):
        print(f"\n[{i}/{len(segments)}] ({len(segment)} chars)")
        print(f"   📄 {segment[:60]}{'...' if len(segment) > 60 else ''}")
        
        # Générer l'audio
        wav = model.generate(
            segment,
            audio_prompt_path=voice_reference,
            exaggeration=exaggeration,
            temperature=temperature,
            cfg_weight=cfg_weight,
            min_p=0.05,
            top_p=1.0,
            repetition_penalty=1.2,
        )
        
        # Convertir en AudioSegment (pydub)
        wav_np = wav.squeeze(0).cpu().numpy()
        wav_int16 = (wav_np * 32767).astype(np.int16)
        
        audio_seg = AudioSegment(
            wav_int16.tobytes(),
            frame_rate=model.sr,
            sample_width=2,
            channels=1
        )
        
        duration = len(audio_seg) / 1000  # en secondes
        total_duration += duration
        print(f"   ✅ Généré: {duration:.1f}s")
        
        audio_segments.append(audio_seg)
        
        # Ajouter une pause entre segments (sauf dernier)
        if i < len(segments):
            pause = AudioSegment.silent(duration=int(pause_between_segments * 1000))
            audio_segments.append(pause)
            total_duration += pause_between_segments
    
    # Assembler tous les segments
    print(f"\n{'─'*70}")
    print(f"🔗 Assemblage de {len(segments)} segments audio...")
    final_audio = sum(audio_segments)
    
    # Sauvegarder
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    final_audio.export(str(output_path), format="wav")
    
    # Stats finales
    final_duration = len(final_audio) / 1000
    file_size = output_path.stat().st_size / (1024 * 1024)
    
    print(f"\n{'='*70}")
    print(f"✅ GÉNÉRATION TERMINÉE !")
    print(f"{'='*70}")
    print(f"📁 Fichier: {output_path.absolute()}")
    print(f"⏱️  Durée audio: {final_duration/60:.1f} min ({final_duration:.0f}s)")
    print(f"💾 Taille fichier: {file_size:.1f} MB")
    print(f"🎯 Ratio: {len(text)/final_duration:.1f} caractères/seconde")
    print(f"📊 Vitesse parole: ~{(len(text)/6)/final_duration*60:.0f} mots/minute")
    print(f"{'='*70}\n")
    
    return str(output_path)

def mode_interactif():
    """Mode interactif pour configurer et générer l'audio"""
    
    print("\n" + "="*70)
    print("🎙️  GÉNÉRATEUR D'AUDIOS LONGS - MODE INTERACTIF")
    print("="*70)
    
    # 1. Source du texte
    print("\n📝 SOURCE DU TEXTE")
    print("1. Saisir le texte directement")
    print("2. Charger depuis un fichier .txt")
    choix = input("\nVotre choix (1 ou 2): ").strip()
    
    if choix == "2":
        fichier = input("Chemin du fichier texte: ").strip().strip('"')
        text = lire_fichier_texte(fichier)
        if not text:
            print("❌ Impossible de lire le fichier. Abandon.")
            return
    else:
        print("\nCollez votre texte (terminez par une ligne vide puis Ctrl+Z puis Entrée sur Windows):")
        lines = []
        try:
            while True:
                line = input()
                lines.append(line)
        except EOFError:
            pass
        text = '\n'.join(lines).strip()
    
    if not text:
        print("❌ Aucun texte fourni. Abandon.")
        return
    
    print(f"✅ Texte chargé: {len(text)} caractères (~{len(text)//6} mots)")
    
    # 2. Langue
    print("\n🌍 LANGUE")
    print("Note: Chatterbox détecte automatiquement la langue du texte.")
    print("Langues supportées: Français, Anglais, Espagnol, Allemand, Italien, etc.")
    lang_code = input("Code langue pour info (fr/en/es/etc, Entrée=auto): ").strip().lower() or None
    
    # 3. Voix
    print("\n🎤 CHOIX DE LA VOIX")
    print("Options:")
    print("1. Voix par défaut Chatterbox")
    print("2. Choisir depuis la bibliothèque de voix")
    print("3. Utiliser votre propre fichier (chemin manuel)")
    
    voix_choix = input("\nVotre choix (1, 2 ou 3): ").strip()
    voice_reference = None
    
    if voix_choix == "2":
        # Lister les voix de la bibliothèque
        from pathlib import Path
        import os
        
        voix_dir = Path(__file__).parent / "voix_bibliotheque"
        extensions = ['.wav', '.mp3', '.flac', '.ogg']
        
        # Chercher toutes les voix
        voix_disponibles = []
        if voix_dir.exists():
            for root, dirs, files in os.walk(voix_dir):
                for fichier in files:
                    if Path(fichier).suffix.lower() in extensions:
                        chemin_complet = Path(root) / fichier
                        categorie = Path(root).name if Path(root).name != "voix_bibliotheque" else "racine"
                        voix_disponibles.append((categorie, fichier, chemin_complet))
        
        if not voix_disponibles:
            print("\n⚠️  Aucune voix trouvée dans la bibliothèque.")
            print(f"📁 Ajoutez vos fichiers audio dans : {voix_dir}")
            print("💡 Utilisez: python gestionnaire_voix.py --init")
            print("\n🔄 Retour à la voix par défaut...")
        else:
            print("\n🎤 BIBLIOTHÈQUE DE VOIX")
            print("="*70)
            
            # Grouper par catégorie
            categories = {}
            for cat, nom, chemin in voix_disponibles:
                if cat not in categories:
                    categories[cat] = []
                categories[cat].append((nom, chemin))
            
            # Afficher
            index_global = 1
            mapping = {}
            
            for cat in ['homme', 'femme', 'autres', 'racine']:
                if cat in categories:
                    emoji = {'homme': '👨', 'femme': '👩', 'autres': '👤', 'racine': '📁'}.get(cat, '📁')
                    print(f"\n{emoji} {cat.upper()}")
                    print("-"*70)
                    for nom, chemin in categories[cat]:
                        taille = chemin.stat().st_size / 1024
                        print(f"  {index_global:2d}. {nom:40s} ({taille:>6.1f} Ko)")
                        mapping[index_global] = chemin
                        index_global += 1
            
            print("="*70)
            
            # Choix
            choix_voix = input(f"\nChoisissez une voix (1-{len(voix_disponibles)}, Entrée=annuler): ").strip()
            
            if choix_voix and choix_voix.isdigit():
                index = int(choix_voix)
                if index in mapping:
                    voice_reference = str(mapping[index])
                    print(f"✅ Voix sélectionnée: {mapping[index].name}")
                else:
                    print("⚠️  Choix invalide. Voix par défaut utilisée.")
            else:
                print("🔄 Voix par défaut utilisée.")
    
    elif voix_choix == "3":
        print("\n💡 CONSEIL: Enregistrez 3-30 secondes de voix claire.")
        print("   - Bonne qualité audio (pas de bruit de fond)")
        print("   - Ton naturel et expressif")
        print("   - Format: WAV, MP3, FLAC, etc.")
        
        voice_file = input("\nChemin du fichier audio de référence: ").strip().strip('"')
        if Path(voice_file).exists():
            voice_reference = voice_file
            print(f"✅ Voix de référence: {voice_file}")
        else:
            print(f"⚠️  Fichier non trouvé. Utilisation de la voix par défaut.")
    
    # 4. Choix du ton/style (PRESETS)
    print("\n🎭 CHOIX DU TON/STYLE")
    print("="*70)
    print("Sélectionnez un preset pour votre type de contenu:")
    print()
    
    # Afficher tous les presets
    preset_keys = list(PRESETS_TONS.keys())
    for i, (key, preset) in enumerate(PRESETS_TONS.items(), 1):
        print(f"{i:2d}. {preset['nom']}")
        print(f"    {preset['description']}")
        print()
    
    print("="*70)
    
    # Choix du preset
    while True:
        choix_preset = input(f"\nVotre choix (1-{len(preset_keys)}, Entrée=3 Podcast informatif): ").strip()
        
        if not choix_preset:
            choix_preset = "3"  # Podcast informatif par défaut
        
        try:
            index = int(choix_preset) - 1
            if 0 <= index < len(preset_keys):
                preset_key = preset_keys[index]
                preset = PRESETS_TONS[preset_key]
                print(f"\n✅ Ton sélectionné: {preset['nom']}")
                break
            else:
                print(f"❌ Veuillez choisir entre 1 et {len(preset_keys)}")
        except ValueError:
            print("❌ Veuillez entrer un nombre")
    
    # Appliquer le preset ou demander les paramètres
    if preset_key == "personnalise":
        # Mode personnalisé - demander tous les paramètres
        print("\n⚙️  PARAMÈTRES PERSONNALISÉS")
        
        print("\n😊 Expression (exaggeration):")
        print("   0.5 = Neutre (recommandé)")
        print("   0.3-0.4 = Calme/sobre")
        print("   0.6-0.8 = Expressif/dynamique")
        exag_input = input("Expression (0.3-0.8, Entrée=0.5): ").strip()
        exaggeration = float(exag_input) if exag_input else 0.5
        
        print("\n🌡️  Température (créativité):")
        print("   0.7 = Stable")
        print("   0.8 = Équilibré (recommandé)")
        print("   1.0 = Plus créatif")
        temp_input = input("Température (0.7-1.0, Entrée=0.8): ").strip()
        temperature = float(temp_input) if temp_input else 0.8
        
        print("\n⚡ CFG Weight (contrôle du rythme):")
        print("   0.5 = Équilibré (recommandé)")
        cfg_input = input("CFG Weight (0.0-1.0, Entrée=0.5): ").strip()
        cfg_weight = float(cfg_input) if cfg_input else 0.5
        
        print("\n✂️  Taille des segments:")
        print("   300 = Petits segments (plus naturel, plus lent)")
        print("   400 = Moyen (recommandé)")
        print("   500 = Grands segments (plus rapide)")
        seg_input = input("Taille segment (300-500, Entrée=400): ").strip()
        segment_size = int(seg_input) if seg_input else 400
        
        print("\n⏸️  Pause entre segments:")
        print("   0.5s = Rapide")
        print("   0.8s = Normal (recommandé)")
        print("   1.0s = Lent/réfléchi")
        pause_input = input("Pause (0.5-1.0s, Entrée=0.8): ").strip()
        pause = float(pause_input) if pause_input else 0.8
    else:
        # Utiliser les paramètres du preset
        exaggeration = preset['exaggeration']
        temperature = preset['temperature']
        cfg_weight = preset['cfg_weight']
        segment_size = preset['segment_size']
        pause = preset['pause_between_segments']
        
        print(f"\n📋 Paramètres appliqués:")
        print(f"   Expression: {exaggeration}")
        print(f"   Température: {temperature}")
        print(f"   CFG Weight: {cfg_weight}")
        print(f"   Segments: {segment_size} caractères")
        print(f"   Pause: {pause}s")
    
    # 5. Fichier de sortie
    print("\n💾 FICHIER DE SORTIE")
    default_output = "podcasts_longs/mon_podcast.wav"
    output = input(f"Nom du fichier (Entrée={default_output}): ").strip() or default_output
    
    # Confirmation
    print("\n" + "="*70)
    print("📋 RÉCAPITULATIF")
    print("="*70)
    print(f"Texte: {len(text)} caractères")
    print(f"Langue: {LANGUES_INFO.get(lang_code, 'Auto-détection') if lang_code else 'Auto-détection'}")
    print(f"Voix: {'Référence: ' + voice_reference if voice_reference else 'Défaut Chatterbox'}")
    print(f"Expression: {exaggeration}")
    print(f"Température: {temperature}")
    print(f"CFG: {cfg_weight}")
    print(f"Segments: {segment_size} chars")
    print(f"Pause: {pause}s")
    print(f"Sortie: {output}")
    print("="*70)
    
    confirm = input("\n✅ Lancer la génération ? (o/n): ").strip().lower()
    
    if confirm not in ['o', 'oui', 'y', 'yes']:
        print("❌ Génération annulée.")
        return
    
    # Génération
    generate_long_audio(
        text=text,
        output_path=output,
        voice_reference=voice_reference,
        language=lang_code,
        exaggeration=exaggeration,
        temperature=temperature,
        cfg_weight=cfg_weight,
        segment_size=segment_size,
        pause_between_segments=pause
    )
    
    print("🎉 Terminé ! Votre podcast est prêt pour YouTube !")

def main():
    parser = argparse.ArgumentParser(
        description="Générateur d'audios longs avec Chatterbox TTS",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
  # Mode interactif
  python generer_long_audio_interactive.py
  
  # Avec preset de ton
  python generer_long_audio_interactive.py --texte script.txt --ton journaliste
  
  # Avec voix personnalisée
  python generer_long_audio_interactive.py --texte script.txt --voix ma_voix.wav --ton podcast_dynamique
  
  # Paramètres personnalisés
  python generer_long_audio_interactive.py --texte script.txt --expression 0.6 --temperature 0.8
  
Presets disponibles: journaliste, narrateur, podcast_info, podcast_dynamique, publicite, 
                    documentaire, tutoriel, meditation, storytelling, enfant
        """
    )
    
    parser.add_argument('--texte', '-t', help='Fichier texte source (.txt)')
    parser.add_argument('--output', '-o', help='Fichier audio de sortie (.wav)')
    parser.add_argument('--voix', '-v', help='Fichier audio de référence pour cloner la voix')
    parser.add_argument('--langue', '-l', choices=list(LANGUES_INFO.keys()), 
                        help='Code langue (info seulement, auto-détection)')
    parser.add_argument('--ton', choices=[k for k in PRESETS_TONS.keys() if k != 'personnalise'],
                        help='Preset de ton/style (journaliste, narrateur, podcast_info, etc.)')
    parser.add_argument('--expression', '-e', type=float,
                        help='Niveau d\'expression (0.25-2.0, ignoré si --ton utilisé)')
    parser.add_argument('--temperature', type=float,
                        help='Créativité (0.05-5.0, ignoré si --ton utilisé)')
    parser.add_argument('--cfg', type=float,
                        help='CFG weight (0.0-1.0, ignoré si --ton utilisé)')
    parser.add_argument('--segment', '-s', type=int,
                        help='Taille des segments en caractères (ignoré si --ton utilisé)')
    parser.add_argument('--pause', '-p', type=float,
                        help='Pause entre segments en secondes (ignoré si --ton utilisé)')
    
    args = parser.parse_args()
    
    # Si aucun argument, mode interactif
    if not args.texte:
        mode_interactif()
        return
    
    # Mode ligne de commande
    text = lire_fichier_texte(args.texte)
    if not text:
        print(f"❌ Impossible de lire {args.texte}")
        return
    
    output = args.output or "podcasts_longs/output.wav"
    
    # Déterminer les paramètres (preset ou manuel)
    if args.ton:
        preset = PRESETS_TONS[args.ton]
        print(f"🎭 Ton sélectionné: {preset['nom']}")
        exaggeration = preset['exaggeration']
        temperature = preset['temperature']
        cfg_weight = preset['cfg_weight']
        segment_size = preset['segment_size']
        pause = preset['pause_between_segments']
    else:
        # Paramètres manuels avec valeurs par défaut
        exaggeration = args.expression if args.expression is not None else 0.5
        temperature = args.temperature if args.temperature is not None else 0.8
        cfg_weight = args.cfg if args.cfg is not None else 0.5
        segment_size = args.segment if args.segment is not None else 400
        pause = args.pause if args.pause is not None else 0.8
    
    generate_long_audio(
        text=text,
        output_path=output,
        voice_reference=args.voix,
        language=args.langue,
        exaggeration=exaggeration,
        temperature=temperature,
        cfg_weight=cfg_weight,
        segment_size=segment_size,
        pause_between_segments=pause
    )

if __name__ == "__main__":
    main()
