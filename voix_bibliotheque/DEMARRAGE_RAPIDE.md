# 🎤 BIBLIOTHÈQUE DE VOIX - RÉSUMÉ ULTRA-RAPIDE

## ✨ Qu'est-ce que c'est ?

Un système pour **organiser et sélectionner vos voix** en 2 clics au lieu de taper des chemins longs.

---

## 🚀 Démarrage (2 minutes)

```powershell
# 1. Initialiser
cd "C:\Users\adolk\Documents\Youtube ai audio\chatterbox"
.\venv\Scripts\activate
python gestionnaire_voix.py --init

# 2. Ajouter votre voix (enregistrée 20-30s)
copy ma_voix.wav voix_bibliotheque\homme\

# 3. Utiliser
python generer_long_audio_interactive.py
# → Option 2 (Bibliothèque)
# → Sélectionnez votre voix
```

---

## 💡 Avantages

**Avant :**
```
Chemin : C:\Users\...\Documents\...\Enregistrements\...\ma_voix.wav
```

**Maintenant :**
```
Choisissez (1-3): 1
```

- ✅ **95% plus rapide**
- ✅ **Zéro erreur**
- ✅ **Organisation automatique**

---

## 📁 Structure

```
voix_bibliotheque/
├── homme/              # Voix masculines
│   └── ma_voix.wav
├── femme/              # Voix féminines
└── autres/             # Voix spéciales
```

---

## 🔧 Commandes

```powershell
# Lister
python gestionnaire_voix.py --liste

# Chercher
python gestionnaire_voix.py --chercher podcast

# Tester
python gestionnaire_voix.py --test ma_voix.wav
```

---

## 🎯 Utilisation

### Mode interactif (recommandé)

```powershell
python generer_long_audio_interactive.py
```

Menu :
```
🎤 CHOIX DE LA VOIX
1. Voix par défaut
2. Bibliothèque    ← Nouveau !
3. Chemin manuel

Choix: 2

🎤 BIBLIOTHÈQUE
1. ma_voix.wav

Choix: 1 ✅
```

### Ligne de commande

```powershell
python generer_long_audio_interactive.py ^
  --texte script.txt ^
  --voix voix_bibliotheque\homme\ma_voix.wav ^
  --ton podcast_dynamique
```

---

## 🎨 Combiner avec presets

**Parfait pour YouTube :**

```
Voix (bibliothèque) + Ton (preset) = Production en 5 min ! ⚡
```

**Exemple :**
1. Bibliothèque → `voix_podcast.wav`
2. Preset → `podcast_dynamique`
3. ✅ Génération automatique !

---

## 📚 Documentation

- **Guide complet :** `GUIDE_BIBLIOTHEQUE_VOIX.md` (15KB)
- **Résumé :** `BIBLIOTHEQUE_VOIX_RESUME.md` (10KB)
- **Voix par défaut :** `VOIX_PAR_DEFAUT.md` (8KB)

---

## 🎉 Résultat

**Workflow YouTube optimisé :**

```powershell
# Setup (une fois - 5 min)
python gestionnaire_voix.py --init
copy ma_voix.wav voix_bibliotheque\homme\

# Production (5 min par épisode)
python generer_long_audio_interactive.py
# → Bibliothèque → voix → preset → Générer !
```

**Système professionnel complet ! 🚀**

---

**Commencez maintenant :**
```powershell
python gestionnaire_voix.py --init
```
