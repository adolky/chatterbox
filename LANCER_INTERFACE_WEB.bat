@echo off
echo.
echo ╔═══════════════════════════════════════════════════════════════╗
echo ║                                                               ║
echo ║     🎙️  CHATTERBOX TTS - INTERFACE WEB                      ║
echo ║                                                               ║
echo ║     Lancement de l'interface graphique...                     ║
echo ║                                                               ║
echo ╚═══════════════════════════════════════════════════════════════╝
echo.

REM Définir le PYTHONPATH
set PYTHONPATH=%CD%\src

REM Activer l'environnement virtuel
call venv\Scripts\activate.bat

REM Lancer l'interface web
echo 🚀 Démarrage de l'interface web Gradio...
echo 🌐 L'interface s'ouvrira automatiquement dans votre navigateur
echo.
echo ⏸️  Pour arrêter l'interface, fermez cette fenêtre ou appuyez sur Ctrl+C
echo.

python interface_web.py

pause
