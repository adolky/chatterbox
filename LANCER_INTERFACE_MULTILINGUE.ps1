# Chatterbox TTS - Longue Duree v1.1
# Avec Support Multilingue (24 langues)
# Et Sauvegarde de Voix

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "  Chatterbox TTS - Longue Duree v1.1" -ForegroundColor Cyan
Write-Host "  Avec Support Multilingue (24 langues)" -ForegroundColor Cyan
Write-Host "  Et Sauvegarde de Voix" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Change to script directory
Set-Location -Path $PSScriptRoot

Write-Host "[1/3] Verification de l'environnement..." -ForegroundColor Yellow
if (!(Test-Path "venv\Scripts\python.exe")) {
    Write-Host "ERREUR: Environnement virtuel non trouve!" -ForegroundColor Red
    Write-Host "Veuillez executer l'installation d'abord." -ForegroundColor Red
    Read-Host "Appuyez sur Entree pour quitter"
    exit 1
}

Write-Host "[2/3] Verification du dossier de sauvegarde des voix..." -ForegroundColor Yellow
if (!(Test-Path "voix_sauvegardees")) {
    New-Item -ItemType Directory -Path "voix_sauvegardees" | Out-Null
    Write-Host "Dossier 'voix_sauvegardees' cree" -ForegroundColor Green
}

Write-Host "[3/3] Lancement de l'application..." -ForegroundColor Yellow
Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host " NOUVELLES FONCTIONNALITES v1.1 :" -ForegroundColor Green
Write-Host " - 24 langues supportees" -ForegroundColor White
Write-Host " - Sauvegarde et gestion de voix" -ForegroundColor White
Write-Host " - Interface amelioree" -ForegroundColor White
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "L'application va s'ouvrir dans votre navigateur..." -ForegroundColor Cyan
Write-Host "Pour arreter : Fermez cette fenetre ou appuyez sur Ctrl+C" -ForegroundColor Yellow
Write-Host ""

& "venv\Scripts\python.exe" gradio_tts_app.py

if ($LASTEXITCODE -ne 0) {
    Write-Host ""
    Write-Host "ERREUR lors du lancement!" -ForegroundColor Red
    Write-Host "Consultez GUIDE_UTILISATION.md pour l'aide" -ForegroundColor Yellow
    Read-Host "Appuyez sur Entree pour quitter"
}
