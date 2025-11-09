# Chatterbox TTS - Version Longue Durée
# Lanceur PowerShell

Write-Host "========================================" -ForegroundColor Cyan
Write-Host " Chatterbox TTS - Version Longue Duree" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Lancement de l'interface Gradio amelioree..." -ForegroundColor Green
Write-Host "- Support textes illimites (1-2h+)" -ForegroundColor Yellow
Write-Host "- Chargement de fichiers texte" -ForegroundColor Yellow
Write-Host "- Estimation automatique de duree" -ForegroundColor Yellow
Write-Host ""

# Aller dans le répertoire du script
Set-Location -Path $PSScriptRoot

# Vérifier si l'environnement virtuel existe
if (Test-Path "venv\Scripts\python.exe") {
    Write-Host "Utilisation de l'environnement virtuel..." -ForegroundColor Green
    & "venv\Scripts\python.exe" "gradio_tts_app.py"
} else {
    Write-Host "Environnement virtuel non trouve, utilisation de Python global..." -ForegroundColor Yellow
    python gradio_tts_app.py
}

Write-Host ""
Write-Host "Appuyez sur une touche pour continuer..." -ForegroundColor Cyan
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
