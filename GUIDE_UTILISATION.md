# 🎙️ GUIDE D'UTILISATION - CHATTERBOX TTS

**Générateur de podcasts AI avec licence MIT pour monétisation YouTube**

---

## 📋 TABLE DES MATIÈRES

1. [Vue d'ensemble](#vue-densemble)
2. [Démarrage rapide](#démarrage-rapide)
3. [Modes d'utilisation](#modes-dutilisation)
4. [Fonctionnalités avancées](#fonctionnalités-avancées)
5. [Licence et monétisation](#licence-et-monétisation)
6. [Dépannage](#dépannage)

---

## 🎯 VUE D'ENSEMBLE

### Qu'est-ce que Chatterbox?

**Chatterbox** est un système de synthèse vocale (TTS) open source développé par **Resemble.AI**:

- ✅ **Licence MIT** - Utilisation commerciale autorisée
- 🌍 **23 langues supportées** (dont français)
- 🎭 **Contrôle émotionnel** (joie, tristesse, colère, etc.)
- 🎤 **Clonage vocal zero-shot**
- ⚡ **Latence ~200ms** - Temps réel possible
- 🔒 **Watermarking intégré** - Traçabilité

### Configuration matérielle

**Votre PC:**
- GPU: NVIDIA RTX 3060 Ti (8GB VRAM) ✅
- RAM: 32GB ✅
- CUDA: 12.9 ✅
- Modèle: 3.2GB sur disque

**Performances:**
- ~10 secondes de génération pour 100 caractères
- Qualité: 24kHz, mono, WAV

---

## 🚀 DÉMARRAGE RAPIDE

### Étape 1: Lancer l'environnement

Double-cliquez sur:
```
DEMARRER_ICI.bat
```

Cela active l'environnement virtuel Python avec toutes les dépendances.

### Étape 2: Premier test

Dans la console qui s'ouvre, tapez:
```bash
python test_chatterbox.py
```

Ce test génère un fichier audio de démonstration en français.

**Résultat attendu:**
```
✅ Audio généré: 9.12 secondes
💾 Fichier sauvegardé: test_chatterbox_fr.wav
```

---

## 🎬 MODES D'UTILISATION

### Mode 1: Génération interactive

**Pour quoi?** Créer des fichiers audio un par un de manière interactive.

**Comment?**
```bash
python generer_podcast.py
```

**Interface:**
```
📝 Entrez votre texte:
> Bonjour, bienvenue sur ma chaîne YouTube!

💾 Nom du fichier (ENTRÉE pour auto):
> intro_episode_01

✅ Audio généré: 5.23 secondes
💾 Fichier sauvegardé: podcasts_generes/intro_episode_01.wav
```

**Commandes spéciales:**
- `quit` - Quitter
- `help` - Afficher l'aide

**Fichiers générés:**
- Dossier: `podcasts_generes/`
- Format: WAV 24kHz mono
- Noms: auto ou personnalisés

---

### Mode 2: Génération par lot (batch)

**Pour quoi?** Traiter plusieurs segments d'un coup depuis un fichier texte.

**Comment?**

1. Créez un fichier texte `mon_script.txt`:
```
Bienvenue dans l'épisode cinq de notre podcast.
Aujourd'hui nous allons parler de l'intelligence artificielle.
La synthèse vocale a fait d'énormes progrès ces dernières années.
Merci de votre écoute et à bientôt!
```

2. Lancez le générateur:
```bash
python generer_batch.py
```

3. Indiquez le fichier:
```
📂 Chemin du fichier texte (ou 'exemple' pour créer un exemple):
> mon_script.txt

🏷️  Préfixe pour les fichiers (ENTRÉE pour 'segment'):
> episode05
```

**Résultat:**
```
podcasts_batch/
├── episode05_20250129_143022_001.wav
├── episode05_20250129_143022_002.wav
├── episode05_20250129_143022_003.wav
└── episode05_20250129_143022_004.wav
```

**Astuce:** Tapez `exemple` pour générer un fichier d'exemple automatiquement.

---

## 🎯 FONCTIONNALITÉS AVANCÉES

### Langues supportées

Chatterbox supporte **23 langues**:

**Européennes:**
- Français 🇫🇷
- Anglais 🇬🇧🇺🇸
- Espagnol 🇪🇸
- Allemand 🇩🇪
- Italien 🇮🇹
- Portugais 🇵🇹
- Russe 🇷🇺
- Polonais 🇵🇱
- Et plus...

**Asiatiques:**
- Chinois 🇨🇳
- Japonais 🇯🇵
- Coréen 🇰🇷
- Hindi 🇮🇳
- Et plus...

### Contrôle émotionnel

*(À implémenter selon l'API Chatterbox)*

```python
# Exemple théorique
wav = model.generate(texte, emotion="happy")
wav = model.generate(texte, emotion="sad")
wav = model.generate(texte, emotion="angry")
```

Émotions disponibles: neutral, happy, sad, angry, surprised, fearful

### Clonage vocal

Chatterbox permet le clonage de voix depuis un échantillon audio:

```python
# Charger un échantillon de voix
reference_audio = "ma_voix.wav"

# Générer avec cette voix
wav = model.generate(texte, reference_audio=reference_audio)
```

**Utilisation éthique:**
- ⚠️ Utilisez uniquement votre propre voix
- ⚠️ Obtenez le consentement pour d'autres voix
- ⚠️ Respectez les lois sur l'usurpation d'identité

---

## ⚖️ LICENCE ET MONÉTISATION

### Licence MIT - Que puis-je faire?

✅ **AUTORISÉ:**
- Utilisation commerciale (YouTube, podcasts, audiolivres)
- Modification du code
- Distribution du code
- Utilisation privée
- Monétisation des contenus générés

❌ **OBLIGATIONS:**
- Inclure la licence MIT dans les distributions du code
- Mentionner Resemble.AI (recommandé)

### Monétisation YouTube

**Chatterbox est compatible avec la monétisation YouTube:**

1. ✅ Licence MIT = usage commercial autorisé
2. ✅ Watermarking intégré = traçabilité
3. ✅ Pas de redevances ou royalties

**Dans vos descriptions YouTube:**
```
Audio généré avec Chatterbox TTS de Resemble.AI
https://github.com/resemble-ai/chatterbox
Licence: MIT
```

### Watermarking

Chatterbox inclut un système de watermarking invisible:
- 🔍 Permet d'identifier les audios générés
- 🛡️ Protection contre l'abus
- 🔒 Non-détectable à l'oreille

---

## 🔧 DÉPANNAGE

### Problème: "CUDA non disponible"

**Symptômes:**
```
⚠️  CUDA non disponible, utilisation du CPU
```

**Solutions:**
1. Vérifiez que votre GPU est bien une NVIDIA
2. Testez CUDA:
   ```bash
   python test_cuda.py
   ```
3. Réinstallez PyTorch avec CUDA:
   ```bash
   pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
   ```

---

### Problème: "No module named 'chatterbox'"

**Symptômes:**
```
ImportError: No module named 'chatterbox'
```

**Solutions:**
1. Vérifiez que vous utilisez bien `DEMARRER_ICI.bat`
2. Ou activez manuellement l'environnement:
   ```bash
   .\venv\Scripts\activate
   set PYTHONPATH=%CD%\src
   ```

---

### Problème: Audio de mauvaise qualité

**Solutions:**
1. Utilisez des phrases complètes avec ponctuation
2. Évitez les abréviations (écrivez "numéro" au lieu de "n°")
3. Séparez les longues phrases en plusieurs segments
4. Vérifiez que le texte est bien en français (pas de mixing langues)

---

### Problème: Génération trop lente

**Solutions:**
1. Vérifiez que CUDA est bien utilisé:
   ```python
   print(model.device)  # Doit afficher "cuda"
   ```
2. Fermez les autres applications gourmandes
3. Réduisez la longueur des segments (max 200 caractères)

---

### Problème: Erreur "Out of memory"

**Symptômes:**
```
RuntimeError: CUDA out of memory
```

**Solutions:**
1. Réduisez la longueur du texte (max 150 caractères par segment)
2. Redémarrez Python entre les générations longues
3. Libérez la VRAM:
   ```python
   torch.cuda.empty_cache()
   ```

---

## 📚 RESSOURCES

### Liens officiels

- **GitHub:** https://github.com/resemble-ai/chatterbox
- **Resemble.AI:** https://www.resemble.ai/
- **Documentation:** https://github.com/resemble-ai/chatterbox/blob/main/README.md

### Communauté

- **Issues GitHub:** https://github.com/resemble-ai/chatterbox/issues
- **Discussions:** https://github.com/resemble-ai/chatterbox/discussions

### Exemples d'utilisation

Voir les fichiers:
- `test_chatterbox.py` - Test basique
- `generer_podcast.py` - Mode interactif
- `generer_batch.py` - Traitement par lot
- `exemple_podcast.txt` - Fichier d'exemple

---

## 🎓 CONSEILS POUR YOUTUBE

### Structure d'un bon podcast

1. **Introduction** (10-15s)
   ```
   Bonjour et bienvenue sur [NOM CHAÎNE]! 
   Dans cette vidéo, nous allons voir [SUJET].
   ```

2. **Contenu principal** (segments de 30-60s)
   - Un segment par idée
   - Phrases courtes et claires
   - Transitions entre segments

3. **Conclusion** (10-15s)
   ```
   Si vous avez aimé cette vidéo, n'oubliez pas de liker et vous abonner.
   À très bientôt pour un nouveau contenu!
   ```

### Optimisation de la qualité

**DO:**
- ✅ Utilisez une ponctuation correcte
- ✅ Écrivez des phrases naturelles
- ✅ Faites des pauses (utilisez des points)
- ✅ Testez sur plusieurs segments courts

**DON'T:**
- ❌ Texte tout en majuscules
- ❌ Abréviations (sauf courantes: Dr., M., etc.)
- ❌ Nombres en chiffres (écrivez "vingt-trois" pas "23")
- ❌ URLs ou emails

### Post-production

Après génération, vous pouvez améliorer l'audio avec:
- **Audacity** (gratuit) - normalisation, équaliseur
- **Adobe Audition** - traitement pro
- **Reaper** - DAW complet

---

## ✅ CHECKLIST AVANT PUBLICATION YOUTUBE

- [ ] Audio généré avec qualité 24kHz
- [ ] Licence MIT mentionnée dans la description
- [ ] Watermarking présent (automatique)
- [ ] Pas de contenu protégé par copyright dans le texte
- [ ] Qualité audio vérifiée (pas de distorsion)
- [ ] Durée adaptée au format vidéo
- [ ] Pistes exportées en WAV ou MP3 320kbps

---

## 📞 SUPPORT

Pour toute question:

1. **Vérifiez d'abord cette documentation**
2. **Testez avec `test_chatterbox.py`**
3. **Consultez les issues GitHub** (problèmes connus)
4. **Créez une issue** (nouveau problème)

---

**Bon podcast! 🎙️**

*Généré avec ❤️ par Chatterbox - Resemble.AI*
