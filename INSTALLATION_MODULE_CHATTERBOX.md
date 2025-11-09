# 🔧 GUIDE D'INSTALLATION - Module Chatterbox

## ✅ SOLUTION APPLIQUÉE

Le module **chatterbox** a été installé avec succès dans l'environnement virtuel.

---

## 📋 Commande Exécutée

```powershell
.\venv\Scripts\pip.exe install -e . --no-deps
```

Cette commande :
- ✅ Installe le package `chatterbox-tts` en mode éditable (`-e`)
- ✅ Évite les conflits de dépendances (`--no-deps`)
- ✅ Permet l'utilisation de `from chatterbox.tts import ChatterboxTTS`

---

## 🧪 Vérification

Pour vérifier que le module est bien installé :

```powershell
.\venv\Scripts\python.exe -c "from chatterbox.tts import ChatterboxTTS; print('✅ OK')"
```

Résultat attendu :
```
✅ OK
```

---

## 🚀 LANCER L'APPLICATION MAINTENANT

Tout est prêt ! Double-cliquez sur :
```
LANCER_INTERFACE_LONGUE_DUREE.bat
```

Ou en ligne de commande :
```powershell
.\venv\Scripts\python.exe gradio_tts_app.py
```

---

## ⚠️ Note sur les Dépendances

Il existe un conflit entre :
- **Gradio 5.44.1** (requiert typer >= 0.12)
- **Spacy 3.6.x** (requiert typer < 0.10.0)

L'installation avec `--no-deps` contourne ce conflit car toutes les autres dépendances nécessaires sont déjà installées.

---

## 🔍 Si l'Application Ne Démarre Toujours Pas

Vérifiez que tous les modules sont présents :

```powershell
.\venv\Scripts\python.exe -c "import numpy, torch, gradio, chatterbox.tts; print('✅ Tous les modules OK')"
```

---

## 📁 Fichiers Importants

- `pyproject.toml` - Configuration du package
- `src/chatterbox/` - Code source du module
- `venv/` - Environnement virtuel Python

---

**✅ Le module chatterbox est maintenant installé et prêt à l'emploi !**
