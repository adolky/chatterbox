# 🚀 CHATTERBOX TTS - MODE PRODUCTION

## 📋 Configuration Complète

Votre application Chatterbox TTS est maintenant configurée pour fonctionner en **mode production** avec :
- ✅ Démarrage automatique au redémarrage de Windows
- ✅ Redémarrage automatique en cas de crash
- ✅ Logs détaillés pour le debugging
- ✅ Monitoring continu (optionnel)
- ✅ **Accès depuis d'autres PC du réseau** 🌐

---

## 🎯 DÉMARRAGE RAPIDE

### 1️⃣ Configuration Initiale (À FAIRE UNE SEULE FOIS)

**Ouvrir PowerShell en tant qu'Administrateur :**
```
Clic droit sur le menu Démarrer → Windows PowerShell (admin)
```

**Exécuter les scripts de configuration :**
```powershell
cd "c:\Users\adolk\Documents\Youtube ai audio\chatterbox"
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned -Force

# 1. Configurer le démarrage automatique
.\CONFIGURER_DEMARRAGE_AUTO.ps1

# 2. Configurer le pare-feu pour l'accès réseau
.\CONFIGURER_PAREFEU.ps1
```

**Répondez "O" pour démarrer l'application immédiatement.**

✅ **C'est fait !** L'application démarrera automatiquement à chaque redémarrage et sera accessible depuis d'autres PC.

---

## 📁 FICHIERS DE PRODUCTION

### Scripts de Démarrage

| Fichier | Description | Usage |
|---------|-------------|-------|
| **DEMARRER_PRODUCTION.bat** | Script de démarrage principal | Double-clic pour lancer manuellement |
| **CONFIGURER_DEMARRAGE_AUTO.ps1** | Configure le démarrage automatique | Exécuter 1 seule fois en admin |
| **CONFIGURER_PAREFEU.ps1** | Configure l'accès réseau | Exécuter 1 seule fois en admin |
| **MONITORING.ps1** | Surveillance continue (optionnel) | Pour monitoring 24/7 |

### Logs

Tous les logs sont dans le dossier `logs/` :

```
logs/
├── app_20251111_190000.log        ← Logs de l'application
├── app_20251111_143022.log        ← Session précédente
└── monitor.log                     ← Logs du monitoring (si actif)
```

---

## 🔧 UTILISATION

### Démarrage Manuel

Double-cliquez sur : **`DEMARRER_PRODUCTION.bat`**

L'application :
- Démarre automatiquement
- Crée un fichier de log avec timestamp
- Se redémarre automatiquement en cas de crash
- S'ouvre dans votre navigateur sur http://localhost:7860

### Arrêt de l'Application

**Méthode 1 - Dans la fenêtre de commande :**
```
Ctrl + C
```

**Méthode 2 - Via le Gestionnaire des tâches :**
```
Ctrl + Shift + Esc → Chercher "python.exe" → Terminer la tâche
```

**Méthode 3 - Via PowerShell :**
```powershell
Stop-Process -Name python -Force
```

### Vérifier l'État

**Accès local (sur ce PC) :**
```
http://localhost:7860
```

**Accès depuis un autre PC du réseau :**
```
http://VOTRE_IP:7860
```

**Pour connaître votre IP :**
```powershell
ipconfig | Select-String "IPv4"
```

**Voir les logs en temps réel :**
```powershell
cd "c:\Users\adolk\Documents\Youtube ai audio\chatterbox\logs"
Get-Content -Path (Get-ChildItem | Sort-Object LastWriteTime -Descending | Select-Object -First 1).Name -Wait
```

---

## 🔄 GESTION DU DÉMARRAGE AUTOMATIQUE

### Vérifier la Tâche Planifiée

```powershell
Get-ScheduledTask -TaskName "ChatterboxTTS_AutoStart"
```

### Désactiver le Démarrage Automatique

```powershell
schtasks /Change /TN "ChatterboxTTS_AutoStart" /DISABLE
```

### Réactiver le Démarrage Automatique

```powershell
schtasks /Change /TN "ChatterboxTTS_AutoStart" /ENABLE
```

### Supprimer la Tâche Planifiée

```powershell
schtasks /Delete /TN "ChatterboxTTS_AutoStart" /F
```

### Lancer Manuellement la Tâche

```powershell
schtasks /Run /TN "ChatterboxTTS_AutoStart"
```

---

## 📊 MONITORING (OPTIONNEL)

Pour une surveillance continue 24/7 avec redémarrage automatique :

### Démarrer le Monitoring

```powershell
cd "c:\Users\adolk\Documents\Youtube ai audio\chatterbox"
.\MONITORING.ps1
```

**Fonctionnalités :**
- ✅ Vérifie que l'application répond toutes les 60 secondes
- ✅ Redémarre automatiquement après 3 échecs consécutifs
- ✅ Logs toutes les actions dans `logs/monitor.log`

**Pour arrêter le monitoring :**
```
Ctrl + C
```

### Monitoring en Arrière-Plan (Windows Service)

Pour un monitoring permanent même après déconnexion :

```powershell
# Créer une tâche planifiée pour le monitoring
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-File `"c:\Users\adolk\Documents\Youtube ai audio\chatterbox\MONITORING.ps1`""
$trigger = New-ScheduledTaskTrigger -AtStartup
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -ExecutionTimeLimit (New-TimeSpan -Days 0)
Register-ScheduledTask -TaskName "ChatterboxTTS_Monitor" -Action $action -Trigger $trigger -Settings $settings -RunLevel Highest
```

---

## 📝 LOGS ET DEBUGGING

### Structure des Logs

Chaque session crée un nouveau fichier de log :

```
[2025-11-11 19:00:00] INFO __main__: CHATTERBOX TTS - MODE PRODUCTION
[2025-11-11 19:00:02] INFO __main__: Démarrage de l'interface Gradio...
[2025-11-11 19:00:02] INFO __main__: Device: cuda
[2025-11-11 19:00:05] INFO __main__: Modèle chargé avec succès sur cuda
[2025-11-11 19:05:12] INFO __main__: Nouvelle génération - Langue: fr, Longueur texte: 2847 caractères
[2025-11-11 19:05:13] INFO __main__: Texte divisé en 12 batches (2847 caractères)
[2025-11-11 19:23:45] INFO __main__: Génération terminée - 12 batches, 215.32s audio, 18.52min
```

### Consulter les Logs

**Dernier fichier de log :**
```powershell
cd "c:\Users\adolk\Documents\Youtube ai audio\chatterbox\logs"
Get-Content (Get-ChildItem | Sort-Object LastWriteTime -Descending | Select-Object -First 1).Name
```

**Suivre en temps réel :**
```powershell
Get-Content -Path (Get-ChildItem | Sort-Object LastWriteTime -Descending | Select-Object -First 1).Name -Wait
```

**Rechercher des erreurs :**
```powershell
Get-ChildItem *.log | Select-String "ERROR" -Context 2
```

### Rotation des Logs

Les logs s'accumulent avec le temps. Pour nettoyer :

**Supprimer les logs de plus de 30 jours :**
```powershell
cd "c:\Users\adolk\Documents\Youtube ai audio\chatterbox\logs"
Get-ChildItem *.log | Where-Object {$_.LastWriteTime -lt (Get-Date).AddDays(-30)} | Remove-Item
```

**Voir l'espace utilisé :**
```powershell
Get-ChildItem *.log | Measure-Object -Property Length -Sum | Select-Object @{Name="TailleMB";Expression={[math]::Round($_.Sum/1MB,2)}}
```

---

## 🛠️ DÉPANNAGE

### L'application ne démarre pas

**1. Vérifier les logs :**
```powershell
cd "c:\Users\adolk\Documents\Youtube ai audio\chatterbox\logs"
Get-Content (Get-ChildItem | Sort-Object LastWriteTime -Descending | Select-Object -First 1).Name | Select-Object -Last 50
```

**2. Vérifier l'environnement virtuel :**
```powershell
Test-Path "c:\Users\adolk\Documents\Youtube ai audio\chatterbox\venv\Scripts\python.exe"
```

**3. Tester manuellement :**
```powershell
cd "c:\Users\adolk\Documents\Youtube ai audio\chatterbox"
.\venv\Scripts\Activate.ps1
python gradio_tts_app.py
```

### Le port 7860 est déjà utilisé

**Trouver quel processus utilise le port :**
```powershell
netstat -ano | findstr :7860
```

**Tuer le processus :**
```powershell
# Remplacer PID par l'ID du processus
Stop-Process -Id PID -Force
```

### L'application crash sans arrêt

**1. Vérifier les erreurs dans les logs**

**2. Augmenter le délai de redémarrage dans DEMARRER_PRODUCTION.bat :**
```batch
timeout /t 30 /nobreak  # Au lieu de 10 secondes
```

**3. Vérifier la mémoire GPU :**
```powershell
nvidia-smi
```

### La tâche planifiée ne fonctionne pas

**Vérifier l'état :**
```powershell
Get-ScheduledTask -TaskName "ChatterboxTTS_AutoStart" | Select-Object State, LastRunTime, NextRunTime
```

**Voir les logs de la tâche :**
```
Gestionnaire des tâches → Bibliothèque du planificateur de tâches → ChatterboxTTS_AutoStart → Historique
```

**Recréer la tâche :**
```powershell
.\CONFIGURER_DEMARRAGE_AUTO.ps1
```

---

## ⚙️ PARAMÈTRES DE PRODUCTION

### Performances

Dans `gradio_tts_app.py`, les paramètres actuels sont :

```python
# Tokens dynamiques pour qualité optimale
max_tokens = 650  # Texte complet garanti

# Cleanup GPU optimisé
BATCHES_PER_GROUP = 8  # Nettoyage tous les 8 batches

# Queue Gradio
max_size = 50  # 50 générations en attente max
default_concurrency_limit = 1  # 1 génération à la fois
```

### Sécurité

L'application est accessible depuis :
- ✅ Localhost : http://localhost:7860
- ✅ Réseau local : http://VOTRE_IP:7860
- ✅ Internet (Gradio share) : URL temporaire générée

**Pour désactiver l'accès Internet :**

Modifier dans `gradio_tts_app.py` :
```python
demo.queue(max_size=50, default_concurrency_limit=1).launch(
    share=False,  # ← Changer True en False
    server_name="127.0.0.1",  # ← Seulement localhost
    server_port=7860, 
    inbrowser=True
)
```

---

## 📊 STATISTIQUES DE PRODUCTION

### Voir l'Uptime

```powershell
# Temps depuis le dernier démarrage de l'application
$logFile = Get-ChildItem "c:\Users\adolk\Documents\Youtube ai audio\chatterbox\logs\app_*.log" | Sort-Object LastWriteTime -Descending | Select-Object -First 1
$startTime = (Get-Content $logFile.FullName | Select-Object -First 20 | Select-String "CHATTERBOX TTS - MODE PRODUCTION" | ForEach-Object { $_ -replace '\[|\].*', '' })[0]
$uptime = (Get-Date) - [datetime]$startTime
Write-Host "Uptime: $($uptime.Days) jours, $($uptime.Hours) heures, $($uptime.Minutes) minutes"
```

### Nombre de Générations

```powershell
# Compter les générations dans les logs
Get-ChildItem "c:\Users\adolk\Documents\Youtube ai audio\chatterbox\logs\app_*.log" | Select-String "Nouvelle génération" | Measure-Object | Select-Object -ExpandProperty Count
```

---

## 🎉 CHECKLIST DE PRODUCTION

Avant de mettre en production, vérifiez :

- [ ] ✅ Script DEMARRER_PRODUCTION.bat fonctionne
- [ ] ✅ Tâche planifiée créée et active
- [ ] ✅ Application démarre au redémarrage du PC
- [ ] ✅ Logs créés dans le dossier `logs/`
- [ ] ✅ Application accessible sur http://localhost:7860
- [ ] ✅ Génération test réussie
- [ ] ✅ Redémarrage automatique en cas de crash testé
- [ ] ✅ Monitoring optionnel configuré (si désiré)

---

## 📞 COMMANDES UTILES

### Redémarrage Rapide

```powershell
# Arrêter
Stop-Process -Name python -Force

# Démarrer
cd "c:\Users\adolk\Documents\Youtube ai audio\chatterbox"
.\DEMARRER_PRODUCTION.bat
```

### Nettoyage Complet

```powershell
# Arrêter l'application
Stop-Process -Name python -Force

# Nettoyer les logs de plus de 7 jours
cd "c:\Users\adolk\Documents\Youtube ai audio\chatterbox\logs"
Get-ChildItem *.log | Where-Object {$_.LastWriteTime -lt (Get-Date).AddDays(-7)} | Remove-Item

# Nettoyer le cache GPU
python -c "import torch; torch.cuda.empty_cache()"
```

### État du Système

```powershell
# Vérifier GPU
nvidia-smi

# Vérifier processus Python
Get-Process python -ErrorAction SilentlyContinue

# Vérifier port 7860
netstat -ano | findstr :7860

# Vérifier tâche planifiée
Get-ScheduledTask -TaskName "ChatterboxTTS_AutoStart"
```

---

## 📖 DOCUMENTATION

Pour plus d'informations :
- **Guide utilisateur** : `GUIDE_FINAL.md`
- **README original** : `README.md`
- **Logs détaillés** : `logs/`

---

**Version Production - 11 novembre 2025**  
**Configuration automatique réussie** ✅

L'application est maintenant prête pour fonctionner 24/7 en mode production ! 🚀
