# 🔧 Dépannage - Erreur "ModuleNotFoundError: No module named 'numpy'"

## ❌ Le Problème

L'erreur `ModuleNotFoundError: No module named 'numpy'` signifie que le script essaie d'utiliser Python système au lieu de l'environnement virtuel où tous les modules sont installés.

---

## ✅ Solutions

### Solution 1 : Utiliser le Lanceur Corrigé (RECOMMANDÉ)

Le fichier `LANCER_INTERFACE_LONGUE_DUREE.bat` a été corrigé pour utiliser automatiquement l'environnement virtuel.

**Double-cliquez simplement sur** :
```
LANCER_INTERFACE_LONGUE_DUREE.bat
```

### Solution 2 : Utiliser le Lanceur PowerShell

Si le .bat ne fonctionne pas :

1. **Clic-droit** sur `LANCER_INTERFACE_LONGUE_DUREE.ps1`
2. **Sélectionnez** "Exécuter avec PowerShell"

### Solution 3 : Ligne de Commande Directe

Ouvrez PowerShell dans le dossier `chatterbox` et exécutez :

```powershell
.\venv\Scripts\python.exe gradio_tts_app.py
```

### Solution 4 : Activer l'Environnement Virtuel Manuellement

```powershell
cd "c:\Users\adolk\Documents\Youtube ai audio\chatterbox"
.\venv\Scripts\Activate.ps1
python gradio_tts_app.py
```

---

## 🧪 Vérifier que NumPy est Installé

Pour vérifier que NumPy est bien installé dans l'environnement virtuel :

```powershell
.\venv\Scripts\python.exe -c "import numpy; print('NumPy version:', numpy.__version__)"
```

Résultat attendu :
```
NumPy version: 1.25.2
```

---

## 📋 Autres Erreurs Possibles

### Erreur : "python n'est pas reconnu..."

**Cause** : Python n'est pas dans le PATH système

**Solution** : Utilisez toujours `.\venv\Scripts\python.exe` ou les lanceurs .bat/.ps1

### Erreur : "cannot be loaded because running scripts is disabled"

**Cause** : Politique d'exécution PowerShell restrictive

**Solution** :
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Puis relancez le script PowerShell.

### Erreur : Module 'gradio' ou 'torch' manquant

**Solution** : Installer les dépendances
```powershell
.\venv\Scripts\pip.exe install -r requirements.txt
```

---

## 🎯 Méthode Recommandée (La Plus Simple)

1. **Ouvrez** le dossier `chatterbox`
2. **Double-cliquez** sur `LANCER_INTERFACE_LONGUE_DUREE.bat`
3. **Attendez** que l'interface s'ouvre dans le navigateur

Si ça ne fonctionne toujours pas, utilisez la **Solution 3** ci-dessus.

---

## 📞 Si Rien Ne Fonctionne

Réinstallez les dépendances dans l'environnement virtuel :

```powershell
cd "c:\Users\adolk\Documents\Youtube ai audio\chatterbox"
.\venv\Scripts\Activate.ps1
pip install --upgrade numpy torch gradio
python gradio_tts_app.py
```

---

**✅ Après correction, l'application devrait démarrer sans erreur !**
