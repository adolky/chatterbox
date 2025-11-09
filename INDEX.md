# 📚 INDEX DES FICHIERS - CHATTERBOX TTS

> **Navigation rapide vers tous les fichiers et leur fonction**

---

## ⭐ FICHIERS ESSENTIELS (À CONNAÎTRE)

### 🚀 DÉMARRAGE RAPIDE

| Fichier | Type | Description |
|---------|------|-------------|
| **SYSTEME_COMPLET.md** | Guide | ⭐ **COMMENCEZ ICI** - Vue d'ensemble du système complet <br> • Workflow YouTube en 5-10 min <br> • Presets + Bibliothèque + Multilingue <br> • Exemples de production <br> • Aide rapide |
| **MEMO_RAPIDE.md** | Référence | ⚡ **Aide-mémoire essentiel** (lecture 5 min) <br> • Commandes principales <br> • Presets de tons <br> • Bibliothèque de voix <br> • Exemples rapides |
| **LANCER_INTERFACE.bat** | Lanceur | 🌐 Interface web Gradio <br> • Accès local + distant <br> • Share=True (lien public) <br> • Port 7860 |

### 📚 DOCUMENTATION PRINCIPALE

| Fichier | Taille | Description |
|---------|--------|-------------|
| **README_FR.md** | 62KB | 📘 Vue d'ensemble complète en français <br> • Qu'est-ce que Chatterbox? <br> • Installation et configuration <br> • Exemples de code <br> • Fonctionnalités avancées |
| **INSTALLATION.md** | 11KB | 📄 Détails de l'installation <br> • Composants installés <br> • Configuration matérielle <br> • Licence MIT (monétisation ✅) <br> • Support technique |
| **GUIDE_UTILISATION.md** | 10KB | 📚 Guide utilisateur complet <br> • Interface web <br> • Scripts Python <br> • Conseils YouTube <br> • Dépannage |

### ⭐ NOUVEAUTÉS (2024)

| Fichier | Taille | Description |
|---------|--------|-------------|
| **NOUVEAUTE_PRESETS.md** | 10KB | 🎭 **Système de presets de tons** <br> • 11 styles prédéfinis <br> • Journaliste, podcast, méditation, etc. <br> • Paramètres auto-appliqués |
| **NOUVEAUTE_BIBLIOTHEQUE.md** | 12KB | 🎤 **Bibliothèque de voix intégrée** <br> • Organisation automatique <br> • Sélection en 2 clics <br> • Gestion de profils multiples |

---

## 🐍 SCRIPTS PYTHON (UTILISATION)

### Scripts principaux

| Fichier | Fonction | Usage |
|---------|----------|-------|
| **test_chatterbox.py** | Test rapide | Test de base du système <br> `python test_chatterbox.py` |
| **generer_podcast.py** | Mode interactif | Génère un audio à la fois <br> `python generer_podcast.py` |
| **generer_batch.py** | Mode batch | Traite un fichier texte multi-segments <br> `python generer_batch.py` |
| **test_multilingue.py** | Test langues | Teste 9 langues différentes <br> `python test_multilingue.py` |

### Scripts d'exemple (Chatterbox original)

| Fichier | Fonction | Usage |
|---------|----------|-------|
| `example_tts.py` | Exemple TTS | Exemple officiel de synthèse vocale |
---

## 🎭 PRESETS DE TONS

| Fichier | Taille | Description |
|---------|--------|-------------|
| **GUIDE_PRESETS_TONS.md** | 12KB | 📖 **Guide complet des 11 presets** <br> • Description détaillée de chaque preset <br> • Paramètres techniques <br> • Exemples d'utilisation <br> • Tableau comparatif |

**11 presets disponibles :**
- 📰 Journaliste TV/Radio
- 📖 Narrateur audiobook
- 🎙️ Podcast informatif
- ⚡ Podcast dynamique (recommandé YouTube)
- 📢 Publicité/Promo
- 🎬 Documentaire
- 🎓 Tutoriel/Formation
- 🧘 Méditation/Relaxation
- ✨ Storytelling/Histoire
- 🧒 Contenu pour enfants
- ⚙️ Personnalisé (contrôle manuel)

---

## 🎤 BIBLIOTHÈQUE DE VOIX

| Fichier | Taille | Description |
|---------|--------|-------------|
| **GUIDE_BIBLIOTHEQUE_VOIX.md** | 15KB | 📚 **Guide complet bibliothèque** <br> • Enregistrer votre voix <br> • Organisation (homme/femme/autres) <br> • Cas d'usage professionnels <br> • Dépannage |
| **BIBLIOTHEQUE_VOIX_RESUME.md** | 10KB | ⚡ **Résumé rapide** <br> • Démarrage en 3 étapes <br> • Commandes gestionnaire <br> • FAQ |
| **VOIX_PAR_DEFAUT.md** | 8KB | 🤖 **Explication voix par défaut** <br> • Comment fonctionne la voix neutre <br> • Comparaison défaut vs. personnalisée <br> • Quand utiliser chaque option |
| **GUIDE_CLONAGE_VOIX.md** | 9KB | 🎙️ **Tutoriel enregistrement vocal** <br> • Comment enregistrer (Audacity, smartphone) <br> • Nettoyage audio <br> • Critères de qualité |
| **gestionnaire_voix.py** | Script | 🔧 **Gestionnaire CLI bibliothèque** <br> • Lister voix : `--liste` <br> • Tester voix : `--test` <br> • Chercher : `--chercher` |

**Dossier bibliothèque :**
```
voix_bibliotheque/
├── homme/         # Voix masculines
├── femme/         # Voix féminines
├── autres/        # Voix spéciales
└── README.md      # Documentation
```

---

## 📝 GÉNÉRATION D'AUDIOS LONGS

| Fichier | Taille | Description |
|---------|--------|-------------|
| **generer_long_audio_interactive.py** | Script | ⭐ **Script principal production** <br> • Mode interactif guidé <br> • 11 presets de tons intégrés <br> • Bibliothèque de voix intégrée <br> • Support CLI avec --ton et --voix <br> • Audios 5-15 minutes |
| **generer_long_audio.py** | Script | 📄 Script basique audios longs <br> • Version simple sans menu <br> • Exemple intégré |
| **GUIDE_AUDIOS_LONGS.md** | 17KB | 📚 **Guide génération longue** <br> • Segmentation intelligente <br> • Assemblage audio <br> • Optimisation performance |

---

## 🌐 ACCÈS DISTANT

| Fichier | Taille | Description |
|---------|--------|-------------|
| **ACCES_DISTANT.md** | 8KB | 🌍 **Configuration accès distant** <br> • Gradio share=True (lien public) <br> • Accès LAN (IP:7860) <br> • Configuration firewall |
| **gradio_tts_app.py** | Script | 🌐 **Interface web Gradio** <br> • Modifié : server_name="0.0.0.0" <br> • Modifié : share=True <br> • Port 7860 ouvert |

---

## 🐍 SCRIPTS PYTHON (UTILISATION)

### Scripts principaux

| Fichier | Fonction | Usage |
|---------|----------|-------|
| **generer_long_audio_interactive.py** | ⭐ Production | **Script principal recommandé** <br> `python generer_long_audio_interactive.py` <br> • Menu interactif complet <br> • Presets + Bibliothèque + CLI |
| **test_chatterbox.py** | Test rapide | Test de base du système <br> `python test_chatterbox.py` |
| **gestionnaire_voix.py** | Gestion voix | Gérer bibliothèque de voix <br> `python gestionnaire_voix.py --liste` |
| **generer_long_audio.py** | Simple | Version basique sans menu <br> `python generer_long_audio.py` |

### Scripts d'exemple (Chatterbox original)

| Fichier | Fonction | Usage |
|---------|----------|-------|
| `example_tts.py` | Exemple TTS | Exemple officiel de synthèse vocale |
| `example_vc.py` | Exemple VC | Exemple de conversion vocale |
| `example_for_mac.py` | Exemple Mac | Version pour macOS |
| `multilingual_app.py` | App multilingue | Application multilingue Gradio |

---

## 📁 DOSSIERS

### Dossiers systèmes

| Dossier | Contenu | Taille |
|---------|---------|--------|
| **src/** | Code source Chatterbox | ~500KB |
| **venv/** | Environnement virtuel Python 3.11 | ~4GB |
| **.git/** | Historique Git | Variable |

### Dossiers de sortie (créés automatiquement)

| Dossier | Créé par | Contenu |
|---------|----------|---------|
| **podcasts_generes/** | `generer_podcast.py` | Fichiers WAV du mode interactif |
| **podcasts_batch/** | `generer_batch.py` | Fichiers WAV du mode batch |
| **tests_multilingues/** | `test_multilingue.py` | Tests audio multilingues |

---

## 📄 FICHIERS CONFIGURATION

| Fichier | Type | Description |
|---------|------|-------------|
| `pyproject.toml` | Config | Configuration du projet Python <br> Dépendances et métadonnées |
| `.gitignore` | Git | Fichiers ignorés par Git |
| `LICENSE` | Licence | Licence MIT du projet |

---

## 🎨 RESSOURCES

| Fichier | Type | Description |
|---------|------|-------------|
| `Chatterbox-Multilingual.png` | Image | Logo/illustration Chatterbox |
| `test_chatterbox_fr.wav` | Audio | ✅ Test audio réussi (9.12s) |

---

## 📖 DOCUMENTATION OFFICIELLE

| Fichier | Langue | Description |
|---------|--------|-------------|
| `README.md` | Anglais | README original Chatterbox (en anglais) |

---

## 🗂️ ORGANISATION PAR USAGE

### Pour débuter

1. **DEMARRER_ICI.bat** - Double-cliquez ici
2. **AIDE_RAPIDE.md** - Lisez ça en 2 minutes
3. **test_chatterbox.py** - Lancez ce test

### Pour utiliser au quotidien

1. **generer_podcast.py** - Mode interactif
2. **generer_batch.py** - Mode batch
3. **AIDE_RAPIDE.md** - Référence rapide

### Pour approfondir

1. **README_FR.md** - Vue d'ensemble complète
2. **GUIDE_UTILISATION.md** - Guide détaillé
3. **INSTALLATION.md** - Infos techniques

### Pour développer

1. **src/** - Code source
2. **example_*.py** - Exemples officiels
3. **pyproject.toml** - Configuration

---

## 📊 STATISTIQUES

### Fichiers créés pour cette installation

| Type | Nombre | Taille totale |
|------|--------|---------------|
| **Documentation (MD)** | 5 | ~40KB |
| **Scripts Python** | 4 | ~18KB |
| **Lanceur** | 1 | ~1KB |
| **Audio généré** | 1 | ~875KB |
| **TOTAL fichiers créés** | 11 | ~934KB |

### Fichiers Chatterbox originaux

| Type | Nombre |
|------|--------|
| Scripts Python | 6 |
| Documentation | 1 |
| Configuration | 3 |
| Ressources | 1 |

### Dossiers système

| Dossier | Taille estimée |
|---------|----------------|
| **venv/** | ~4GB |
| **src/** | ~500KB |
| **Modèles (cache HuggingFace)** | ~3.2GB |
| **TOTAL système** | ~7.5GB |

---

## 🎯 NAVIGATION RAPIDE

### Par objectif

**Je veux commencer rapidement:**
1. `DEMARRER_ICI.bat`
2. `AIDE_RAPIDE.md`
3. `test_chatterbox.py`

**Je veux créer un podcast:**
1. `generer_podcast.py` (interactif)
2. `generer_batch.py` (batch)

**Je veux comprendre le système:**
1. `README_FR.md`
2. `GUIDE_UTILISATION.md`

**J'ai un problème:**
1. `AIDE_RAPIDE.md` (section Dépannage)
2. `GUIDE_UTILISATION.md` (section Dépannage détaillée)
3. `INSTALLATION.md` (support technique)

**Je veux voir des exemples:**
1. `test_chatterbox.py`
2. `test_multilingue.py`
3. `example_tts.py`

---

## 🔗 LIENS ENTRE FICHIERS

### Hiérarchie de lecture

```
DEMARRER_ICI.bat  →  Lance l'environnement
        ↓
AIDE_RAPIDE.md    →  Guide rapide (2 min)
        ↓
README_FR.md      →  Vue d'ensemble complète
        ↓
GUIDE_UTILISATION.md  →  Guide détaillé
        ↓
INSTALLATION.md   →  Détails techniques
```

### Dépendances de scripts

```
generer_podcast.py  ┐
generer_batch.py    ├─→  src/chatterbox/
test_chatterbox.py  │
test_multilingue.py ┘
```

---

## 📋 CHECKLIST D'UTILISATION

### Première utilisation

- [ ] Lire `AIDE_RAPIDE.md` (2 min)
- [ ] Lancer `DEMARRER_ICI.bat`
- [ ] Exécuter `python test_chatterbox.py`
- [ ] Tester `python generer_podcast.py`

### Utilisation régulière

- [ ] Lancer `DEMARRER_ICI.bat`
- [ ] Choisir mode (interactif ou batch)
- [ ] Générer vos audios
- [ ] Vérifier `podcasts_generes/` ou `podcasts_batch/`

### En cas de problème

- [ ] Consulter `AIDE_RAPIDE.md` (dépannage express)
- [ ] Relancer `test_chatterbox.py`
- [ ] Lire `GUIDE_UTILISATION.md` (dépannage détaillé)
- [ ] Consulter GitHub Issues

---

## 🎓 PARCOURS D'APPRENTISSAGE

### Niveau 1: Débutant (30 min)

1. Lire `AIDE_RAPIDE.md`
2. Lancer `DEMARRER_ICI.bat`
3. Tester `test_chatterbox.py`
4. Essayer `generer_podcast.py`

**Objectif:** Générer votre premier audio

### Niveau 2: Intermédiaire (1-2h)

1. Lire `README_FR.md`
2. Créer plusieurs audios avec `generer_podcast.py`
3. Tester le mode batch avec `generer_batch.py`
4. Explorer `test_multilingue.py`

**Objectif:** Maîtriser les deux modes de génération

### Niveau 3: Avancé (3-5h)

1. Lire `GUIDE_UTILISATION.md` en entier
2. Explorer les fonctionnalités avancées
3. Tester le clonage vocal
4. Créer votre premier contenu YouTube

**Objectif:** Utiliser toutes les fonctionnalités

### Niveau 4: Expert (projet complet)

1. Créer un podcast complet multi-épisodes
2. Automatiser la production avec scripts batch
3. Post-produire avec Audacity
4. Publier sur YouTube avec monétisation

**Objectif:** Production professionnelle

---

## 💡 CONSEILS D'ORGANISATION

### Fichiers à garder ouverts

Pendant votre utilisation, gardez ces fichiers accessibles:
- `AIDE_RAPIDE.md` - Référence rapide
- Console avec `DEMARRER_ICI.bat` - Environnement actif

### Fichiers à consulter occasionnellement

- `GUIDE_UTILISATION.md` - Quand vous cherchez des détails
- `INSTALLATION.md` - Pour le support technique

### Fichiers à ignorer

Ces fichiers sont là mais vous n'en aurez probablement pas besoin:
- `example_*.py` - Exemples officiels (anciens)
- `gradio_*.py` - Non fonctionnels (conflits)
- `pyproject.toml` - Configuration (ne pas modifier)

---

## 🆘 AIDE PAR TYPE DE BESOIN

| Besoin | Fichier(s) |
|--------|-----------|
| **Démarrage rapide** | `AIDE_RAPIDE.md` |
| **Comprendre le système** | `README_FR.md` |
| **Utilisation détaillée** | `GUIDE_UTILISATION.md` |
| **Problèmes techniques** | `INSTALLATION.md` |
| **Référence commandes** | `AIDE_RAPIDE.md` |
| **Exemples de code** | `test_*.py` |
| **Support technique** | `INSTALLATION.md` |
| **Licence et légal** | `LICENSE`, `GUIDE_UTILISATION.md` |

---

## ✅ FICHIERS ESSENTIELS - RÉSUMÉ

**Les 5 fichiers à connaître absolument:**

1. ⭐ **DEMARRER_ICI.bat** - Pour lancer
2. ⚡ **AIDE_RAPIDE.md** - Guide express
3. 🎙️ **generer_podcast.py** - Création audio
4. 📚 **GUIDE_UTILISATION.md** - Documentation complète
5. 🧪 **test_chatterbox.py** - Vérification système

**Avec seulement ces 5 fichiers, vous pouvez tout faire!**

---

**Navigation:**
- [Retour au README](README_FR.md)
- [Guide rapide](AIDE_RAPIDE.md)
- [Lancer](DEMARRER_ICI.bat)
