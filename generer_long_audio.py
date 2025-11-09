#!/usr/bin/env python3
"""
Générateur d'audios longs (5-15 minutes)
Optimisé pour les podcasts YouTube
"""

import torch
import numpy as np
from pathlib import Path
import re
from pydub import AudioSegment
from chatterbox.tts import ChatterboxTTS

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

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

def generate_long_audio(
    text,
    output_path="output_long.wav",
    voice_reference=None,
    exaggeration=0.5,
    segment_size=500,
    pause_between_segments=0.5
):
    """
    Génère un audio long en segments puis assemble
    
    Args:
        text: Texte complet (peut être très long)
        output_path: Fichier de sortie
        voice_reference: Fichier audio de référence pour cloner la voix
        exaggeration: Niveau d'expression (0.25-2.0)
        segment_size: Taille max de chaque segment (chars)
        pause_between_segments: Pause entre segments (secondes)
    """
    
    print(f"🎙️  GÉNÉRATION AUDIO LONG")
    print(f"📝 Texte: {len(text)} caractères (~{len(text)//6} mots)")
    print(f"⚙️  Device: {DEVICE}")
    print()
    
    # Découper le texte
    segments = split_text_smart(text, max_chars=segment_size)
    print(f"✂️  Texte découpé en {len(segments)} segments")
    
    # Charger le modèle
    print("🔄 Chargement du modèle...")
    model = ChatterboxTTS.from_pretrained(DEVICE)
    
    # Générer chaque segment
    audio_segments = []
    total_duration = 0
    
    for i, segment in enumerate(segments, 1):
        print(f"\n🎵 Segment {i}/{len(segments)} ({len(segment)} chars)")
        print(f"   Texte: {segment[:50]}...")
        
        # Générer l'audio
        wav = model.generate(
            segment,
            audio_prompt_path=voice_reference,
            exaggeration=exaggeration,
            temperature=0.8,
            cfg_weight=0.5,
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
    
    # Assembler tous les segments
    print(f"\n🔗 Assemblage de {len(audio_segments)} segments...")
    final_audio = sum(audio_segments)
    
    # Sauvegarder
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    final_audio.export(str(output_path), format="wav")
    
    # Stats finales
    final_duration = len(final_audio) / 1000
    file_size = output_path.stat().st_size / (1024 * 1024)
    
    print(f"\n✅ TERMINÉ !")
    print(f"📁 Fichier: {output_path}")
    print(f"⏱️  Durée: {final_duration/60:.1f} minutes ({final_duration:.0f}s)")
    print(f"💾 Taille: {file_size:.1f} MB")
    print(f"🎯 Ratio: {len(text)/final_duration:.1f} caractères/seconde")
    
    return str(output_path)

# Exemple d'utilisation
if __name__ == "__main__":
    # Exemple de texte long (podcast fictif)
    long_text = """
L'Odyssée des Réseaux Informatiques : De l'Arpanet au Cloud
Chapitre 1 : Les Prémices de la Connexion
L'histoire des réseaux informatiques n'a pas commencé avec des ordinateurs, mais avec le désir humain de communiquer rapidement sur de longues distances. Bien avant les câbles à fibres optiques et le Wi-Fi, les systèmes de communication précoces, comme le télégraphe optique de Claude Chappe à la fin du XVIIIe siècle, ont démontré la puissance de la transmission d'informations codées. Ce n'était pas de l'informatique, mais c'était le début de la réflexion sur les réseaux.
Avec l'avènement de l'électricité, le télégraphe électrique, puis le téléphone, ont permis des communications instantanées, posant les bases physiques et conceptuelles pour ce qui allait suivre. L'idée de "réseau" – un ensemble de nœuds interconnectés pour échanger des informations – était déjà bien ancrée.
Dans les années 1950 et 1960, les premiers ordinateurs étaient de vastes machines isolées, traitant les données par lots. Cependant, des penseurs visionnaires ont commencé à imaginer un avenir où ces machines pourraient se parler entre elles. Des personnalités comme J.C.R. Licklider, de l'ARPA (Advanced Research Projects Agency) aux États-Unis, ont conceptualisé un "réseau galactique" où chacun pourrait accéder à des données et des programmes depuis n'importe où.
Chapitre 2 : La Naissance d'ARPANET et le Paquet Révolutionnaire
La véritable percée dans les réseaux informatiques est survenue avec le projet ARPANET. Financé par l'ARPA, l'objectif était de créer un réseau de communication robuste, capable de résister à une panne partielle (une préoccupation majeure pendant la guerre froide).
La découverte clé a été la commutation de paquets, une idée développée indépendamment par Paul Baran et Donald Davies. Contrairement à la commutation de circuits (utilisée par le téléphone, où une ligne dédiée est établie pour la durée de la communication), la commutation de paquets décompose les messages en petits blocs de données, ou "paquets". Chaque paquet peut voyager indépendamment à travers le réseau, en suivant le chemin le plus efficace, et être réassemblé à destination. Cela rendait le réseau plus efficace et résilient.
Le 29 octobre 1969, la première liaison ARPANET a été établie entre l'Université de Californie à Los Angeles (UCLA) et le Stanford Research Institute (SRI). Le premier message envoyé fut "LO" (pour "LOGIN"), avant que le système ne plante. Cet instant a marqué la naissance technique d'Internet. Le premier IMP (Interface Message Processor), précurseur du routeur moderne, a joué un rôle crucial dans la gestion de ces paquets.
Chapitre 3 : L'Universalité grâce aux Protocoles (TCP/IP)
Au début des années 1970, ARPANET se développait, mais il restait un réseau fermé. Pour connecter différents réseaux entre eux (le concept d'"internetworking"), un langage universel était nécessaire. Vinton Cerf et Robert Kahn ont été les architectes de cette solution.
Leur découverte majeure a été le développement des protocoles TCP (Transmission Control Protocol) et IP (Internet Protocol). Le protocole IP gère l'adressage et le routage des paquets, s'assurant qu'ils arrivent à la bonne destination. Le protocole TCP, lui, garantit que tous les paquets arrivent, dans le bon ordre, et sans erreur.
Le 1er janvier 1983 est une date clé : ARPANET a officiellement basculé vers TCP/IP, marquant la naissance formelle de ce que nous appelons aujourd'hui Internet. Cette standardisation a permis à n'importe quel réseau, qu'il soit universitaire, militaire ou d'entreprise, de se connecter et de communiquer, créant un véritable "réseau de réseaux".
Chapitre 4 : La Démocratisation et le World Wide Web
Pendant longtemps, Internet est resté un outil principalement utilisé par les chercheurs, les universitaires et les militaires. L'interface était complexe et peu intuitive. Le grand public n'avait pas encore accès à cette révolution.
C'est au CERN, en Suisse, que tout a changé. En 1989, un jeune chercheur britannique nommé Tim Berners-Lee a proposé un système pour faciliter le partage d'informations entre physiciens. Sa découverte n'était pas un nouveau réseau, mais une couche d'application révolutionnaire : le World Wide Web (le Web).
Le Web reposait sur trois piliers technologiques :
HTML (HyperText Markup Language) : Un langage pour structurer les documents.
URL (Uniform Resource Locator) : Une adresse unique pour chaque ressource sur le réseau.
HTTP (HyperText Transfer Protocol) : Un protocole pour transférer ces documents.
En 1990, Berners-Lee a créé le premier navigateur web et le premier serveur web. Surtout, en 1993, le CERN a pris la décision capitale de rendre la technologie du Web libre de droits, permettant son adoption massive.
Chapitre 5 : L'Ère de la Mobilité et le Futur des Réseaux
Les années 1990 et 2000 ont vu l'explosion d'Internet grâce au Web et à l'accès grand public via les modems, puis l'ADSL et la fibre optique. D'autres découvertes et innovations ont été essentielles :
Ethernet : Développé par Robert Metcalfe et David Boggs chez Xerox PARC, Ethernet est devenu le standard dominant pour les réseaux locaux (LAN), permettant des connexions rapides et fiables dans les bureaux et les foyers.
Le Wi-Fi : Issu des travaux de plusieurs chercheurs, notamment en Australie, le Wi-Fi (basé sur la norme IEEE 802.11) a libéré les appareils des câbles, inaugurant l'ère de la mobilité.
Le Cloud Computing : Plus récemment, le développement d'architectures de cloud computing a transformé l'ordinateur personnel en un simple terminal, la puissance de calcul et le stockage résidant dans de vastes centres de données accessibles via Internet.
Aujourd'hui, les réseaux informatiques sont le système nerveux de notre société. Des milliards d'appareils sont connectés, des smartphones aux objets intelligents. Les découvertes continues dans des domaines comme l'Internet des objets (IoT), l'intelligence artificielle et les réseaux 5G et 6G continuent de repousser les limites de ce qui est possible, façonnant un avenir toujours plus interconnecté. Chaque jour, de nouvelles découvertes enrichissent cette incroyable odyssée de la connexion.
    """.strip()
    
    print("=" * 70)
    print("EXEMPLE : Génération d'un podcast de 5 minutes")
    print("=" * 70)
    
    # Générer l'audio
    output_file = generate_long_audio(
        text=long_text,
        output_path="podcasts_longs/podcast_ia_5min.wav",
        voice_reference=None,  # Ou spécifiez un fichier pour cloner une voix
        exaggeration=0.6,      # Un peu plus expressif pour un podcast
        segment_size=400,      # Segments plus petits pour plus de naturel
        pause_between_segments=0.8  # Pause entre phrases
    )
    
    print("\n" + "=" * 70)
    print("Vous pouvez maintenant uploader ce fichier sur YouTube !")
    print("=" * 70)
