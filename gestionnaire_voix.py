#!/usr/bin/env python3
"""
Gestionnaire de bibliothèque de voix pour Chatterbox
Permet de lister, tester et gérer vos voix de référence
"""

import os
import argparse
from pathlib import Path
from typing import List, Dict

# Configuration
VOIX_DIR = Path(__file__).parent / "voix_bibliotheque"
EXTENSIONS_AUDIO = ['.wav', '.mp3', '.flac', '.ogg']


def lister_voix() -> Dict[str, List[Path]]:
    """Liste toutes les voix disponibles dans la bibliothèque"""
    voix = {
        'homme': [],
        'femme': [],
        'autres': [],
        'racine': []
    }
    
    if not VOIX_DIR.exists():
        print(f"❌ Le dossier {VOIX_DIR} n'existe pas")
        return voix
    
    # Parcourir les sous-dossiers
    for categorie in ['homme', 'femme', 'autres']:
        cat_dir = VOIX_DIR / categorie
        if cat_dir.exists():
            for fichier in cat_dir.iterdir():
                if fichier.suffix.lower() in EXTENSIONS_AUDIO:
                    voix[categorie].append(fichier)
    
    # Fichiers à la racine
    for fichier in VOIX_DIR.iterdir():
        if fichier.is_file() and fichier.suffix.lower() in EXTENSIONS_AUDIO:
            voix['racine'].append(fichier)
    
    return voix


def afficher_bibliotheque():
    """Affiche la bibliothèque de voix de manière organisée"""
    print("\n" + "="*70)
    print("🎤 BIBLIOTHÈQUE DE VOIX CHATTERBOX")
    print("="*70 + "\n")
    
    voix = lister_voix()
    total = sum(len(v) for v in voix.values())
    
    if total == 0:
        print("📭 Aucune voix trouvée dans la bibliothèque")
        print(f"\n💡 Ajoutez vos fichiers audio dans : {VOIX_DIR}")
        print("\n📖 Consultez voix_bibliotheque/README.md pour plus d'infos")
        return
    
    print(f"📊 Total : {total} voix disponibles\n")
    
    # Afficher par catégorie
    categories = [
        ('homme', '👨 Voix Homme'),
        ('femme', '👩 Voix Femme'),
        ('autres', '👤 Autres Voix'),
        ('racine', '📁 À la racine')
    ]
    
    for key, titre in categories:
        if voix[key]:
            print(f"\n{titre}")
            print("-" * 70)
            for i, fichier in enumerate(voix[key], 1):
                taille = fichier.stat().st_size / 1024  # Ko
                print(f"  {i:2d}. {fichier.name:40s} ({taille:>6.1f} Ko)")
    
    print("\n" + "="*70)
    print(f"\n📍 Chemin : {VOIX_DIR}")
    print("\n💡 Utilisation :")
    print(f"   python generer_long_audio_interactive.py --voix {voix['homme'][0].name if voix['homme'] else 'ma_voix.wav'}")
    print("="*70 + "\n")


def tester_voix(fichier: str):
    """Teste une voix avec un texte court"""
    import sys
    sys.path.insert(0, str(Path(__file__).parent / 'src'))
    
    from chatterbox import Chatterbox
    import torch
    
    # Chercher le fichier
    voix_path = None
    
    # Chercher dans la bibliothèque
    for root, dirs, files in os.walk(VOIX_DIR):
        if fichier in files:
            voix_path = Path(root) / fichier
            break
    
    # Ou chemin absolu/relatif
    if voix_path is None:
        voix_path = Path(fichier)
        if not voix_path.exists():
            print(f"❌ Fichier non trouvé : {fichier}")
            return
    
    print(f"\n🎤 Test de la voix : {voix_path.name}")
    print("="*70)
    print(f"📍 Chemin : {voix_path}")
    print(f"📊 Taille : {voix_path.stat().st_size / 1024:.1f} Ko")
    print("\n⏳ Génération en cours...")
    
    # Charger le modèle
    device = "cuda" if torch.cuda.is_available() else "cpu"
    tts = Chatterbox.from_pretrained(device=device)
    
    # Texte de test
    texte = "Bonjour ! Ceci est un test de voix. Comment trouvez-vous cette voix ?"
    
    # Générer
    output_path = Path("test_voix_") / voix_path.stem / ".wav"
    
    wav = tts.generate(
        text=texte,
        language="fr",
        audio_prompt_path=str(voix_path),
        exaggeration=0.5,
        temperature=0.8,
        cfg_weight=0.5
    )
    
    # Sauvegarder
    import scipy.io.wavfile as wavfile
    wavfile.write(str(output_path), 24000, wav)
    
    print(f"\n✅ Test généré : {output_path}")
    print(f"🎧 Écoutez le fichier pour évaluer la qualité")
    print("="*70 + "\n")


def ajouter_categories():
    """Crée les sous-dossiers de catégories s'ils n'existent pas"""
    categories = ['homme', 'femme', 'autres']
    
    for cat in categories:
        cat_dir = VOIX_DIR / cat
        if not cat_dir.exists():
            cat_dir.mkdir(parents=True)
            print(f"✅ Créé : {cat_dir}")
    
    print("\n📁 Structure créée :")
    print(f"   {VOIX_DIR}/")
    print(f"   ├── homme/")
    print(f"   ├── femme/")
    print(f"   └── autres/")


def main():
    parser = argparse.ArgumentParser(
        description="Gestionnaire de bibliothèque de voix Chatterbox",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples d'utilisation :

  # Lister toutes les voix
  python gestionnaire_voix.py --liste

  # Tester une voix
  python gestionnaire_voix.py --test voix_homme_neutre.wav

  # Créer la structure de dossiers
  python gestionnaire_voix.py --init

  # Rechercher une voix
  python gestionnaire_voix.py --chercher journaliste
        """
    )
    
    parser.add_argument('--liste', '-l',
                        action='store_true',
                        help='Lister toutes les voix disponibles')
    
    parser.add_argument('--test', '-t',
                        metavar='FICHIER',
                        help='Tester une voix avec un texte court')
    
    parser.add_argument('--init', '-i',
                        action='store_true',
                        help='Créer la structure de dossiers')
    
    parser.add_argument('--chercher', '-c',
                        metavar='MOT_CLE',
                        help='Chercher une voix par mot-clé')
    
    args = parser.parse_args()
    
    # Si aucun argument, afficher la liste
    if not any(vars(args).values()):
        afficher_bibliotheque()
        return
    
    if args.init:
        ajouter_categories()
    
    if args.liste:
        afficher_bibliotheque()
    
    if args.test:
        tester_voix(args.test)
    
    if args.chercher:
        voix = lister_voix()
        resultats = []
        
        for categorie, fichiers in voix.items():
            for fichier in fichiers:
                if args.chercher.lower() in fichier.name.lower():
                    resultats.append((categorie, fichier))
        
        if resultats:
            print(f"\n🔍 Résultats pour '{args.chercher}' :")
            print("="*70)
            for cat, fichier in resultats:
                print(f"  [{cat:8s}] {fichier.name}")
            print("="*70 + "\n")
        else:
            print(f"\n❌ Aucune voix trouvée pour '{args.chercher}'")


if __name__ == "__main__":
    main()
