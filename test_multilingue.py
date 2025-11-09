"""
TEST MULTILINGUE - CHATTERBOX TTS
Teste la génération audio en plusieurs langues
"""

import sys
from pathlib import Path
import torch
import torchaudio as ta

# Ajout du chemin source
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from chatterbox.tts import ChatterboxTTS

print("=" * 70)
print("🌍 TEST MULTILINGUE - CHATTERBOX TTS")
print("=" * 70)

# Textes dans différentes langues
textes_multilingues = {
    'français': "Bonjour, bienvenue dans notre podcast multilingue!",
    'english': "Hello, welcome to our multilingual podcast!",
    'español': "¡Hola, bienvenido a nuestro podcast multilingüe!",
    'deutsch': "Hallo, willkommen zu unserem mehrsprachigen Podcast!",
    'italiano': "Ciao, benvenuto nel nostro podcast multilingue!",
    'português': "Olá, bem-vindo ao nosso podcast multilíngue!",
    '中文': "你好，欢迎来到我们的多语言播客！",
    '日本語': "こんにちは、私たちの多言語ポッドキャストへようこそ！",
    '한국어': "안녕하세요, 다국어 팟캐스트에 오신 것을 환영합니다!",
}

# Vérification GPU
if torch.cuda.is_available():
    device = 'cuda'
    print(f"✅ GPU: {torch.cuda.get_device_name(0)}")
else:
    device = 'cpu'
    print("⚠️  CPU utilisé (pas de CUDA)")

# Chargement du modèle
print("\n📥 Chargement du modèle...")
model = ChatterboxTTS.from_pretrained(device=device)
print(f"✅ Modèle chargé sur: {model.device}")

# Créer le dossier de sortie
output_dir = Path("tests_multilingues")
output_dir.mkdir(exist_ok=True)

print(f"\n📁 Dossier de sortie: {output_dir.absolute()}")
print("\n" + "=" * 70)
print("🎙️  GÉNÉRATION AUDIO PAR LANGUE")
print("=" * 70)

resultats = []

for langue, texte in textes_multilingues.items():
    print(f"\n🌐 {langue.upper()}")
    print(f"   Texte: {texte}")
    
    try:
        # Génération
        print("   ⏳ Génération...")
        wav = model.generate(texte)
        
        # Informations
        duree = wav.shape[-1] / model.sr
        print(f"   ✅ Durée: {duree:.2f}s")
        
        # Sauvegarde
        nom_fichier = f"test_{langue.replace(' ', '_')}.wav"
        output_path = output_dir / nom_fichier
        ta.save(str(output_path), wav.cpu(), model.sr)
        print(f"   💾 Sauvegardé: {nom_fichier}")
        
        resultats.append({
            'langue': langue,
            'success': True,
            'duree': duree,
            'fichier': nom_fichier
        })
        
    except Exception as e:
        print(f"   ❌ Erreur: {e}")
        resultats.append({
            'langue': langue,
            'success': False,
            'erreur': str(e)
        })

# Rapport final
print("\n" + "=" * 70)
print("📊 RAPPORT FINAL")
print("=" * 70)

success = sum(1 for r in resultats if r['success'])
total = len(resultats)

print(f"\n✅ Réussis: {success}/{total} langues")
print(f"❌ Échecs: {total - success}/{total}")

print("\n📄 Fichiers générés:")
for r in resultats:
    if r['success']:
        print(f"   ✅ {r['langue']:15} → {r['fichier']:30} ({r['duree']:.2f}s)")
    else:
        print(f"   ❌ {r['langue']:15} → Échec")

print(f"\n📁 Tous les fichiers sont dans: {output_dir.absolute()}")

print("\n" + "=" * 70)
print("✅ TEST MULTILINGUE TERMINÉ")
print("=" * 70)
print("""
ℹ️  NOTES:
   • Chatterbox supporte 23 langues
   • La qualité peut varier selon la langue
   • Certaines langues nécessitent une meilleure prononciation du texte
   • Licence MIT - Utilisation commerciale autorisée
""")
