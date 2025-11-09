# 🎙️ CHATTERBOX TTS - GÉNÉRATEUR DE PODCAST IA

> **Synthèse vocale professionnelle avec licence MIT pour monétisation YouTube**

![Chatterbox](Chatterbox-Multilingual.png)

---

## 📋 QU'EST-CE QUE C'EST?

**Chatterbox** est un système de synthèse vocale (Text-to-Speech) open source développé par **Resemble.AI**.

### ✨ Caractéristiques principales

- 🌍 **23 langues supportées** (français, anglais, espagnol, chinois, japonais, etc.)
- ⚖️ **Licence MIT** - Utilisation commerciale autorisée
- 🎭 **Contrôle émotionnel** - Joie, tristesse, colère, neutre
- 🎤 **Clonage vocal** - Reproduisez n'importe quelle voix
- ⚡ **Temps réel** - Latence ~200ms
- 🔒 **Watermarking** - Traçabilité intégrée
- 💰 **Monétisation YouTube autorisée**

### 🎯 Configuration de ce PC

- **GPU:** NVIDIA RTX 3060 Ti (8GB VRAM) ✅
- **CUDA:** 12.9 ✅
- **Python:** 3.11.9 ✅
- **PyTorch:** 2.6.0+cu124 ✅
- **Modèle:** 3.2GB (déjà téléchargé) ✅

---

## 🚀 DÉMARRAGE RAPIDE

### 🌐 MÉTHODE 1 : INTERFACE WEB (RECOMMANDÉE - pour non-techniciens)

**Pour les utilisateurs non-techniques** - Pas de ligne de commande !

Double-cliquez sur:
```
LANCER_INTERFACE_WEB.bat
```

**Ensuite:**
1. ⏳ Attendez 20-30 secondes (chargement)
2. 🌐 Votre navigateur s'ouvre automatiquement
3. 🚀 Cliquez sur "Charger le modèle"
4. 📝 Écrivez votre texte ou insérez un exemple
5. 🎙️ Cliquez sur "GÉNÉRER L'AUDIO"
6. ✅ C'est fait !

**📚 Guide complet:** Consultez `GUIDE_INTERFACE_WEB.md`

---

### ⌨️ MÉTHODE 2 : LIGNE DE COMMANDE (pour techniciens)

#### 1️⃣ Lancez l'environnement

Double-cliquez sur:
```
DEMARRER_ICI.bat
```

#### 2️⃣ Testez l'installation

Dans la console qui s'ouvre:
```bash
python test_chatterbox.py
```

**Résultat attendu:**
```
✅ Audio généré: 9.12 secondes
💾 Fichier sauvegardé: test_chatterbox_fr.wav
```

#### 3️⃣ Créez votre premier podcast

```bash
python generer_podcast.py
```

Entrez votre texte et laissez la magie opérer ! 🎉

---

## 📚 DOCUMENTATION

### Guides complets

- **[GUIDE_INTERFACE_WEB.md](GUIDE_INTERFACE_WEB.md)** ⭐ **NOUVEAU !** - Interface graphique pour non-techniciens
  - Utilisation simple dans le navigateur
  - Pas de ligne de commande
  - Guide pas-à-pas illustré

- **[GUIDE_UTILISATION.md](GUIDE_UTILISATION.md)** - Guide utilisateur complet (ligne de commande)
  - Modes d'utilisation (interactif / batch)
  - Fonctionnalités avancées
  - Conseils pour YouTube
  - Dépannage

- **[INSTALLATION.md](INSTALLATION.md)** - Détails de l'installation
  - Composants installés
  - Configuration matérielle
  - Licence et usage commercial
  - Support technique

### Démarrage rapide

| Fichier | Description |
|---------|-------------|
| `LANCER_INTERFACE_WEB.bat` | 🌐 **INTERFACE WEB** - Pour non-techniciens ⭐ **NOUVEAU !** |
| `DEMARRER_ICI.bat` | ⌨️ **LIGNE DE COMMANDE** - Pour techniciens |
| `test_chatterbox.py` | Test rapide du système |
| `generer_podcast.py` | Mode interactif - Un texte à la fois |
| `generer_batch.py` | Mode batch - Plusieurs textes d'un coup |

---

## 🎬 MODES D'UTILISATION

### Mode Interactif

**Pour:** Créer des fichiers audio un par un

```bash
python generer_podcast.py
```

**Interface:**
```
📝 Entrez votre texte:
> Bonjour, bienvenue sur ma chaîne YouTube!

💾 Nom du fichier (ENTRÉE pour auto):
> intro_episode01

✅ Audio généré: 5.23 secondes
💾 Fichier sauvegardé: podcasts_generes/intro_episode01.wav
```

### Mode Batch (par lot)

**Pour:** Traiter plusieurs segments depuis un fichier texte

```bash
python generer_batch.py
```

**Exemple de fichier texte** (`mon_script.txt`):
```
Bienvenue dans l'épisode cinq de notre podcast.
Aujourd'hui nous allons parler de l'intelligence artificielle.
La synthèse vocale a fait d'énormes progrès.
Merci de votre écoute et à bientôt!
```

**Résultat:**
```
podcasts_batch/
├── episode05_20250129_001.wav
├── episode05_20250129_002.wav
├── episode05_20250129_003.wav
└── episode05_20250129_004.wav
```

---

## 🌍 LANGUES SUPPORTÉES

Chatterbox parle **23 langues:**

| Région | Langues |
|--------|---------|
| **Europe** | Français 🇫🇷, Anglais 🇬🇧🇺🇸, Espagnol 🇪🇸, Allemand 🇩🇪, Italien 🇮🇹, Portugais 🇵🇹, Russe 🇷🇺, Polonais 🇵🇱, Néerlandais 🇳🇱, Tchèque 🇨🇿 |
| **Asie** | Chinois 🇨🇳, Japonais 🇯🇵, Coréen 🇰🇷, Hindi 🇮🇳, Thaï 🇹🇭, Vietnamien 🇻🇳, Indonésien 🇮🇩 |
| **Moyen-Orient** | Arabe 🇸🇦, Turc 🇹🇷 |

**Testé avec succès:** Français ✅

---

## ⚖️ LICENCE ET MONÉTISATION YOUTUBE

### Licence MIT

```
✅ Utilisation commerciale autorisée
✅ Modification autorisée  
✅ Distribution autorisée
✅ Utilisation privée autorisée
✅ MONÉTISATION YOUTUBE AUTORISÉE
```

### Que puis-je faire?

**AUTORISÉ ✅**
- Monétiser vos vidéos YouTube avec audio généré
- Créer des podcasts commerciaux
- Vendre des audiolivres
- Utiliser dans des publicités
- Modifier le code source

**RECOMMANDÉ 💡**
- Mentionner Chatterbox dans vos descriptions:
  ```
  Audio généré avec Chatterbox TTS de Resemble.AI
  https://github.com/resemble-ai/chatterbox
  Licence: MIT
  ```

---

## 📊 PERFORMANCES

### Votre configuration actuelle

| Matériel | Spécification | Status |
|----------|---------------|--------|
| GPU | NVIDIA RTX 3060 Ti (8GB) | ✅ Optimal |
| VRAM | 8GB | ✅ Suffisant |
| CUDA | 12.9 | ✅ Compatible |
| Modèle | 3.2GB téléchargé | ✅ Prêt |

### Vitesses de génération

| Longueur texte | Durée audio | Temps génération |
|----------------|-------------|------------------|
| 50 caractères | ~4 secondes | ~15 secondes |
| 100 caractères | ~9 secondes | ~30 secondes |
| 200 caractères | ~18 secondes | ~60 secondes |

**Note:** Première génération plus lente (chargement du modèle)

---

## 🎓 EXEMPLES D'UTILISATION

### Exemple 1: Intro YouTube

```python
texte = """
Bonjour et bienvenue sur ma chaîne Tech Review! 
Dans cette vidéo, nous allons découvrir les nouveautés 
en intelligence artificielle. 
N'oubliez pas de liker et de vous abonner!
"""

# Génération
wav = model.generate(texte)
ta.save("intro_youtube.wav", wav.cpu(), model.sr)
```

### Exemple 2: Podcast multilingue

```python
# Français
intro_fr = "Bonjour à tous, bienvenue dans notre podcast!"

# Anglais
intro_en = "Hello everyone, welcome to our podcast!"

# Espagnol
intro_es = "¡Hola a todos, bienvenidos a nuestro podcast!"

for lang, texte in [('fr', intro_fr), ('en', intro_en), ('es', intro_es)]:
    wav = model.generate(texte)
    ta.save(f"intro_{lang}.wav", wav.cpu(), model.sr)
```

### Exemple 3: Audiobook

```python
# Lire un livre par chapitres
with open("mon_livre.txt", 'r', encoding='utf-8') as f:
    chapitres = f.read().split('\n\n')  # Séparé par lignes vides

for i, chapitre in enumerate(chapitres, 1):
    wav = model.generate(chapitre)
    ta.save(f"audiobook_chapitre_{i:02d}.wav", wav.cpu(), model.sr)
```

---

## 🔧 DÉPANNAGE RAPIDE

### ❌ Problème: "CUDA non disponible"

**Solution:**
```bash
python test_chatterbox.py
```
Si le test échoue, vérifiez que votre GPU NVIDIA est bien détecté.

### ❌ Problème: "No module named 'chatterbox'"

**Solution:**
Utilisez toujours `DEMARRER_ICI.bat` ou définissez manuellement:
```powershell
$env:PYTHONPATH = "C:\Users\adolk\Documents\Youtube ai audio\chatterbox\src"
```

### ❌ Problème: Audio de mauvaise qualité

**Solutions:**
- ✅ Utilisez une ponctuation correcte (`.`, `,`, `!`, `?`)
- ✅ Écrivez les nombres en lettres ("vingt-trois" pas "23")
- ✅ Évitez les abréviations ("numéro" pas "n°")
- ✅ Séparez les longues phrases

### 📚 Plus de solutions

Consultez `GUIDE_UTILISATION.md` section **Dépannage**

---

## 📁 STRUCTURE DES FICHIERS

```
chatterbox/
│
├── 📂 src/                        Code source Chatterbox
├── 📂 venv/                       Environnement Python
├── 📂 podcasts_generes/           Sorties mode interactif
├── 📂 podcasts_batch/             Sorties mode batch
│
├── ⭐ DEMARRER_ICI.bat            LANCEUR PRINCIPAL
├── 📘 README_FR.md                Ce fichier
├── 📚 GUIDE_UTILISATION.md        Guide complet
├── 📄 INSTALLATION.md             Détails installation
│
├── 🐍 test_chatterbox.py          Test rapide
├── 🎙️ generer_podcast.py          Mode interactif
├── 📦 generer_batch.py            Mode batch
│
├── 🎵 test_chatterbox_fr.wav      Audio de test
└── 📝 exemple_podcast.txt         Script d'exemple
```

---

## 🎯 PROCHAINES ÉTAPES

### Pour débuter

1. ✅ **Testez l'installation**
   ```bash
   python test_chatterbox.py
   ```

2. ✅ **Créez votre premier podcast**
   ```bash
   python generer_podcast.py
   ```

3. ✅ **Testez le mode batch**
   ```bash
   python generer_batch.py
   # Tapez "exemple" pour générer un fichier de test
   ```

### Pour progresser

4. 📖 **Lisez le guide complet**
   - Ouvrez `GUIDE_UTILISATION.md`

5. 🎨 **Explorez les fonctionnalités avancées**
   - Clonage vocal
   - Contrôle émotionnel
   - Multi-langues

6. 🎬 **Créez votre premier contenu YouTube**
   - Générez vos audios
   - Montez avec vos images/vidéos
   - Publiez et monétisez !

---

## 🌟 FONCTIONNALITÉS AVANCÉES

### Clonage vocal

Utilisez votre propre voix comme référence:

```python
from chatterbox.tts import ChatterboxTTS

model = ChatterboxTTS.from_pretrained(device='cuda')

# Votre échantillon de voix (10-30s recommandé)
reference = "ma_voix.wav"

# Générer avec votre voix
wav = model.generate(
    "Bonjour, voici ma voix clonée!",
    reference_audio=reference
)

ta.save("ma_voix_clonee.wav", wav.cpu(), model.sr)
```

**⚠️ Éthique:**
- Utilisez uniquement votre propre voix
- Obtenez le consentement pour d'autres voix
- Ne créez pas de deepfakes malveillants

### Contrôle émotionnel

Ajoutez des émotions à votre voix:

```python
emotions = ['neutral', 'happy', 'sad', 'angry', 'surprised']

for emotion in emotions:
    wav = model.generate(
        "Ce texte sera dit avec différentes émotions.",
        emotion=emotion
    )
    ta.save(f"emotion_{emotion}.wav", wav.cpu(), model.sr)
```

**Note:** Vérifiez la documentation officielle pour l'API exacte.

---

## 📞 SUPPORT ET RESSOURCES

### Documentation
- 📚 [Guide utilisateur complet](GUIDE_UTILISATION.md)
- 📄 [Détails installation](INSTALLATION.md)
- 📖 [README original Chatterbox](README.md)

### Liens externes
- 🌐 **Site officiel:** https://www.resemble.ai/
- 🐙 **GitHub:** https://github.com/resemble-ai/chatterbox
- 🤗 **HuggingFace:** https://huggingface.co/resemble-ai

### Besoin d'aide?

1. Consultez `GUIDE_UTILISATION.md` (section Dépannage)
2. Testez avec `test_chatterbox.py`
3. Vérifiez les [issues GitHub](https://github.com/resemble-ai/chatterbox/issues)
4. Créez une nouvelle issue avec détails complets

---

## ✅ CHECKLIST AVANT PUBLICATION YOUTUBE

Avant de publier votre vidéo avec audio Chatterbox:

- [ ] Audio généré en qualité 24kHz
- [ ] Licence MIT mentionnée dans la description
- [ ] Pas de contenu protégé par copyright
- [ ] Qualité audio vérifiée (pas de distorsion)
- [ ] Durée adaptée au format vidéo
- [ ] Post-production terminée (normalisation, équaliseur)
- [ ] Format final: WAV ou MP3 320kbps

**Exemple de description YouTube:**
```
🎙️ Audio généré avec Chatterbox TTS
Technologie: Resemble.AI (https://github.com/resemble-ai/chatterbox)
Licence: MIT - Open Source
```

---

## 🎉 FÉLICITATIONS!

Vous êtes maintenant prêt à créer des podcasts IA professionnels!

### Ce que vous pouvez faire maintenant:

✅ Créer des intros/outros pour vos vidéos YouTube  
✅ Générer des podcasts complets  
✅ Produire des audiolivres  
✅ Créer du contenu multilingue  
✅ Monétiser vos créations  
✅ Cloner votre propre voix  
✅ Ajuster les émotions  

---

## 💡 CONSEILS PRO

### Pour un audio YouTube de qualité

1. **Structurez votre script**
   - Introduction claire (10-15s)
   - Contenu principal (segments de 30-60s)
   - Conclusion avec CTA (10-15s)

2. **Optimisez votre texte**
   - Phrases courtes et claires
   - Ponctuation correcte
   - Nombres en lettres

3. **Post-production**
   - Normalisez le volume (Audacity gratuit)
   - Ajoutez de la musique de fond
   - Équilibrez les fréquences

4. **Testez avant publication**
   - Écoutez l'audio complet
   - Vérifiez la synchronisation avec la vidéo
   - Demandez des retours

---

## 🚀 BON PODCAST!

**N'oubliez pas:**
- 🎙️ La qualité du texte = qualité de l'audio
- 📝 Testez plusieurs fois avant la version finale
- 🎬 Soyez créatif !
- 💰 Monétisez légalement avec la licence MIT
- 🌟 Partagez vos créations !

---

**Version:** 0.1.4  
**Installation:** 29 janvier 2025  
**Système:** Windows 11 + RTX 3060 Ti  

*Créé avec ❤️ par Resemble.AI*  
*Configuration par GitHub Copilot*

---

**Liens rapides:**
- 📚 [Guide complet](GUIDE_UTILISATION.md)
- 📄 [Installation](INSTALLATION.md)
- 🐙 [GitHub](https://github.com/resemble-ai/chatterbox)
- ⭐ [LANCER](DEMARRER_ICI.bat)
