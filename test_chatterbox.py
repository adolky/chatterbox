"""Test Chatterbox TTS avec GPU RTX 3060 Ti"""

import torch
import torchaudio as ta

# Vérification CUDA
print("=" * 60)
print("🔍 VÉRIFICATION MATÉRIEL")
print("=" * 60)
print(f"CUDA disponible: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"GPU: {torch.cuda.get_device_name(0)}")
    print(f"VRAM totale: {torch.cuda.get_device_properties(0).total_memory / 1024**3:.1f} GB")
    print(f"VRAM disponible: {torch.cuda.memory_allocated(0) / 1024**3:.1f} GB utilisée")

# Import Chatterbox
print("\n" + "=" * 60)
print("📦 CHARGEMENT CHATTERBOX")
print("=" * 60)

try:
    from chatterbox.tts import ChatterboxTTS
    print("✓ Module chatterbox importé avec succès")
except ImportError as e:
    print(f"✗ Erreur d'import: {e}")
    print("\nℹ️  Installation manquante. Installez avec:")
    print("   pip install git+https://github.com/resemble-ai/chatterbox.git")
    exit(1)

# Chargement du modèle
print("\n📥 Téléchargement du modèle Chatterbox (première fois uniquement)...")
print("   Cela peut prendre plusieurs minutes...")

model = ChatterboxTTS.from_pretrained(device='cuda')
print(f"✓ Modèle chargé sur: {model.device}")

# Test génération français
print("\n" + "=" * 60)
print("🎙️ GÉNÉRATION AUDIO - TEST FRANÇAIS")
print("=" * 60)

texte = "Bonjour ! Bienvenue sur mon podcast généré par intelligence artificielle. Chatterbox est un système de synthèse vocale avec contrôle émotionnel."

print(f"Texte: {texte}")
print("Génération en cours...")

wav = model.generate(texte)
print(f"✓ Audio généré: {wav.shape}")
print(f"  - Durée: {wav.shape[-1] / model.sr:.2f} secondes")
print(f"  - Sample rate: {model.sr} Hz")

# Sauvegarde
output_path = "test_chatterbox_fr.wav"
ta.save(output_path, wav.cpu(), model.sr)
print(f"✓ Audio sauvegardé: {output_path}")

print("\n" + "=" * 60)
print("✅ TEST TERMINÉ AVEC SUCCÈS")
print("=" * 60)
print("\nℹ️  Licence: MIT (monétisation YouTube autorisée)")
print("ℹ️  Langues supportées: 23 (dont français)")
print("ℹ️  Fonctionnalités: émotions, clonage vocal, watermarking")
