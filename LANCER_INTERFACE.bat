@echo off
chcp 65001 >nul
echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║                                                               ║
echo ║     🎙️  CHATTERBOX TTS - INTERFACE WEB                      ║
echo ║                                                               ║
echo ║     Interface officielle Resemble.AI                          ║
echo ║     ✅ Accessible depuis d'autres PC (lien public)            ║
echo ║                                                               ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.

REM Définir le PYTHONPATH
set PYTHONPATH=%CD%\src

REM Activer l'environnement virtuel
call venv\Scripts\activate.bat

echo 🚀 Lancement de l'interface web...
echo.
echo ⏳ Chargement en cours (20-30 secondes)...
echo    - Chargement des bibliothèques Python
echo    - Initialisation de Gradio
echo    - Création du lien public
echo.
echo 📱 ACCÈS DEPUIS D'AUTRES PC :
echo    Un lien public sera généré (ex: https://xxxxx.gradio.live)
echo    Partagez ce lien pour un accès depuis n'importe quel appareil
echo.
echo 🌐 ACCÈS LOCAL :
echo    http://127.0.0.1:7860 (sur ce PC uniquement)
echo.
echo ⏸️  Pour arrêter: Ctrl+C ou fermez cette fenêtre
echo.
echo ═══════════════════════════════════════════════════════════════
echo.

python gradio_tts_app.py

pause
