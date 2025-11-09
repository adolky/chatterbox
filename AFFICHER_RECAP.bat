@echo off
chcp 65001 >nul
cls
type "%~dp0RECAP_VISUEL.txt"
echo.
echo ══════════════════════════════════════════════════════════════════════
echo.
echo Voulez-vous lancer l'application maintenant ? (O/N)
set /p choice="Votre choix : "

if /i "%choice%"=="O" (
    echo.
    echo Lancement de l'application...
    python "%~dp0gradio_tts_app.py"
) else (
    echo.
    echo Vous pouvez la lancer plus tard en double-cliquant sur :
    echo LANCER_INTERFACE_LONGUE_DUREE.bat
    echo.
)

pause
