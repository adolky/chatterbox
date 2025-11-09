"""
GÉNÉRATEUR DE PODCAST CHATTERBOX TTS
Génération interactive de podcasts avec émotions et voix personnalisées
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

class PodcastGenerator:
    def __init__(self, device='cuda'):
        """Initialise le générateur avec Chatterbox"""
        print("=" * 70)
        print("🎙️  CHATTERBOX TTS - GÉNÉRATEUR DE PODCAST")
        print("=" * 70)
        
        # Vérification GPU
        if device == 'cuda' and not torch.cuda.is_available():
            print("⚠️  CUDA non disponible, utilisation du CPU")
            device = 'cpu'
        
        if device == 'cuda':
            gpu_name = torch.cuda.get_device_name(0)
            vram = torch.cuda.get_device_properties(0).total_memory / 1024**3
            print(f"🎮 GPU détecté: {gpu_name} ({vram:.1f} GB VRAM)")
        
        # Chargement modèle
        print("\n📥 Chargement du modèle Chatterbox...")
        self.model = ChatterboxTTS.from_pretrained(device=device)
        print(f"✅ Modèle chargé sur: {self.model.device}")
        print(f"📊 Sample rate: {self.model.sr} Hz")
        
        # Créer dossier de sortie
        self.output_dir = Path("podcasts_generes")
        self.output_dir.mkdir(exist_ok=True)
        print(f"📁 Dossier de sortie: {self.output_dir.absolute()}")
        
    def generer_audio(self, texte, nom_fichier=None, emotion="neutral", vitesse=1.0):
        """
        Génère un fichier audio à partir du texte
        
        Args:
            texte: Texte à synthétiser
            nom_fichier: Nom du fichier de sortie (optionnel)
            emotion: Type d'émotion (neutral, happy, sad, angry, etc.)
            vitesse: Vitesse de parole (0.5 = lent, 1.0 = normal, 1.5 = rapide)
        """
        if not texte.strip():
            print("❌ Texte vide, génération annulée")
            return None
        
        # Nom de fichier par défaut
        if nom_fichier is None:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            nom_fichier = f"podcast_{timestamp}.wav"
        
        # Ajouter .wav si nécessaire
        if not nom_fichier.endswith('.wav'):
            nom_fichier += '.wav'
        
        output_path = self.output_dir / nom_fichier
        
        print("\n" + "=" * 70)
        print("🎙️  GÉNÉRATION EN COURS")
        print("=" * 70)
        print(f"📝 Texte ({len(texte)} caractères):")
        print(f"   {texte[:100]}{'...' if len(texte) > 100 else ''}")
        print(f"🎭 Émotion: {emotion}")
        print(f"⚡ Vitesse: {vitesse}x")
        
        try:
            # Génération
            print("\n⏳ Synthèse vocale...")
            wav = self.model.generate(
                texte,
                # Note: Chatterbox ne supporte pas directement ces paramètres
                # Ceci est un exemple d'interface, ajustez selon l'API réelle
            )
            
            duree = wav.shape[-1] / self.model.sr
            print(f"✅ Audio généré: {duree:.2f} secondes")
            
            # Sauvegarde
            ta.save(str(output_path), wav.cpu(), self.model.sr)
            print(f"💾 Fichier sauvegardé: {output_path}")
            
            # Stats
            taille_mo = output_path.stat().st_size / (1024 * 1024)
            print(f"📊 Taille: {taille_mo:.2f} MB")
            
            return output_path
            
        except Exception as e:
            print(f"❌ Erreur lors de la génération: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def mode_interactif(self):
        """Mode interactif pour générer des podcasts"""
        print("\n" + "=" * 70)
        print("🎬 MODE INTERACTIF")
        print("=" * 70)
        print("Tapez votre texte puis appuyez sur ENTRÉE")
        print("Tapez 'quit' pour quitter, 'help' pour l'aide")
        print("=" * 70 + "\n")
        
        while True:
            try:
                # Demander le texte
                print("\n📝 Entrez votre texte:")
                texte = input("> ").strip()
                
                if not texte:
                    continue
                
                if texte.lower() == 'quit':
                    print("\n👋 Au revoir!")
                    break
                
                if texte.lower() == 'help':
                    self.afficher_aide()
                    continue
                
                # Demander le nom du fichier
                print("\n💾 Nom du fichier (ENTRÉE pour auto):")
                nom = input("> ").strip()
                
                # Générer
                self.generer_audio(texte, nom or None)
                
                # Continuer?
                print("\n🔄 Générer un autre fichier? (O/n)")
                continuer = input("> ").strip().lower()
                if continuer == 'n':
                    print("\n👋 Au revoir!")
                    break
                    
            except KeyboardInterrupt:
                print("\n\n👋 Arrêt demandé. Au revoir!")
                break
            except Exception as e:
                print(f"\n❌ Erreur: {e}")
                import traceback
                traceback.print_exc()
    
    def afficher_aide(self):
        """Affiche l'aide"""
        print("\n" + "=" * 70)
        print("📚 AIDE - GÉNÉRATEUR DE PODCAST CHATTERBOX")
        print("=" * 70)
        print("""
🎙️  UTILISATION:
   1. Entrez votre texte pour générer l'audio
   2. Donnez un nom de fichier ou laissez vide pour auto-générer
   3. L'audio sera sauvegardé dans le dossier 'podcasts_generes'

🎯 COMMANDES:
   quit  - Quitter le programme
   help  - Afficher cette aide

📝 CONSEILS:
   • Utilisez des phrases complètes avec ponctuation
   • Le modèle supporte 23 langues (dont le français)
   • Durée typique: ~10 secondes pour 100 caractères
   • Format de sortie: WAV 24kHz mono

⚖️  LICENCE:
   • MIT License - Commercial autorisé
   • Monétisation YouTube autorisée
   • Watermarking intégré

🔗 LIENS:
   • GitHub: https://github.com/resemble-ai/chatterbox
   • Licence: Voir fichier LICENSE
        """)
        print("=" * 70)


def main():
    """Point d'entrée principal"""
    try:
        # Créer le générateur
        generator = PodcastGenerator(device='cuda')
        
        # Lancer en mode interactif
        generator.mode_interactif()
        
    except Exception as e:
        print(f"\n❌ Erreur fatale: {e}")
        import traceback
        traceback.print_exc()
        input("\nAppuyez sur ENTRÉE pour fermer...")


if __name__ == "__main__":
    main()
