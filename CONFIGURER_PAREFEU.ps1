# ========================================
# CONFIGURATION PARE-FEU WINDOWS
# Permet l'accès à Chatterbox TTS depuis d'autres PC
# ========================================

# Vérifier les privilèges administrateur
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
$isAdmin = $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

if (-not $isAdmin) {
    Write-Host "ERREUR: Ce script doit être exécuté en tant qu'Administrateur!" -ForegroundColor Red
    Write-Host "Faites un clic droit sur ce fichier et sélectionnez 'Exécuter en tant qu'administrateur'" -ForegroundColor Yellow
    pause
    exit 1
}

Write-Host "========================================" -ForegroundColor Green
Write-Host "CONFIGURATION PARE-FEU WINDOWS" -ForegroundColor Green
Write-Host "Chatterbox TTS - Accès Réseau" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

$ruleName = "Chatterbox TTS"
$port = 7860

# Vérifier si la règle existe déjà
Write-Host "[1/3] Vérification des règles existantes..." -ForegroundColor Cyan
$existingRule = Get-NetFirewallRule -DisplayName $ruleName -ErrorAction SilentlyContinue

if ($existingRule) {
    Write-Host "      Une règle existe déjà. Suppression..." -ForegroundColor Yellow
    Remove-NetFirewallRule -DisplayName $ruleName
}

Write-Host "[2/3] Création de la règle de pare-feu..." -ForegroundColor Cyan

try {
    # Créer la règle pour le trafic entrant (TCP)
    New-NetFirewallRule `
        -DisplayName $ruleName `
        -Direction Inbound `
        -Protocol TCP `
        -LocalPort $port `
        -Action Allow `
        -Profile Domain,Private,Public `
        -Description "Permet l'accès à Chatterbox TTS depuis d'autres ordinateurs du réseau" `
        -ErrorAction Stop | Out-Null
    
    Write-Host "      Règle créée avec succès!" -ForegroundColor Green
} catch {
    Write-Host "ERREUR lors de la création de la règle: $_" -ForegroundColor Red
    pause
    exit 1
}

Write-Host "[3/3] Vérification de la configuration..." -ForegroundColor Cyan

# Obtenir l'adresse IP locale
$localIP = (Get-NetIPAddress -AddressFamily IPv4 | Where-Object {$_.InterfaceAlias -notlike "*Loopback*" -and $_.IPAddress -notlike "169.254.*"}).IPAddress | Select-Object -First 1

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "CONFIGURATION TERMINÉE!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Détails de la configuration:" -ForegroundColor Cyan
Write-Host "  - Règle de pare-feu: $ruleName"
Write-Host "  - Port autorisé: $port (TCP)"
Write-Host "  - Profils: Domaine, Privé, Public"
Write-Host "  - Direction: Entrant (Inbound)"
Write-Host "  - Action: Autoriser"
Write-Host ""
Write-Host "📡 ACCÈS À L'APPLICATION:" -ForegroundColor Yellow
Write-Host ""
Write-Host "  Sur ce PC:" -ForegroundColor Cyan
Write-Host "    http://localhost:$port"
Write-Host ""
Write-Host "  Depuis un autre PC du réseau:" -ForegroundColor Cyan
Write-Host "    http://${localIP}:$port"
Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "INSTRUCTIONS POUR LES AUTRES PC:" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. Assurez-vous que l'application est lancée sur ce PC"
Write-Host "2. Sur l'autre PC, ouvrez un navigateur web"
Write-Host "3. Entrez l'adresse: http://${localIP}:$port"
Write-Host "4. L'interface Chatterbox TTS devrait s'afficher"
Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "NOTES IMPORTANTES:" -ForegroundColor Yellow
Write-Host ""
Write-Host "• Les deux PC doivent être sur le même réseau local"
Write-Host "• L'adresse IP peut changer si vous redémarrez votre PC"
Write-Host "• Pour vérifier votre IP actuelle: ipconfig"
Write-Host "• Pour désactiver: Désactivez la règle '$ruleName' dans le pare-feu"
Write-Host ""
Write-Host "COMMANDES UTILES:" -ForegroundColor Cyan
Write-Host ""
Write-Host "  Voir la règle:"
Write-Host "    Get-NetFirewallRule -DisplayName '$ruleName'"
Write-Host ""
Write-Host "  Désactiver la règle:"
Write-Host "    Disable-NetFirewallRule -DisplayName '$ruleName'"
Write-Host ""
Write-Host "  Réactiver la règle:"
Write-Host "    Enable-NetFirewallRule -DisplayName '$ruleName'"
Write-Host ""
Write-Host "  Supprimer la règle:"
Write-Host "    Remove-NetFirewallRule -DisplayName '$ruleName'"
Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host ""

# Test de connectivité
Write-Host "Test de connectivité sur le port $port..." -ForegroundColor Cyan
$listener = $null
try {
    $listener = [System.Net.Sockets.TcpListener]::new([System.Net.IPAddress]::Any, $port)
    $listener.Start()
    Write-Host "✅ Le port $port est disponible et prêt" -ForegroundColor Green
    $listener.Stop()
} catch {
    Write-Host "⚠️  Le port $port est peut-être déjà utilisé (c'est normal si l'application tourne)" -ForegroundColor Yellow
    if ($listener) { $listener.Stop() }
}

Write-Host ""
Write-Host "Configuration terminée! Vous pouvez maintenant accéder" -ForegroundColor Green
Write-Host "à Chatterbox TTS depuis d'autres PC du réseau." -ForegroundColor Green
Write-Host ""
pause
