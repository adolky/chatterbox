@echo off
REM ========================================
REM CHATTERBOX TTS - MODE PRODUCTION
REM D\u00e9marrage automatique avec gestion d'erreurs
REM ========================================

TITLE Chatterbox TTS - Mode Production

REM D\u00e9finir le chemin du projet
set PROJECT_DIR=c:\Users\adolk\Documents\Youtube ai audio\chatterbox
set LOG_DIR=%PROJECT_DIR%\logs
set VENV_PYTHON=%PROJECT_DIR%\venv\Scripts\python.exe
set APP_SCRIPT=%PROJECT_DIR%\gradio_tts_app.py

REM Cr\u00e9er le dossier de logs s'il n'existe pas
if not exist "%LOG_DIR%" mkdir "%LOG_DIR%"

REM Fichier de log avec timestamp
for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value') do set datetime=%%I
set TIMESTAMP=%datetime:~0,8%_%datetime:~8,6%
set LOG_FILE=%LOG_DIR%\app_%TIMESTAMP%.log

echo ======================================== >> "%LOG_FILE%"
echo DEMARRAGE CHATTERBOX TTS - MODE PRODUCTION >> "%LOG_FILE%"
echo Date: %date% %time% >> "%LOG_FILE%"
echo ======================================== >> "%LOG_FILE%"
echo.

echo [%time%] D\u00e9marrage de Chatterbox TTS en mode production...
echo [%time%] D\u00e9marrage de Chatterbox TTS en mode production... >> "%LOG_FILE%"

REM Changer vers le r\u00e9pertoire du projet
cd /d "%PROJECT_DIR%"
echo [%time%] R\u00e9pertoire: %PROJECT_DIR% >> "%LOG_FILE%"

REM V\u00e9rifier que l'environnement virtuel existe
if not exist "%VENV_PYTHON%" (
    echo [ERREUR] Environnement virtuel non trouv\u00e9: %VENV_PYTHON%
    echo [ERREUR] Environnement virtuel non trouv\u00e9: %VENV_PYTHON% >> "%LOG_FILE%"
    pause
    exit /b 1
)

REM V\u00e9rifier que le script existe
if not exist "%APP_SCRIPT%" (
    echo [ERREUR] Script non trouv\u00e9: %APP_SCRIPT%
    echo [ERREUR] Script non trouv\u00e9: %APP_SCRIPT% >> "%LOG_FILE%"
    pause
    exit /b 1
)

echo [%time%] Lancement de l'application... >> "%LOG_FILE%"
echo [%time%] Lancement de l'application...
echo [%time%] Logs: %LOG_FILE%
echo.
echo ========================================
echo   Application accessible sur:
echo   http://localhost:7860
echo ========================================
echo.
echo Appuyez sur Ctrl+C pour arr\u00eater l'application
echo.

REM Boucle infinie pour red\u00e9marrage automatique en cas de crash
:RESTART
echo [%time%] D\u00e9marrage de l'application... >> "%LOG_FILE%"

REM Lancer l'application avec logs
"%VENV_PYTHON%" "%APP_SCRIPT%" >> "%LOG_FILE%" 2>&1

REM Si l'application s'arr\u00eate
set EXIT_CODE=%ERRORLEVEL%
echo [%time%] Application arr\u00eat\u00e9e avec code: %EXIT_CODE% >> "%LOG_FILE%"

if %EXIT_CODE% EQU 0 (
    echo [%time%] Application arr\u00eat\u00e9e normalement >> "%LOG_FILE%"
    echo Application arr\u00eat\u00e9e normalement
    pause
    exit /b 0
) else (
    echo [ERREUR] Application crash\u00e9e avec code %EXIT_CODE% >> "%LOG_FILE%"
    echo [ERREUR] Application crash\u00e9e! Red\u00e9marrage dans 10 secondes...
    echo [%time%] Red\u00e9marrage automatique dans 10 secondes... >> "%LOG_FILE%"
    timeout /t 10 /nobreak
    goto RESTART
)
