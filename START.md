# ⚡ DÉMARRAGE IMMÉDIAT - BIBLIOTHÈQUE DE VOIX

## 🎯 3 commandes pour commencer

```powershell
# 1. Initialiser (30 secondes)
cd "C:\Users\adolk\Documents\Youtube ai audio\chatterbox"
.\venv\Scripts\activate
python gestionnaire_voix.py --init

# 2. Ajouter votre voix (2 minutes)
# Enregistrez 20-30s avec smartphone ou Audacity
copy ma_voix.wav voix_bibliotheque\homme\

# 3. Utiliser (5 minutes)
python generer_long_audio_interactive.py
# → Voix : Option 2 (Bibliothèque)
# → Ton : Option 4 (Podcast dynamique)
```

**Temps total : 8 minutes** ⚡

---

## 📝 Voix par défaut de Chatterbox

**Question :** Quelles sont les voix par défaut ?

**Réponse :** Chatterbox utilise une **voix synthétique neutre** générée automatiquement (zero-shot TTS). Il n'y a **pas de fichiers audio pré-enregistrés**.

**Caractéristiques :**
- 🤖 Voix neutre professionnelle
- 🌍 Fonctionne dans 23 langues
- ⚡ Immédiatement disponible
- 🎭 Modulable par presets

**Pour utiliser :**
```powershell
python generer_long_audio_interactive.py
# → Voix : Option 1 (Défaut)
```

**Pour personnaliser :**
```powershell
python generer_long_audio_interactive.py
# → Voix : Option 2 (Bibliothèque) ← Votre vraie voix !
```

---

## 🎤 3 options de voix

### Option 1 : Voix par défaut
- ✅ Aucun setup
- ✅ Tests rapides
- ⚠️ Voix synthétique (pas votre voix)

### Option 2 : Bibliothèque (NOUVEAU ⭐)
- ✅ Vos voix organisées
- ✅ Sélection en 2 clics
- ✅ Réutilisation facile

### Option 3 : Chemin manuel
- ✅ Fichier unique
- ⚠️ Chemin long à taper

**Recommandation YouTube : Option 2 (Bibliothèque)**

---

## 🚀 Commandes utiles

```powershell
# Voir vos voix
python gestionnaire_voix.py --liste

# Chercher une voix
python gestionnaire_voix.py --chercher podcast

# Tester une voix
python gestionnaire_voix.py --test ma_voix.wav

# Générer un podcast
python generer_long_audio_interactive.py
```

---

## 📚 Documentation

| Fichier | Pour quoi ? |
|---------|-------------|
| **SYSTEME_COMPLET.md** | Vue d'ensemble complète |
| **MEMO_RAPIDE.md** | Commandes essentielles |
| **GUIDE_BIBLIOTHEQUE_VOIX.md** | Guide détaillé bibliothèque |
| **VOIX_PAR_DEFAUT.md** | Explication voix par défaut |

---

## 🎉 Résultat

**Système complet de production podcasts YouTube :**

```
Voix (bibliothèque) + Ton (preset) = Podcast en 5 min ! 🚀
```

**Commencez maintenant :**
```powershell
python gestionnaire_voix.py --init
```
