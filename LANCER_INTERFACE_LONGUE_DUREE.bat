@echo off
echo ========================================
echo  Chatterbox TTS - Version Longue Duree
echo ========================================
echo.
echo Lancement de l'interface Gradio amelioree...
echo - Support textes illimites (1-2h+)
echo - Chargement de fichiers texte
echo - Estimation automatique de duree
echo.

cd /d "%~dp0"

REM Vérifier si l'environnement virtuel existe
if exist "venv\Scripts\python.exe" (
    echo Utilisation de l'environnement virtuel...
    venv\Scripts\python.exe gradio_tts_app.py
) else (
    echo Environnement virtuel non trouve, utilisation de Python global...
    python gradio_tts_app.py
)

pause
