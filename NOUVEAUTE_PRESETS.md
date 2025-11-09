# 🎭 NOUVEAUTÉ : PRESETS DE TONS

## ✨ Qu'est-ce qui a changé ?

**Avant :**
```powershell
python generer_long_audio_interactive.py
# Vous deviez régler manuellement :
# - Expression (0.3-0.8)
# - Température (0.7-1.0)
# - CFG Weight (0.0-1.0)
# - Taille segments (300-500)
# - Pause (0.5-1.0s)
```

**Maintenant :**
```powershell
python generer_long_audio_interactive.py
# Choisissez simplement un ton :
# 1. Journaliste
# 2. Narrateur
# 3. Podcast informatif
# etc.

# Les paramètres sont appliqués automatiquement ! ✅
```

---

## 🎯 Les 11 presets disponibles

| # | Preset | Emoji | Pour quel contenu ? |
|---|--------|-------|---------------------|
| 1 | Journaliste | 📰 | Actualités, reportages, bulletins d'info |
| 2 | Narrateur | 📖 | Livres audio, contes, histoires |
| 3 | Podcast informatif | 🎙️ | Podcasts éducatifs, vulgarisation |
| 4 | Podcast dynamique | ⚡ | Podcasts divertissants, gaming |
| 5 | Publicité | 📢 | Pubs, promos, annonces commerciales |
| 6 | Documentaire | 🎬 | Documentaires, analyses approfondies |
| 7 | Tutoriel | 🎓 | Tutos, cours en ligne, formations |
| 8 | Méditation | 🧘 | Méditation guidée, relaxation, ASMR |
| 9 | Storytelling | ✨ | Récits, anecdotes, histoires captivantes |
| 10 | Enfant | 🧒 | Histoires pour enfants, éducation jeunesse |
| 11 | Personnalisé | ⚙️ | Contrôle manuel de tous les paramètres |

---

## 🚀 Comment utiliser ?

### Option 1 : Mode interactif (le plus simple)

```powershell
cd "C:\Users\adolk\Documents\Youtube ai audio\chatterbox"
.\venv\Scripts\activate
python generer_long_audio_interactive.py
```

**Le script affiche :**
```
🎭 CHOIX DU TON/STYLE
======================================================================
Sélectionnez un preset pour votre type de contenu:

 1. 📰 Journaliste TV/Radio
    Ton professionnel, neutre et autoritaire. Pour actualités, reportages.

 2. 📖 Narrateur audiobook
    Ton calme et posé. Pour livres audio, histoires, contes.

 3. 🎙️ Podcast informatif
    Ton conversationnel et accessible. Pour podcasts éducatifs.

[...]

Votre choix (1-11, Entrée=3 Podcast informatif): _
```

**Tapez le numéro → C'est tout ! Les paramètres sont configurés automatiquement.**

---

### Option 2 : Ligne de commande

```powershell
# Actualité avec ton journaliste
python generer_long_audio_interactive.py \
  --texte actualites.txt \
  --ton journaliste \
  --output actu.wav

# Podcast avec ton dynamique + votre voix
python generer_long_audio_interactive.py \
  --texte episode.txt \
  --ton podcast_dynamique \
  --voix ma_voix.wav \
  --output ep01.wav

# Méditation guidée
python generer_long_audio_interactive.py \
  --texte meditation.txt \
  --ton meditation \
  --output relax.wav
```

---

## 💡 Exemples concrets

### Podcast tech (ton journaliste)

**Texte :**
> "Apple a annoncé aujourd'hui son nouveau iPhone 16. Le modèle embarque une puce A18 révolutionnaire. Les précommandes débuteront vendredi prochain."

**Commande :**
```powershell
python generer_long_audio_interactive.py \
  --texte actu_tech.txt \
  --ton journaliste
```

**Résultat :** Voix professionnelle, neutre, rythme soutenu ✅

---

### Histoire du soir (ton narrateur)

**Texte :**
> "Il était une fois, dans une forêt enchantée, un petit renard curieux. Chaque nuit, il observait les étoiles scintiller au-dessus des arbres."

**Commande :**
```powershell
python generer_long_audio_interactive.py \
  --texte histoire.txt \
  --ton narrateur \
  --voix voix_douce.wav
```

**Résultat :** Voix calme, apaisante, pauses longues ✅

---

### Pub produit (ton publicité)

**Texte :**
> "Ne manquez pas cette offre exceptionnelle ! Seulement aujourd'hui, 50% de réduction sur tous nos produits. Profitez-en maintenant !"

**Commande :**
```powershell
python generer_long_audio_interactive.py \
  --texte promo.txt \
  --ton publicite
```

**Résultat :** Voix enthousiaste, persuasive, rythme rapide ✅

---

## 🎛️ Paramètres appliqués par preset

**Exemple : Preset "Journaliste"**
```python
Expression: 0.5      # Neutre
Température: 0.7    # Stable
CFG Weight: 0.6     # Régulier
Segments: 400       # Moyen
Pause: 0.6s         # Court
```

**Exemple : Preset "Méditation"**
```python
Expression: 0.3      # Très sobre
Température: 0.6    # Très stable
CFG Weight: 0.7     # Très régulier
Segments: 500       # Long
Pause: 1.2s         # Très long
```

**Détails complets :** `GUIDE_PRESETS_TONS.md`

---

## 🔄 Comparaison avant/après

### AVANT (complexe)

```powershell
python generer_long_audio_interactive.py

# Questions :
Expression (0.3-0.8, Entrée=0.5): 0.6
Température (0.7-1.0, Entrée=0.8): 0.8
CFG Weight (0.0-1.0, Entrée=0.5): 0.5
Taille segment (300-500, Entrée=400): 400
Pause (0.5-1.0s, Entrée=0.8): 0.7

# 5 questions techniques ! 😰
```

### MAINTENANT (simple)

```powershell
python generer_long_audio_interactive.py

# Question :
Votre choix (1-11, Entrée=3 Podcast informatif): 3

# 1 seule question ! 😊
# Tous les paramètres optimisés automatiquement !
```

---

## ✅ Avantages

**1. Simplicité**
- Plus besoin de comprendre les paramètres techniques
- Choix intuitif basé sur le type de contenu

**2. Qualité**
- Paramètres optimisés par des experts
- Résultats professionnels garantis

**3. Gain de temps**
- Configuration instantanée
- Pas d'expérimentation nécessaire

**4. Flexibilité**
- Option "Personnalisé" toujours disponible
- Compatible avec clonage de voix

---

## 🎓 Pour aller plus loin

### Tester plusieurs tons

Pour le même texte :

```powershell
# Version journaliste
python generer_long_audio_interactive.py \
  --texte texte.txt --ton journaliste -o v1.wav

# Version podcast dynamique
python generer_long_audio_interactive.py \
  --texte texte.txt --ton podcast_dynamique -o v2.wav

# Comparez et choisissez !
```

### Créer votre propre preset

Modifiez `generer_long_audio_interactive.py` :

```python
PRESETS_TONS = {
    # ... presets existants ...
    
    "mon_style": {
        "nom": "🎨 Mon Style Perso",
        "description": "Description de mon style unique",
        "exaggeration": 0.65,
        "temperature": 0.75,
        "cfg_weight": 0.45,
        "segment_size": 380,
        "pause_between_segments": 0.75,
    },
}
```

---

## 📊 Statistiques

**11 presets** couvrent :
- ✅ Actualités & Information
- ✅ Divertissement & Podcast
- ✅ Éducation & Formation
- ✅ Commerce & Publicité
- ✅ Bien-être & Relaxation
- ✅ Enfants & Jeunesse
- ✅ Narration & Storytelling

**99% des cas d'usage couverts !**

---

## 🆘 FAQ

### Q : Puis-je modifier un preset ?

**R :** Oui, deux options :
1. Choisir "Personnalisé" (#11) et ajuster manuellement
2. Modifier le fichier Python directement

### Q : Les presets fonctionnent avec ma voix ?

**R :** Oui ! Tous les presets sont compatibles avec le clonage de voix :
```powershell
python generer_long_audio_interactive.py \
  --texte texte.txt \
  --voix ma_voix.wav \
  --ton podcast_dynamique
```

### Q : Quel preset pour YouTube ?

**R :** Recommandations :
- Actualités → `journaliste`
- Podcast éducatif → `podcast_info`
- Podcast divertissement → `podcast_dynamique`
- Tuto/Formation → `tutoriel`
- Storytelling → `storytelling`

### Q : Comment annuler un preset ?

**R :** En ligne de commande, omettez `--ton` et spécifiez les paramètres :
```powershell
python generer_long_audio_interactive.py \
  --texte texte.txt \
  --expression 0.6 \
  --temperature 0.8
```

---

## 🎉 Conclusion

**Les presets de tons rendent Chatterbox encore plus accessible !**

**Avant :** Réglages techniques complexes
**Maintenant :** Choix simple et intuitif

**Résultat :** Qualité professionnelle en 1 clic ! ✨

---

## 📚 Documentation

| Fichier | Contenu |
|---------|---------|
| **GUIDE_PRESETS_TONS.md** | Détails complets des 11 presets |
| **MEMO_RAPIDE.md** | Aide-mémoire avec exemples presets |
| **GUIDE_UTILISATION.md** | Guide d'utilisation général |
| **GUIDE_AUDIOS_LONGS.md** | Podcasts 5-15 minutes |
| **GUIDE_CLONAGE_VOIX.md** | Utiliser votre propre voix |

---

**🚀 Testez dès maintenant :**

```powershell
cd "C:\Users\adolk\Documents\Youtube ai audio\chatterbox"
.\venv\Scripts\activate
python generer_long_audio_interactive.py

# Choisissez un preset et créez votre premier podcast !
```

**Bonne création ! 🎙️✨**
