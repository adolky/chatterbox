@echo off
chcp 65001 >nul
cls

echo ═══════════════════════════════════════════════════════════════════════
echo                    🔧 CORRECTION ERREUR NUMPY 🔧
echo ═══════════════════════════════════════════════════════════════════════
echo.
type "%~dp0CORRECTION_NUMPY.txt"
echo.
echo.
echo ═══════════════════════════════════════════════════════════════════════
echo.
echo Que voulez-vous faire ?
echo.
echo   [1] Tester l'installation (recommandé)
echo   [2] Lancer l'application maintenant
echo   [3] Voir le guide de dépannage
echo   [4] Quitter
echo.
set /p choix="Votre choix (1-4) : "

if "%choix%"=="1" (
    cls
    call "%~dp0TESTER_INSTALLATION.bat"
    goto :menu
)

if "%choix%"=="2" (
    cls
    call "%~dp0LANCER_INTERFACE_LONGUE_DUREE.bat"
    goto :end
)

if "%choix%"=="3" (
    start "" "%~dp0DEPANNAGE_ERREUR_NUMPY.md"
    goto :menu
)

if "%choix%"=="4" (
    goto :end
)

echo Choix invalide !
timeout /t 2 >nul
goto :menu

:menu
echo.
echo Appuyez sur une touche pour revenir au menu...
pause >nul
cls
goto :start

:end
