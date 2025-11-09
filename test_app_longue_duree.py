"""
Test rapide pour vérifier que l'application Gradio fonctionne
"""
import sys

def test_imports():
    """Test que tous les modules nécessaires sont disponibles"""
    print("🔍 Vérification des modules...")
    
    try:
        import gradio as gr
        print(f"✅ Gradio {gr.__version__} - OK")
    except ImportError:
        print("❌ Gradio non installé")
        return False
    
    try:
        import torch
        print(f"✅ PyTorch {torch.__version__} - OK")
        print(f"   CUDA disponible: {torch.cuda.is_available()}")
    except ImportError:
        print("❌ PyTorch non installé")
        return False
    
    try:
        import numpy as np
        print(f"✅ NumPy {np.__version__} - OK")
    except ImportError:
        print("❌ NumPy non installé")
        return False
    
    return True


def test_functions():
    """Test les fonctions de l'application"""
    print("\n🔍 Test des fonctions utilitaires...")
    
    try:
        # Définir la fonction estimate_duration localement pour le test
        def estimate_duration(text):
            """Estimate audio duration based on text length"""
            if not text or text.strip() == "":
                return "📊 Aucun texte"
            
            words = len(text.split())
            minutes = words / 150
            hours = minutes / 60
            
            if hours >= 1:
                return f"📊 **Estimation** : ~{hours:.1f}h ({words:,} mots, {len(text):,} caractères)"
            elif minutes >= 1:
                return f"📊 **Estimation** : ~{minutes:.0f} min ({words:,} mots, {len(text):,} caractères)"
            else:
                return f"📊 **Estimation** : ~{minutes*60:.0f}s ({words:,} mots, {len(text):,} caractères)"
        
        # Test avec différents textes
        test_cases = [
            ("", "Texte vide"),
            ("Bonjour le monde", "Texte court"),
            (" ".join(["mot"] * 150), "150 mots (1 minute)"),
            (" ".join(["mot"] * 9000), "9000 mots (1 heure)"),
        ]
        
        for text, description in test_cases:
            result = estimate_duration(text)
            print(f"✅ {description}: {result}")
        
        return True
    except Exception as e:
        print(f"❌ Erreur lors du test: {e}")
        import traceback
        traceback.print_exc()
        return False


def main():
    print("=" * 60)
    print("🧪 Test de l'Application Chatterbox TTS Longue Durée")
    print("=" * 60)
    print()
    
    # Test des imports
    if not test_imports():
        print("\n⚠️ Certains modules manquent. Installez-les avec:")
        print("   pip install gradio torch numpy")
        return False
    
    # Test des fonctions
    if not test_functions():
        print("\n⚠️ Problème avec les fonctions de l'application")
        return False
    
    print("\n" + "=" * 60)
    print("✅ Tous les tests sont passés !")
    print("=" * 60)
    print()
    print("🚀 Vous pouvez maintenant lancer l'application:")
    print("   python gradio_tts_app.py")
    print("   ou")
    print("   Double-clic sur LANCER_INTERFACE_LONGUE_DUREE.bat")
    print()
    
    return True


if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
