# 🎯 CHATTERBOX - GUIDE RAPIDE

## 🚀 LANCEMENT RAPIDE

### Interface Web (GUI)
```powershell
.\LANCER_INTERFACE.bat
```
- Interface sur http://127.0.0.1:7860
- Lien public pour accès distant
- Limite de texte supprimée

---

## 🎙️ GÉNÉRATION D'AUDIOS LONGS

### Méthode 1 : Mode Interactif (Recommandé)

```powershell
cd "C:\Users\adolk\Documents\Youtube ai audio\chatterbox"
.\venv\Scripts\activate
python generer_long_audio_interactive.py
```

**Le script vous demande :**
1. 📝 Source du texte (saisie directe ou fichier .txt)
2. 🌍 Langue (fr/en/etc. - détection auto)
3. 🎤 Voix (défaut, bibliothèque, ou fichier manuel) ⭐ NOUVEAU !
4. 🎭 **TON/STYLE** (journaliste, podcast, pub, etc.)
5. 💾 Nom du fichier de sortie

**11 presets de tons disponibles :**
- 📰 Journaliste TV/Radio
- 📖 Narrateur audiobook
- 🎙️ Podcast informatif
- ⚡ Podcast dynamique
- 📢 Publicité/Promo
- 🎬 Documentaire
- 🎓 Tutoriel/Formation
- 🧘 Méditation/Relaxation
- ✨ Storytelling/Histoire
- 🧒 Contenu pour enfants
- ⚙️ Personnalisé (paramètres manuels)

**Tout est guidé étape par étape !**

---

### Méthode 2 : Ligne de commande

**Avec preset de ton (NOUVEAU ⭐):**
```powershell
# Ton journaliste
python generer_long_audio_interactive.py ^
  --texte mon_script.txt ^
  --ton journaliste ^
  --output podcast.wav

# Podcast dynamique avec votre voix
python generer_long_audio_interactive.py ^
  --texte script.txt ^
  --voix "mes_voix\ma_voix.wav" ^
  --ton podcast_dynamique ^
  --output episode.wav

# Méditation avec voix calme
python generer_long_audio_interactive.py ^
  --texte meditation.txt ^
  --ton meditation ^
  --voix "voix_calme.wav"
```

**Avec paramètres manuels :**
```powershell
python generer_long_audio_interactive.py ^
  --texte exemple_script.txt ^
  --output test.wav ^
  --expression 0.6 ^
  --temperature 0.8
```

---

## 🎤 BIBLIOTHÈQUE DE VOIX (NOUVEAU ⭐)

### Initialisation

```powershell
python gestionnaire_voix.py --init
```
Crée la structure :
```
voix_bibliotheque/
├── homme/
├── femme/
└── autres/
```

### Ajouter vos voix

**Copier vos fichiers audio :**
```powershell
copy ma_voix.wav voix_bibliotheque\homme\
copy voix_podcast.wav voix_bibliotheque\femme\
```

**Lister les voix disponibles :**
```powershell
python gestionnaire_voix.py --liste
```

### Utilisation

**Mode interactif :**
```powershell
python generer_long_audio_interactive.py
```
Sélectionnez :
- 🎤 Voix → **2. Bibliothèque** ← Nouveau !
- Choisissez dans la liste affichée

**Ligne de commande :**
```powershell
python generer_long_audio_interactive.py ^
  --texte script.txt ^
  --voix voix_bibliotheque\homme\ma_voix.wav ^
  --ton podcast_dynamique
```

**Voir le guide complet :** `GUIDE_BIBLIOTHEQUE_VOIX.md`

---

## 🎤 ENREGISTRER VOTRE VOIX

### Étape 1 : Enregistrer

**Durée idéale : 20-30 secondes**

**Avec smartphone :**
- iPhone → "Mémos vocaux"
- Android → "Enregistreur"

**Avec PC :**
- Téléchargez Audacity (gratuit)
- Branchez un micro USB ou utilisez le micro intégré
- Enregistrez 20-30s de lecture naturelle

**Texte suggéré :**
```
Bonjour, je m'appelle [nom]. 
Je crée des podcasts sur [sujet]. 
J'espère que ce contenu vous sera utile. 
N'hésitez pas à vous abonner. 
Merci et à bientôt !
```

### Étape 2 : Nettoyer (optionnel)

**Avec Audacity :**
1. Ouvrir votre fichier
2. Supprimer silences début/fin
3. `Effet > Normaliser`
4. Exporter en WAV

**Temps : 2 minutes**

### Étape 3 : Ajouter à la bibliothèque

```powershell
# Copier dans la bibliothèque
copy ma_voix.wav voix_bibliotheque\homme\voix_podcast_fr.wav

# Vérifier
python gestionnaire_voix.py --liste

# Utiliser
python generer_long_audio_interactive.py
# → Choisir option 2 (Bibliothèque)

---

## ⚙️ PARAMÈTRES RECOMMANDÉS

### Presets de tons (NOUVEAU ⭐)

**Choisissez simplement le preset adapté à votre contenu !**

| Preset | Utilisation | Caractéristiques |
|--------|-------------|------------------|
| **journaliste** | Actualités, reportages | Professionnel, neutre, autoritaire |
| **narrateur** | Livres audio, contes | Calme, posé, apaisant |
| **podcast_info** | Podcasts éducatifs | Conversationnel, accessible |
| **podcast_dynamique** | Podcasts divertissants | Énergique, enthousiaste |
| **publicite** | Pubs, promos | Vendeur, persuasif, rapide |
| **documentaire** | Documentaires, analyses | Sérieux, contemplatif |
| **tutoriel** | Tutos, formations | Pédagogique, clair |
| **meditation** | Méditation, relaxation | Très calme, apaisant |
| **storytelling** | Histoires, anecdotes | Expressif, captivant |
| **enfant** | Contenu jeunesse | Joyeux, animé |

**Détails complets dans `GUIDE_PRESETS_TONS.md`**

---

### Paramètres manuels (avancé)

**Si vous préférez tout contrôler :**

### Par type de contenu

**Podcast informatif :**
```
Expression (exaggeration): 0.5
Température: 0.7
CFG Weight: 0.5
```

**Podcast dynamique :**
```
Expression: 0.7
Température: 0.8
CFG Weight: 0.4
```

**Narration calme :**
```
Expression: 0.4
Température: 0.7
CFG Weight: 0.6
```

---

## 📊 TEMPS DE GÉNÉRATION (RTX 3060 Ti)

| Durée audio | Temps génération |
|-------------|------------------|
| 1 minute    | ~40 secondes     |
| 5 minutes   | ~3-4 minutes     |
| 10 minutes  | ~6-8 minutes     |
| 15 minutes  | ~10-12 minutes   |

**Ratio : ~1 min génération = 1.5 min audio**

---

## 🌍 LANGUES SUPPORTÉES

Chatterbox détecte automatiquement la langue du texte.

**Langues disponibles :**
- 🇫🇷 Français
- 🇬🇧 Anglais
- 🇪🇸 Espagnol
- 🇩🇪 Allemand
- 🇮🇹 Italien
- 🇵🇹 Portugais
- 🇵🇱 Polonais
- 🇹🇷 Turc
- 🇷🇺 Russe
- 🇳🇱 Néerlandais
- 🇨🇿 Tchèque
- 🇸🇦 Arabe
- 🇨🇳 Chinois
- 🇯🇵 Japonais
- 🇰🇷 Coréen
- 🇮🇳 Hindi

**23 langues au total !**

---

## 📁 STRUCTURE DES FICHIERS

```
Youtube ai audio/
  chatterbox/
    LANCER_INTERFACE.bat          ← Interface web
    generer_long_audio_interactive.py  ← Script interactif
    exemple_script.txt            ← Exemple de texte
    
    mes_voix/                     ← Créez ce dossier
      ma_voix.wav                 ← Votre enregistrement
      
    podcasts_longs/               ← Audios générés
      episode_01.wav
      episode_02.wav
      
    GUIDES:
      GUIDE_UTILISATION.md        ← Utilisation générale
      GUIDE_AUDIOS_LONGS.md       ← Podcasts longs
      GUIDE_CLONAGE_VOIX.md       ← Votre propre voix
      ACCES_DISTANT.md            ← Accès depuis autres PC
```

---

## 🛠️ COMMANDES UTILES

### Activer l'environnement virtuel
```powershell
cd "C:\Users\adolk\Documents\Youtube ai audio\chatterbox"
.\venv\Scripts\activate
```

### Tester rapidement
```powershell
python test_chatterbox.py
```

### Vérifier CUDA
```powershell
python -c "import torch; print(torch.cuda.is_available())"
```

### Interface web
```powershell
.\LANCER_INTERFACE.bat
```

---

## 🎬 WORKFLOW YOUTUBE COMPLET

**Pour un podcast de 10 minutes :**

1. **Écriture du script** (15 min)
   - ~3500 caractères (~600 mots)
   - Bonne ponctuation
   - Sauvegarde en .txt

2. **Génération audio** (8 min)
   ```powershell
   python generer_long_audio_interactive.py
   ```

3. **Post-production** (10 min - optionnel)
   - Audacity : Intro/outro musicale
   - Normalisation volume
   - Export MP3

4. **Création vidéo** (5 min)
   - Image fixe (Canva)
   - DaVinci Resolve (gratuit)
   - Synchronisation audio/image

5. **Upload YouTube** (5 min)
   - Titre SEO
   - Description
   - Tags
   - Miniature

**Total : ~45 minutes pour 10 min de podcast prêt !**

---

## 💰 MONÉTISATION

**Licence MIT = ✅ Usage commercial autorisé**

**Requirements YouTube :**
- 1000 abonnés
- 4000 heures de visionnage (12 mois)

**Chatterbox est parfait pour YouTube !**

---

## 🆘 AIDE RAPIDE

### ❌ Problème courant : Port 7860 déjà utilisé

```powershell
Get-Process python | Stop-Process -Force
```

### ❌ Module non trouvé

```powershell
$env:PYTHONPATH = "$PWD\src"
.\venv\Scripts\activate
```

### ❌ CUDA non détecté

- Vérifiez les drivers NVIDIA
- Redémarrez le PC
- Vérifiez avec : `nvidia-smi`

---

## 📚 DOCUMENTATION COMPLÈTE

| Fichier | Contenu |
|---------|---------|
| `GUIDE_UTILISATION.md` | Utilisation générale de Chatterbox |
| `GUIDE_AUDIOS_LONGS.md` | Générer podcasts 5-15 minutes |
| `GUIDE_CLONAGE_VOIX.md` | **Utiliser votre propre voix** |
| `GUIDE_PRESETS_TONS.md` | ⭐ **Guide des 11 presets de tons** |
| `GUIDE_BIBLIOTHEQUE_VOIX.md` | ⭐ **Bibliothèque de voix intégrée** |
| `GUIDE_CLONAGE_VOIX.md` | Enregistrer et utiliser votre voix |
| `ACCES_DISTANT.md` | Accès depuis smartphone/autres PC |
| `INSTALLATION.md` | Installation technique |
| `README_FR.md` | Vue d'ensemble complète |
| `MEMO_RAPIDE.md` | Ce fichier - aide-mémoire rapide |

---

## 🎉 EXEMPLES RAPIDES

### Test de 30 secondes (voix par défaut)
```powershell
python generer_long_audio_interactive.py ^
  --texte exemple_script.txt ^
  --ton podcast_info ^
  --output test.wav
```

### Actualité journalistique
```powershell
python generer_long_audio_interactive.py ^
  --texte actualites.txt ^
  --ton journaliste ^
  --output actu.wav
```

### Podcast 5 minutes avec bibliothèque de voix
```powershell
# 1. Ajouter votre voix à la bibliothèque
copy ma_voix.wav voix_bibliotheque\homme\

# 2. Générer le podcast
python generer_long_audio_interactive.py
# Choisir : Bibliothèque > ma_voix.wav > Preset podcast_dynamique
```

### Podcast avec voix manuelle
```powershell
python generer_long_audio_interactive.py ^
  --texte mon_script.txt ^
  --voix mes_voix\ma_voix.wav ^
  --ton podcast_dynamique ^
  --output episode_01.wav
```

### Méditation guidée
```powershell
python generer_long_audio_interactive.py ^
  --texte meditation.txt ^
  --ton meditation ^
  --voix voix_calme.wav ^
  --output meditation_10min.wav
```

### Mode interactif complet (recommandé)
```powershell
python generer_long_audio_interactive.py
# Puis suivez les instructions !
# Vous pourrez choisir parmi 11 presets de tons
```

---

## ✅ CHECKLIST AVANT GÉNÉRATION

**Préparation :**
- [ ] Script écrit et relu
- [ ] Ponctuation complète
- [ ] Fichier .txt sauvegardé
- [ ] Voix enregistrée (si clone vocal)
- [ ] GPU libre (fermez jeux/navigateur lourd)

**Lancement :**
- [ ] Environnement virtuel activé
- [ ] Script interactif lancé
- [ ] Paramètres ajustés
- [ ] Dossier de sortie créé

**Vérification :**
- [ ] Audio généré sans erreur
- [ ] Qualité satisfaisante (écoute)
- [ ] Durée correcte
- [ ] Voix naturelle

---

## 🚀 POUR ALLER PLUS LOIN

**Vous maîtrisez maintenant :**
✅ Interface web Gradio
✅ Génération d'audios longs (5-15 min)
✅ Clonage de votre propre voix
✅ Accès distant (lien public)
✅ Workflow YouTube complet

**Prochaines étapes :**
1. Enregistrez votre voix de référence
2. Testez avec `exemple_script.txt`
3. Créez votre premier vrai podcast
4. Uploadez sur YouTube
5. Monétisez ! 💰

**Bonne création de contenu !** 🎙️✨
