@echo off
chcp 65001 >nul
echo.
echo ╔════════════════════════════════════════════════════════════════════╗
echo ║         🎙️  CHATTERBOX TTS - GÉNÉRATEUR DE PODCAST 🎙️             ║
echo ║                    Resemble.AI MIT License                         ║
echo ╚════════════════════════════════════════════════════════════════════╝
echo.
echo 📦 Activation de l'environnement virtuel...
call venv\Scripts\activate.bat

set PYTHONPATH=%CD%\src

echo.
echo ✅ Environnement prêt !
echo.
echo 🚀 Options disponibles:
echo    1. python generer_podcast.py       - Génération interactive
echo    2. python generer_batch.py         - Génération par lot
echo    3. python test_chatterbox.py       - Test rapide
echo.
cmd /k
