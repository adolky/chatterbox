@echo off
echo ============================================
echo  Test Rapide - Environnement Chatterbox
echo ============================================
echo.

cd /d "%~dp0"

echo [1/5] Verification de l'environnement virtuel...
if exist "venv\Scripts\python.exe" (
    echo   [OK] Environnement virtuel trouve
) else (
    echo   [ERREUR] Environnement virtuel non trouve
    goto :error
)

echo.
echo [2/5] Test d'import de NumPy...
venv\Scripts\python.exe -c "import numpy; print('  [OK] NumPy version:', numpy.__version__)" 2>nul
if errorlevel 1 (
    echo   [ERREUR] NumPy non disponible
    goto :error
)

echo.
echo [2b/5] Test d'import du module Chatterbox...
venv\Scripts\python.exe -c "from chatterbox.tts import ChatterboxTTS; print('  [OK] Module chatterbox disponible')" 2>nul
if errorlevel 1 (
    echo   [ERREUR] Module chatterbox non disponible
    echo   Solution: Executez: venv\Scripts\pip.exe install -e . --no-deps
    goto :error
)

echo.
echo [3/5] Test d'import de PyTorch...
venv\Scripts\python.exe -c "import torch; print('  [OK] PyTorch version:', torch.__version__)" 2>nul
if errorlevel 1 (
    echo   [ERREUR] PyTorch non disponible
    goto :error
)

echo.
echo [4/5] Test d'import de Gradio...
venv\Scripts\python.exe -c "import gradio; print('  [OK] Gradio version:', gradio.__version__)" 2>nul
if errorlevel 1 (
    echo   [ERREUR] Gradio non disponible
    goto :error
)

echo.
echo [5/5] Test de syntaxe de gradio_tts_app.py...
venv\Scripts\python.exe -m py_compile gradio_tts_app.py 2>nul
if errorlevel 1 (
    echo   [ERREUR] Erreur de syntaxe dans gradio_tts_app.py
    goto :error
) else (
    echo   [OK] Pas d'erreur de syntaxe
)

echo.
echo ============================================
echo  TOUS LES TESTS SONT PASSES !
echo ============================================
echo.
echo Vous pouvez maintenant lancer l'application :
echo   - Double-clic sur LANCER_INTERFACE_LONGUE_DUREE.bat
echo   - Ou utilisez : venv\Scripts\python.exe gradio_tts_app.py
echo.
pause
exit /b 0

:error
echo.
echo ============================================
echo  ERREUR DETECTEE !
echo ============================================
echo.
echo Consultez le fichier DEPANNAGE_ERREUR_NUMPY.md
echo pour les solutions.
echo.
pause
exit /b 1
