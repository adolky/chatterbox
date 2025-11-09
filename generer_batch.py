"""
GÉNÉRATEUR DE PODCAST PAR LOT - CHATTERBOX TTS
Traite plusieurs textes depuis un fichier texte
Licence MIT - Autorisé pour monétisation YouTube
"""

import os
import sys
import torch
import torchaudio as ta
from pathlib import Path
from datetime import datetime

# Ajout du chemin source
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from chatterbox.tts import ChatterboxTTS


class BatchPodcastGenerator:
    def __init__(self, device='cuda'):
        """Initialise le générateur batch"""
        print("=" * 70)
        print("📦 CHATTERBOX TTS - GÉNÉRATION PAR LOT")
        print("=" * 70)
        
        # Vérification GPU
        if device == 'cuda' and not torch.cuda.is_available():
            print("⚠️  CUDA non disponible, utilisation du CPU")
            device = 'cpu'
        
        if device == 'cuda':
            gpu_name = torch.cuda.get_device_name(0)
            vram = torch.cuda.get_device_properties(0).total_memory / 1024**3
            print(f"🎮 GPU: {gpu_name} ({vram:.1f} GB VRAM)")
        
        # Chargement modèle
        print("\n📥 Chargement du modèle Chatterbox...")
        self.model = ChatterboxTTS.from_pretrained(device=device)
        print(f"✅ Modèle chargé sur: {self.model.device}")
        
        # Dossiers
        self.output_dir = Path("podcasts_batch")
        self.output_dir.mkdir(exist_ok=True)
        
    def traiter_fichier(self, fichier_texte, prefixe="segment"):
        """
        Traite un fichier texte avec un texte par ligne
        
        Args:
            fichier_texte: Chemin vers le fichier .txt
            prefixe: Préfixe pour les fichiers générés
        """
        fichier_path = Path(fichier_texte)
        
        if not fichier_path.exists():
            print(f"❌ Fichier introuvable: {fichier_path}")
            return
        
        print(f"\n📖 Lecture du fichier: {fichier_path}")
        
        # Lire les lignes
        with open(fichier_path, 'r', encoding='utf-8') as f:
            lignes = [ligne.strip() for ligne in f if ligne.strip()]
        
        total = len(lignes)
        print(f"📊 {total} segments à traiter\n")
        
        if total == 0:
            print("❌ Aucun texte trouvé dans le fichier")
            return
        
        # Traiter chaque ligne
        resultats = {
            'success': 0,
            'errors': 0,
            'fichiers': []
        }
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        for i, texte in enumerate(lignes, 1):
            print("=" * 70)
            print(f"🎙️  SEGMENT {i}/{total}")
            print("=" * 70)
            print(f"📝 Texte: {texte[:80]}{'...' if len(texte) > 80 else ''}")
            
            # Nom du fichier
            nom_fichier = f"{prefixe}_{timestamp}_{i:03d}.wav"
            output_path = self.output_dir / nom_fichier
            
            try:
                # Génération
                print("⏳ Génération...")
                wav = self.model.generate(texte)
                
                duree = wav.shape[-1] / self.model.sr
                print(f"✅ Audio: {duree:.2f}s")
                
                # Sauvegarde
                ta.save(str(output_path), wav.cpu(), self.model.sr)
                print(f"💾 Sauvegardé: {nom_fichier}")
                
                resultats['success'] += 1
                resultats['fichiers'].append(str(output_path))
                
            except Exception as e:
                print(f"❌ Erreur: {e}")
                resultats['errors'] += 1
        
        # Rapport final
        print("\n" + "=" * 70)
        print("📊 RAPPORT FINAL")
        print("=" * 70)
        print(f"✅ Réussis: {resultats['success']}/{total}")
        print(f"❌ Erreurs: {resultats['errors']}/{total}")
        print(f"📁 Dossier: {self.output_dir.absolute()}")
        
        if resultats['fichiers']:
            print(f"\n📄 Fichiers générés:")
            for fichier in resultats['fichiers']:
                print(f"   • {Path(fichier).name}")
        
        return resultats


def creer_fichier_exemple():
    """Crée un fichier d'exemple"""
    exemple_path = Path("exemple_podcast.txt")
    
    if exemple_path.exists():
        print(f"ℹ️  Le fichier {exemple_path} existe déjà")
        return str(exemple_path)
    
    contenu = """Bonjour et bienvenue dans ce podcast généré par intelligence artificielle.
Aujourd'hui nous allons parler de la synthèse vocale moderne.
Chatterbox est un système open source développé par Resemble AI.
Il permet de créer des voix réalistes avec contrôle émotionnel.
Le modèle supporte vingt-trois langues différentes.
Vous pouvez utiliser cette technologie pour vos projets YouTube.
La licence MIT permet une utilisation commerciale complète.
Merci d'avoir écouté, à bientôt pour un prochain épisode!"""
    
    with open(exemple_path, 'w', encoding='utf-8') as f:
        f.write(contenu)
    
    print(f"✅ Fichier d'exemple créé: {exemple_path}")
    return str(exemple_path)


def main():
    """Point d'entrée principal"""
    print("=" * 70)
    print("🎬 GÉNÉRATEUR DE PODCAST PAR LOT")
    print("=" * 70)
    print("""
📖 FORMAT DU FICHIER TEXTE:
   • Un segment par ligne
   • Encodage UTF-8
   • Les lignes vides sont ignorées

💡 EXEMPLE:
   exemple_podcast.txt (8 segments)
    """)
    
    # Demander le fichier
    print("\n📂 Chemin du fichier texte (ou 'exemple' pour créer un exemple):")
    chemin = input("> ").strip()
    
    if chemin.lower() == 'exemple':
        chemin = creer_fichier_exemple()
        print(f"\nℹ️  Vous pouvez éditer ce fichier puis relancer le script")
        input("\nAppuyez sur ENTRÉE pour continuer avec cet exemple...")
    
    if not chemin:
        print("❌ Aucun fichier spécifié")
        return
    
    # Demander le préfixe
    print("\n🏷️  Préfixe pour les fichiers (ENTRÉE pour 'segment'):")
    prefixe = input("> ").strip() or "segment"
    
    try:
        # Créer le générateur
        generator = BatchPodcastGenerator(device='cuda')
        
        # Traiter le fichier
        generator.traiter_fichier(chemin, prefixe)
        
        print("\n✅ Traitement terminé!")
        
    except Exception as e:
        print(f"\n❌ Erreur: {e}")
        import traceback
        traceback.print_exc()
    
    input("\nAppuyez sur ENTRÉE pour fermer...")


if __name__ == "__main__":
    main()
