@echo off
chcp 65001 >nul
cls
type "%~dp0ERREURS_TOUTES_CORRIGEES.txt"
echo.
echo ════════════════════════════════════════════════════════════════════
echo.
echo [1] Lancer l'application maintenant
echo [2] Tester l'installation
echo [3] Quitter
echo.
set /p choix="Votre choix (1-3) : "

if "%choix%"=="1" (
    cls
    call "%~dp0LANCER_INTERFACE_LONGUE_DUREE.bat"
)

if "%choix%"=="2" (
    cls
    call "%~dp0TESTER_INSTALLATION.bat"
)

if "%choix%"=="3" (
    exit
)
