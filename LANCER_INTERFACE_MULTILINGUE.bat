@echo off
echo ========================================
echo   Chatterbox TTS - Longue Duree v1.1
echo   Avec Support Multilingue (24 langues)
echo   Et Sauvegarde de Voix
echo ========================================
echo.

cd /d "%~dp0"

echo [1/3] Verification de l'environnement...
if not exist "venv\Scripts\python.exe" (
    echo ERREUR: Environnement virtuel non trouve!
    echo Veuillez executer l'installation d'abord.
    pause
    exit /b 1
)

echo [2/3] Verification du dossier de sauvegarde des voix...
if not exist "voix_sauvegardees" (
    mkdir "voix_sauvegardees"
    echo Dossier 'voix_sauvegardees' cree
)

echo [3/3] Lancement de l'application...
echo.
echo ========================================
echo  NOUVELLES FONCTIONNALITES v1.1 :
echo  - 24 langues supportees
echo  - Sauvegarde et gestion de voix
echo  - Interface amelioree
echo ========================================
echo.
echo L'application va s'ouvrir dans votre navigateur...
echo Pour arreter : Fermez cette fenetre ou appuyez sur Ctrl+C
echo.

venv\Scripts\python.exe gradio_tts_app.py

if errorlevel 1 (
    echo.
    echo ERREUR lors du lancement!
    echo Consultez GUIDE_UTILISATION.md pour l'aide
    pause
)
