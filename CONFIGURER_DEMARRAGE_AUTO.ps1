# ========================================
# SCRIPT POWERSHELL - CR\u00c9ER T\u00c2CHE PLANIFI\u00c9E WINDOWS
# Configure Chatterbox TTS pour d\u00e9marrer automatiquement
# ========================================

# V\u00e9rifier les privil\u00e8ges administrateur
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
$isAdmin = $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "ERREUR: Ce script doit \u00eatre ex\u00e9cut\u00e9 en tant qu'Administrateur!" -ForegroundColor Red
    Write-Host "Faites un clic droit sur ce fichier et s\u00e9lectionnez 'Ex\u00e9cuter en tant qu'administrateur'" -ForegroundColor Yellow
    pause
    exit 1
}

Write-Host "========================================" -ForegroundColor Green
Write-Host "CONFIGURATION D\u00c9MARRAGE AUTOMATIQUE" -ForegroundColor Green
Write-Host "Chatterbox TTS - Mode Production" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

# Param\u00e8tres
$taskName = "ChatterboxTTS_AutoStart"
$projectDir = "c:\Users\adolk\Documents\Youtube ai audio\chatterbox"
$batFile = "$projectDir\DEMARRER_PRODUCTION.bat"
$userName = $env:USERNAME

# V\u00e9rifier que le fichier .bat existe
if (-not (Test-Path $batFile)) {
    Write-Host "ERREUR: Fichier non trouv\u00e9: $batFile" -ForegroundColor Red
    pause
    exit 1
}

Write-Host "[1/4] V\u00e9rification des fichiers... OK" -ForegroundColor Cyan

# Supprimer la t\u00e2che existante si elle existe
$existingTask = Get-ScheduledTask -TaskName $taskName -ErrorAction SilentlyContinue
if ($existingTask) {
    Write-Host "[2/4] Suppression de la t\u00e2che existante..." -ForegroundColor Yellow
    Unregister-ScheduledTask -TaskName $taskName -Confirm:$false
}

Write-Host "[2/4] Pr\u00e9paration de la t\u00e2che planifi\u00e9e..." -ForegroundColor Cyan

# Cr\u00e9er l'action (lancer le .bat)
$action = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c `"$batFile`"" -WorkingDirectory $projectDir

# Cr\u00e9er le d\u00e9clencheur (au d\u00e9marrage de Windows, avec d\u00e9lai de 30s)
$trigger = New-ScheduledTaskTrigger -AtStartup
$trigger.Delay = "PT30S"  # D\u00e9lai de 30 secondes apr\u00e8s le d\u00e9marrage

# Param\u00e8tres de la t\u00e2che
$settings = New-ScheduledTaskSettingsSet `
    -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries `
    -StartWhenAvailable `
    -RestartCount 3 `
    -RestartInterval (New-TimeSpan -Minutes 1) `
    -ExecutionTimeLimit (New-TimeSpan -Days 0)  # Pas de limite de temps

# Cr\u00e9er le principal (utilisateur actuel)
$principal = New-ScheduledTaskPrincipal -UserId $userName -LogonType Interactive -RunLevel Highest

Write-Host "[3/4] Cr\u00e9ation de la t\u00e2che planifi\u00e9e..." -ForegroundColor Cyan

# Enregistrer la t\u00e2che
try {
    Register-ScheduledTask `
        -TaskName $taskName `
        -Action $action `
        -Trigger $trigger `
        -Settings $settings `
        -Principal $principal `
        -Description "Lance automatiquement Chatterbox TTS au d\u00e9marrage de Windows (mode production)" `
        -ErrorAction Stop | Out-Null
    
    Write-Host "[4/4] T\u00e2che planifi\u00e9e cr\u00e9\u00e9e avec succ\u00e8s!" -ForegroundColor Green
} catch {
    Write-Host "ERREUR lors de la cr\u00e9ation de la t\u00e2che: $_" -ForegroundColor Red
    pause
    exit 1
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "CONFIGURATION TERMIN\u00c9E!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "D\u00e9tails de la configuration:" -ForegroundColor Cyan
Write-Host "  - Nom de la t\u00e2che: $taskName"
Write-Host "  - D\u00e9clencheur: Au d\u00e9marrage de Windows (+30s)"
Write-Host "  - Script: $batFile"
Write-Host "  - Utilisateur: $userName"
Write-Host "  - Red\u00e9marrage auto: Oui (3 tentatives max)"
Write-Host "  - Interface: http://localhost:7860"
Write-Host ""
Write-Host "OPTIONS DISPONIBLES:" -ForegroundColor Yellow
Write-Host "  1. D\u00e9sactiver: schtasks /Change /TN `"$taskName`" /DISABLE"
Write-Host "  2. R\u00e9activer: schtasks /Change /TN `"$taskName`" /ENABLE"
Write-Host "  3. Supprimer: schtasks /Delete /TN `"$taskName`" /F"
Write-Host "  4. Lancer maintenant: schtasks /Run /TN `"$taskName`""
Write-Host ""

# Demander si on veut d\u00e9marrer maintenant
$response = Read-Host "Voulez-vous d\u00e9marrer l'application maintenant? (O/N)"
if ($response -eq "O" -or $response -eq "o") {
    Write-Host ""
    Write-Host "Lancement de l'application..." -ForegroundColor Cyan
    Start-ScheduledTask -TaskName $taskName
    Write-Host "Application lanc\u00e9e! V\u00e9rifiez http://localhost:7860" -ForegroundColor Green
}

Write-Host ""
Write-Host "L'application se lancera automatiquement au prochain red\u00e9marrage!" -ForegroundColor Green
pause
