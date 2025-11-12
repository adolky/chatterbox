# ========================================
# SCRIPT DE MONITORING - CHATTERBOX TTS
# V\u00e9rifie que l'application tourne et la relance si n\u00e9cessaire
# ========================================

# Configuration
$projectDir = "c:\Users\adolk\Documents\Youtube ai audio\chatterbox"
$logDir = "$projectDir\logs"
$monitorLog = "$logDir\monitor.log"
$port = 7860
$checkInterval = 60  # V\u00e9rifier toutes les 60 secondes

# Cr\u00e9er le dossier de logs s'il n'existe pas
if (-not (Test-Path $logDir)) {
    New-Item -ItemType Directory -Path $logDir -Force | Out-Null
}

function Write-Log {
    param([string]$message)
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    $logMessage = "[$timestamp] $message"
    Add-Content -Path $monitorLog -Value $logMessage
    Write-Host $logMessage
}

function Test-ApplicationRunning {
    try {
        $response = Invoke-WebRequest -Uri "http://localhost:$port" -TimeoutSec 5 -UseBasicParsing
        return $true
    } catch {
        return $false
    }
}

function Get-ApplicationProcess {
    # Chercher le processus Python qui ex\u00e9cute gradio_tts_app.py
    return Get-Process python -ErrorAction SilentlyContinue | 
           Where-Object { $_.CommandLine -like "*gradio_tts_app.py*" }
}

function Start-Application {
    Write-Log "Tentative de d\u00e9marrage de l'application..."
    
    # Utiliser la t\u00e2che planifi\u00e9e si elle existe
    $task = Get-ScheduledTask -TaskName "ChatterboxTTS_AutoStart" -ErrorAction SilentlyContinue
    
    if ($task) {
        Write-Log "D\u00e9marrage via la t\u00e2che planifi\u00e9e..."
        Start-ScheduledTask -TaskName "ChatterboxTTS_AutoStart"
    } else {
        Write-Log "D\u00e9marrage via le script .bat..."
        $batFile = "$projectDir\DEMARRER_PRODUCTION.bat"
        if (Test-Path $batFile) {
            Start-Process -FilePath "cmd.exe" -ArgumentList "/c `"$batFile`"" -WorkingDirectory $projectDir
        } else {
            Write-Log "ERREUR: Fichier DEMARRER_PRODUCTION.bat non trouv\u00e9!"
        }
    }
    
    # Attendre 30 secondes pour que l'application d\u00e9marre
    Write-Log "Attente du d\u00e9marrage (30s)..."
    Start-Sleep -Seconds 30
}

function Stop-Application {
    Write-Log "Arr\u00eat de l'application..."
    $processes = Get-ApplicationProcess
    if ($processes) {
        $processes | ForEach-Object {
            Write-Log "Arr\u00eat du processus $($_.Id)..."
            Stop-Process -Id $_.Id -Force
        }
    }
    Start-Sleep -Seconds 5
}

# Fonction principale de monitoring
function Start-Monitoring {
    Write-Log "========================================="
    Write-Log "D\u00c9MARRAGE DU MONITORING CHATTERBOX TTS"
    Write-Log "========================================="
    Write-Log "Port: $port"
    Write-Log "Intervalle de v\u00e9rification: $checkInterval secondes"
    Write-Log "Appuyez sur Ctrl+C pour arr\u00eater"
    Write-Log ""
    
    $consecutiveFailures = 0
    $maxFailures = 3
    
    while ($true) {
        $isRunning = Test-ApplicationRunning
        
        if ($isRunning) {
            if ($consecutiveFailures -gt 0) {
                Write-Log "\u2705 Application r\u00e9tablie apr\u00e8s $consecutiveFailures \u00e9checs"
            }
            $consecutiveFailures = 0
            Write-Log "\u2705 Application en ligne (http://localhost:$port)"
        } else {
            $consecutiveFailures++
            Write-Log "\u26a0\ufe0f  Application non accessible! (\u00c9chec $consecutiveFailures/$maxFailures)"
            
            if ($consecutiveFailures -ge $maxFailures) {
                Write-Log "\u274c Application d\u00e9faillante apr\u00e8s $maxFailures tentatives"
                
                # Arr\u00eater les processus zombies
                Stop-Application
                
                # Red\u00e9marrer l'application
                Start-Application
                
                # R\u00e9initialiser le compteur
                $consecutiveFailures = 0
            }
        }
        
        # Attendre avant la prochaine v\u00e9rification
        Start-Sleep -Seconds $checkInterval
    }
}

# Gestion de l'arr\u00eat propre
try {
    Start-Monitoring
} catch [System.Management.Automation.PipelineStoppedException] {
    Write-Log ""
    Write-Log "Arr\u00eat du monitoring demand\u00e9 par l'utilisateur"
    Write-Log "========================================="
} catch {
    Write-Log "ERREUR: $_"
    Write-Log "========================================="
}
