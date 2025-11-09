# 🎤 Guide de la Bibliothèque de Voix Intégrée

## 📚 Vue d'ensemble

Chatterbox dispose maintenant d'un **système de bibliothèque de voix intégrée** qui vous permet de :
- ✅ Organiser vos voix de référence
- ✅ Sélectionner rapidement une voix depuis le menu
- ✅ Gérer plusieurs profils vocaux (homme, femme, etc.)
- ✅ Tester vos voix avant utilisation

---

## 🚀 Démarrage rapide

### 1️⃣ Initialiser la bibliothèque

```powershell
cd "C:\Users\adolk\Documents\Youtube ai audio\chatterbox"
.\venv\Scripts\activate
python gestionnaire_voix.py --init
```

**Résultat :**
```
✅ Créé : voix_bibliotheque/homme/
✅ Créé : voix_bibliotheque/femme/
✅ Créé : voix_bibliotheque/autres/
```

### 2️⃣ Ajouter vos voix

**Option A : Vos propres enregistrements**

Enregistrez votre voix (20-30 secondes) et placez le fichier :
```
voix_bibliotheque/
├── homme/
│   └── ma_voix.wav          ← Votre enregistrement
```

**Option B : Voix existantes**

Copiez vos fichiers audio dans les dossiers appropriés :
```powershell
# Exemple Windows
copy "C:\Mes_Enregistrements\voix_podcast.wav" "voix_bibliotheque\homme\"
```

### 3️⃣ Vérifier la bibliothèque

```powershell
python gestionnaire_voix.py --liste
```

**Affichage :**
```
🎤 BIBLIOTHÈQUE DE VOIX CHATTERBOX
======================================================================
📊 Total : 3 voix disponibles

👨 Voix Homme
----------------------------------------------------------------------
   1. ma_voix.wav                              (  523.4 Ko)
   2. voix_podcast_fr.wav                      (  892.1 Ko)

👩 Voix Femme
----------------------------------------------------------------------
   1. voix_femme_douce.wav                     (  645.8 Ko)
======================================================================
```

### 4️⃣ Utiliser dans le script interactif

```powershell
python generer_long_audio_interactive.py
```

**Nouveau menu :**
```
🎤 CHOIX DE LA VOIX
Options:
1. Voix par défaut Chatterbox
2. Choisir depuis la bibliothèque de voix    ← NOUVEAU !
3. Utiliser votre propre fichier (chemin manuel)

Votre choix (1, 2 ou 3): 2
```

**Puis :**
```
🎤 BIBLIOTHÈQUE DE VOIX
======================================================================

👨 HOMME
----------------------------------------------------------------------
   1. ma_voix.wav                              (  523.4 Ko)
   2. voix_podcast_fr.wav                      (  892.1 Ko)

👩 FEMME
----------------------------------------------------------------------
   3. voix_femme_douce.wav                     (  645.8 Ko)

======================================================================

Choisissez une voix (1-3, Entrée=annuler): 1

✅ Voix sélectionnée: ma_voix.wav
```

---

## 📁 Organisation de la bibliothèque

### Structure recommandée

```
voix_bibliotheque/
│
├── homme/                           # Voix masculines
│   ├── voix_homme_neutre.wav       # Usage général
│   ├── voix_journaliste_fr.wav     # Actualités
│   ├── voix_podcast_tech.wav       # Podcast technologie
│   └── voix_meditation_grave.wav   # Méditation/relaxation
│
├── femme/                           # Voix féminines
│   ├── voix_femme_neutre.wav       # Usage général
│   ├── voix_podcast_dynamique.wav  # Podcast énergique
│   ├── voix_douce_enfant.wav       # Histoires pour enfants
│   └── voix_prof_tutoriel.wav      # Tutoriels pédagogiques
│
├── autres/                          # Voix spéciales
│   ├── voix_enfant_garcon.wav      # Voix d'enfant
│   ├── voix_ado.wav                # Voix adolescent
│   └── voix_robot.wav              # Voix synthétique
│
└── README.md                        # Documentation
```

### Conventions de nommage

**Format recommandé :**
```
voix_[genre]_[style]_[langue].wav

Exemples :
voix_homme_journaliste_fr.wav
voix_femme_podcast_en.wav
voix_neutre_meditation_fr.wav
```

**Catégories par genre :**
- `homme/` : Voix masculines adultes
- `femme/` : Voix féminines adultes
- `autres/` : Enfants, ados, voix spéciales

**Catégories par usage :**
- Journalisme : `voix_*_journaliste.wav`
- Podcast : `voix_*_podcast.wav`
- Tutoriel : `voix_*_tutoriel.wav`
- Méditation : `voix_*_meditation.wav`
- Storytelling : `voix_*_narrateur.wav`

---

## 🎙️ Créer vos voix de référence

### Méthode 1 : Enregistrement smartphone

**Matériel :**
- 📱 Smartphone (appli Enregistreur vocal)
- 🎧 Écouteurs avec micro (optionnel mais recommandé)
- 🚪 Pièce calme

**Procédure :**
1. Lancez l'enregistreur vocal
2. Tenez le téléphone à 20cm de la bouche
3. Lisez un texte naturel pendant 20-30 secondes
4. Sauvegardez et transférez vers PC

**Texte suggéré :**
```
Bonjour, je suis ravi de vous retrouver pour ce nouveau podcast.
Aujourd'hui, nous allons explorer un sujet fascinant qui concerne
tout le monde. Que vous soyez débutant ou expert, vous trouverez
des informations précieuses dans cet épisode. Restez avec moi !
```

### Méthode 2 : Enregistrement PC (Audacity)

**1. Installation :**
```
Télécharger : https://www.audacityteam.org/
```

**2. Configuration :**
- Projet > Fréquence : **24000 Hz** (ou 44100 Hz)
- Qualité : **Mono** (1 canal)

**3. Enregistrement :**
- Cliquez sur 🔴 **Enregistrer**
- Parlez clairement pendant 20-30s
- Cliquez sur ⏹️ **Stop**

**4. Nettoyage (optionnel) :**
```
1. Effet > Réduction du bruit
   - Analyser le bruit (2s de silence)
   - Réduire (Réduction: 12 dB)

2. Effet > Normaliser
   - Niveau max: -1.0 dB
   - Appliquer

3. Fichier > Exporter > WAV
   - Format: WAV (Microsoft) 16-bit PCM
   - Nom: voix_[description].wav
```

**5. Placement :**
```powershell
move voix_ma_voix.wav "C:\Users\adolk\Documents\Youtube ai audio\chatterbox\voix_bibliotheque\homme\"
```

### Méthode 3 : Utiliser une génération existante

Si vous avez déjà généré un audio avec Chatterbox qui vous plaît :

```powershell
# Copier un audio généré comme référence
copy "output_long_audio.wav" "voix_bibliotheque\homme\voix_base_podcast.wav"
```

**Avantage :** Qualité garantie, déjà compatible
**Inconvénient :** Voix synthétique (pas votre vraie voix)

---

## 🔧 Gestionnaire de voix (CLI)

### Commandes disponibles

**Lister toutes les voix :**
```powershell
python gestionnaire_voix.py --liste
# ou
python gestionnaire_voix.py -l
```

**Initialiser la structure :**
```powershell
python gestionnaire_voix.py --init
```

**Tester une voix :**
```powershell
python gestionnaire_voix.py --test ma_voix.wav
```
Génère un court audio de test : `test_voix_ma_voix.wav`

**Chercher une voix :**
```powershell
python gestionnaire_voix.py --chercher podcast
```
Trouve toutes les voix contenant "podcast" dans le nom

**Aide :**
```powershell
python gestionnaire_voix.py --help
```

---

## 💡 Utilisation avancée

### Combiner voix + preset + langue

**Exemple 1 : Podcast tech en français**
```powershell
python generer_long_audio_interactive.py
```
Sélections :
- Texte : `script_podcast.txt`
- Langue : `fr` (auto)
- Voix : **2. Bibliothèque** → `voix_podcast_tech.wav`
- Ton : **4. Podcast dynamique**

**Exemple 2 : Actualités avec voix journaliste**
```powershell
python generer_long_audio_interactive.py \
  --texte actualites.txt \
  --voix voix_bibliotheque/homme/voix_journaliste_fr.wav \
  --ton journaliste
```

**Exemple 3 : Méditation guidée**
```powershell
python generer_long_audio_interactive.py \
  --texte meditation.txt \
  --voix voix_bibliotheque/femme/voix_douce_enfant.wav \
  --ton meditation \
  --output meditation_douce.wav
```

### Créer une collection thématique

**Podcast Gaming :**
```
voix_bibliotheque/
└── homme/
    ├── voix_gaming_energique.wav    # Intro/Outro dynamiques
    ├── voix_gaming_analyse.wav      # Analyse calme
    └── voix_gaming_reaction.wav     # Réactions spontanées
```

**Usage :**
- Intro : Voix énergique + preset `podcast_dynamique`
- Contenu : Voix analyse + preset `podcast_info`
- Outro : Voix réaction + preset `podcast_dynamique`

---

## 📊 Recommandations par type de contenu

| Type de contenu | Voix recommandée | Preset | Durée ref |
|----------------|------------------|---------|-----------|
| **Actualités** | Homme/Femme neutre | `journaliste` | 20-30s |
| **Podcast éducatif** | Voix claire, posée | `podcast_info` | 25-30s |
| **Podcast divertissement** | Voix dynamique | `podcast_dynamique` | 20-25s |
| **Tutoriel** | Voix pédagogique | `tutoriel` | 25-30s |
| **Histoire pour enfants** | Voix douce, expressive | `enfant` | 20-25s |
| **Méditation** | Voix calme, grave | `meditation` | 30s |
| **Documentaire** | Voix posée, sérieuse | `documentaire` | 25-30s |
| **Publicité** | Voix persuasive | `publicite` | 15-20s |
| **Audiobook** | Voix claire, neutre | `narrateur` | 30s |
| **Storytelling** | Voix expressive | `storytelling` | 25-30s |

---

## ✅ Critères de qualité

### ✔️ Bonne voix de référence

- **Durée :** 20-30 secondes (optimal : 25s)
- **Qualité audio :**
  - Pas de bruit de fond
  - Pas d'écho/réverbération
  - Volume stable
- **Contenu :**
  - Phrases naturelles (pas de mots isolés)
  - Intonation variée
  - Débit normal (ni trop rapide, ni trop lent)
- **Format technique :**
  - WAV 16-bit ou 24-bit
  - Sample rate : 24kHz, 44.1kHz ou 48kHz
  - Mono (1 canal) ou Stéréo

### ❌ Éviter

- ❌ Enregistrements trop courts (< 10s)
- ❌ Musique de fond
- ❌ Bruits parasites (clics, pops, ventilateur)
- ❌ Voix trop compressée/filtrée
- ❌ Formats lossy trop compressés (MP3 < 128kbps)
- ❌ Multiple speakers dans le même fichier

---

## 🎯 Cas d'usage réels

### Cas 1 : YouTuber gaming

**Besoin :** 3-4 voix différentes pour varier le contenu

**Solution :**
```
voix_bibliotheque/homme/
├── voix_gaming_intro.wav      # Dynamique pour intros
├── voix_gaming_tuto.wav       # Calme pour tutos
└── voix_gaming_rage.wav       # Expressive pour fails
```

**Workflow :**
1. Enregistrer 3 échantillons avec différents tons
2. Générer intro : `--voix intro.wav --ton podcast_dynamique`
3. Générer tuto : `--voix tuto.wav --ton tutoriel`
4. Générer rage : `--voix rage.wav --ton storytelling`

### Cas 2 : Chaîne éducative multilingue

**Besoin :** Voix pour FR, EN, ES

**Solution :**
```
voix_bibliotheque/homme/
├── voix_prof_fr.wav
├── voix_prof_en.wav
└── voix_prof_es.wav
```

**Workflow :**
```powershell
# Français
python generer_long_audio_interactive.py \
  --texte cours_fr.txt --langue fr \
  --voix voix_bibliotheque/homme/voix_prof_fr.wav --ton tutoriel

# Anglais
python generer_long_audio_interactive.py \
  --texte course_en.txt --langue en \
  --voix voix_bibliotheque/homme/voix_prof_en.wav --ton tutoriel
```

### Cas 3 : Podcast avec plusieurs animateurs

**Besoin :** 2 voix (co-animateurs)

**Solution :**
```
voix_bibliotheque/
├── homme/voix_animateur1.wav
└── femme/voix_animatrice2.wav
```

**Workflow :**
1. Séparer le script par intervenant :
   - `script_partie_animateur1.txt`
   - `script_partie_animateur2.txt`
2. Générer séparément :
   ```powershell
   python generer_long_audio_interactive.py \
     --texte script_partie_animateur1.txt \
     --voix voix_bibliotheque/homme/voix_animateur1.wav \
     --ton podcast_dynamique -o partie1.wav
   
   python generer_long_audio_interactive.py \
     --texte script_partie_animateur2.txt \
     --voix voix_bibliotheque/femme/voix_animatrice2.wav \
     --ton podcast_dynamique -o partie2.wav
   ```
3. Assembler avec Audacity ou autre logiciel

---

## 🆘 Dépannage

### Problème : "Aucune voix trouvée dans la bibliothèque"

**Solution :**
```powershell
# 1. Vérifier la structure
python gestionnaire_voix.py --init

# 2. Lister le contenu
dir voix_bibliotheque /s

# 3. Ajouter une voix test
copy test_chatterbox_fr.wav voix_bibliotheque\homme\voix_test.wav

# 4. Vérifier
python gestionnaire_voix.py --liste
```

### Problème : "La voix générée ne ressemble pas à ma référence"

**Causes possibles :**
1. Référence trop courte (< 15s)
2. Mauvaise qualité audio (bruit, compression)
3. Preset incompatible

**Solutions :**
```powershell
# 1. Nettoyer l'audio avec Audacity (voir section "Méthode 2")

# 2. Allonger la référence (25-30s optimal)

# 3. Tester avec preset neutre
python gestionnaire_voix.py --test ma_voix.wav

# 4. Essayer différents presets
```

### Problème : "Fichier audio non supporté"

**Formats supportés :** WAV, MP3, FLAC, OGG

**Conversion avec FFmpeg :**
```powershell
# Installer FFmpeg (si pas déjà fait)
winget install ffmpeg

# Convertir en WAV
ffmpeg -i ma_voix.mp3 -ar 24000 -ac 1 ma_voix.wav
```

---

## 📚 Ressources externes

### Voix libres de droits

**1. Common Voice (Mozilla)**
- URL : https://commonvoice.mozilla.org/
- Licence : CC0 (domaine public)
- Langues : 100+ langues
- Format : MP3

**2. LibriVox**
- URL : https://librivox.org/
- Licence : Domaine public
- Type : Audiolivres
- Format : MP3, OGG

**3. OpenVoice**
- URL : https://github.com/myshell-ai/OpenVoice
- Licence : MIT (vérifier selon version)
- Type : Voix synthétiques
- Format : WAV

### Outils recommandés

**Enregistrement :**
- Audacity (gratuit) : https://www.audacityteam.org/
- OBS Studio (gratuit) : https://obsproject.com/

**Édition audio :**
- Audacity (gratuit)
- Adobe Audition (payant)
- Reaper (essai gratuit)

**Conversion de format :**
- FFmpeg (CLI) : https://ffmpeg.org/
- HandBrake (GUI) : https://handbrake.fr/

---

## 🎉 Conclusion

La **bibliothèque de voix intégrée** transforme Chatterbox en un outil professionnel avec :

✅ **Organisation** : Classez vos voix par catégorie
✅ **Rapidité** : Sélectionnez une voix en 2 clics
✅ **Flexibilité** : Combinez voix + presets + langues
✅ **Qualité** : Utilisez vos propres voix authentiques

**Workflow complet :**
1. Enregistrez votre voix (20-30s)
2. Ajoutez-la à `voix_bibliotheque/homme/` ou `femme/`
3. Lancez le script interactif
4. Sélectionnez votre voix depuis le menu
5. Choisissez un preset de ton
6. Générez votre podcast YouTube !

**Prochaines étapes :**
```powershell
# Initialiser la bibliothèque
python gestionnaire_voix.py --init

# Enregistrer votre voix (Audacity, smartphone, etc.)

# Ajouter votre voix
copy ma_voix.wav voix_bibliotheque\homme\

# Vérifier
python gestionnaire_voix.py --liste

# Tester
python generer_long_audio_interactive.py
```

🎙️ **Bonne création de contenu !** ✨
