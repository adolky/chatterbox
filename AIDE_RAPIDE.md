# ⚡ AIDE RAPIDE - CHATTERBOX TTS

> **Guide de référence rapide - 2 minutes de lecture**

---

## 🚀 DÉMARRAGE EN 3 ÉTAPES

### 1. Ouvrir le terminal

Double-cliquez sur:
```
DEMARRER_ICI.bat
```

### 2. Choisir un mode

**Mode interactif** (un texte à la fois):
```bash
python generer_podcast.py
```

**Mode batch** (fichier texte):
```bash
python generer_batch.py
```

**Test rapide**:
```bash
python test_chatterbox.py
```

### 3. Générer et profiter!

Vos fichiers audio seront dans:
- `podcasts_generes/` (mode interactif)
- `podcasts_batch/` (mode batch)

---

## 📝 COMMANDES ESSENTIELLES

| Commande | Fonction |
|----------|----------|
| `python test_chatterbox.py` | Test rapide du système |
| `python generer_podcast.py` | Mode interactif |
| `python generer_batch.py` | Traitement par lot |
| `python test_multilingue.py` | Test 9 langues |
| `quit` | Quitter (dans mode interactif) |
| `help` | Aide (dans mode interactif) |

---

## 🎯 SYNTAXE DU TEXTE

### ✅ BON

```
Bonjour et bienvenue sur ma chaîne YouTube!
Aujourd'hui, nous allons découvrir l'intelligence artificielle.
N'oubliez pas de vous abonner.
À bientôt!
```

**Pourquoi ça marche:**
- ✅ Ponctuation correcte
- ✅ Phrases complètes
- ✅ Naturel et fluide

### ❌ MAUVAIS

```
Bjr et bienvenue sur ma chaine YT!
auj on va voir l'IA
abo vous
a+
```

**Pourquoi ça ne marche pas:**
- ❌ Abréviations ("Bjr", "auj", "YT")
- ❌ Pas de ponctuation
- ❌ Trop informel
- ❌ Phrases incomplètes

---

## 💡 ASTUCES RAPIDES

### Pour une meilleure qualité

1. **Écrivez les nombres en lettres**
   - ✅ "vingt-trois" 
   - ❌ "23"

2. **Ajoutez de la ponctuation**
   - ✅ "Bonjour, bienvenue!" 
   - ❌ "Bonjour bienvenue"

3. **Phrases courtes**
   - ✅ Max 150-200 caractères
   - ❌ Pas de phrases interminables

4. **Évitez les symboles**
   - ✅ "numéro un"
   - ❌ "n°1"

### Longueurs recommandées

| Type | Durée | Caractères |
|------|-------|------------|
| Intro | 10-15s | 50-80 |
| Segment | 30-60s | 150-300 |
| Conclusion | 10-15s | 50-80 |

---

## 🌍 LANGUES SUPPORTÉES

Chatterbox parle **23 langues:**

**Testées:**
- ✅ Français

**Disponibles:**
- Anglais, Espagnol, Allemand, Italien, Portugais
- Russe, Polonais, Néerlandais, Tchèque
- Chinois, Japonais, Coréen
- Hindi, Arabe, Turc, Thaï, Vietnamien
- Et plus...

**Test multilingue:**
```bash
python test_multilingue.py
```

---

## 🔧 DÉPANNAGE EXPRESS

### Problème: "CUDA non disponible"

**Test:**
```bash
python test_chatterbox.py
```

**Si GPU non détecté:**
```bash
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu124
```

### Problème: "No module named 'chatterbox'"

**Solution:**
Utilisez toujours `DEMARRER_ICI.bat`

### Problème: Audio de mauvaise qualité

**Checklist:**
- [ ] Ponctuation correcte
- [ ] Nombres en lettres
- [ ] Phrases courtes
- [ ] Pas d'abréviations

---

## ⚖️ LICENCE YOUTUBE

**AUTORISÉ ✅**
- Monétisation YouTube
- Podcasts commerciaux
- Audiolivres
- Publicités

**RECOMMANDÉ 💡**

Dans vos descriptions YouTube:
```
🎙️ Audio: Chatterbox TTS (Resemble.AI)
📜 Licence: MIT - Open Source
🔗 https://github.com/resemble-ai/chatterbox
```

---

## 📂 FICHIERS IMPORTANTS

| Fichier | Usage |
|---------|-------|
| `DEMARRER_ICI.bat` | ⭐ **LANCEUR** |
| `README_FR.md` | Vue d'ensemble |
| `GUIDE_UTILISATION.md` | Guide complet |
| `AIDE_RAPIDE.md` | Ce fichier |

---

## 🎓 WORKFLOW YOUTUBE

### 1. Écrire le script
```
[Intro 10s]
Bonjour et bienvenue!

[Contenu 2-3 min]
Aujourd'hui, nous allons voir...
Premièrement...
Deuxièmement...

[Conclusion 10s]
Merci d'avoir regardé!
Abonnez-vous!
```

### 2. Générer l'audio
```bash
python generer_podcast.py
```

### 3. Post-production
- Ouvrir dans Audacity
- Normaliser le volume
- Ajouter musique de fond (optionnel)
- Exporter en MP3 320kbps

### 4. Montage vidéo
- Synchroniser audio + vidéo
- Ajouter sous-titres (optionnel)
- Exporter

### 5. Publier!
- Upload sur YouTube
- Ajouter description avec licence MIT
- Activer la monétisation ✅

---

## 📊 PERFORMANCES

| Texte | Audio | Temps |
|-------|-------|-------|
| 50 caractères | ~4s | ~15s |
| 100 caractères | ~9s | ~30s |
| 200 caractères | ~18s | ~60s |

**Votre GPU:** RTX 3060 Ti ✅  
**VRAM:** 8GB (suffisant) ✅

---

## 🆘 AIDE

### Documentation complète
- `GUIDE_UTILISATION.md` - Tout savoir

### Support
- GitHub Issues: [lien](https://github.com/resemble-ai/chatterbox/issues)
- Site officiel: [Resemble.AI](https://www.resemble.ai/)

---

## ✅ CHECKLIST AVANT PUBLICATION

- [ ] Audio généré en 24kHz
- [ ] Licence MIT dans description
- [ ] Qualité vérifiée à l'écoute
- [ ] Pas de distorsion
- [ ] Volume normalisé
- [ ] Format: WAV ou MP3 320kbps

---

## 🎯 EXEMPLES RAPIDES

### Intro YouTube
```python
texte = """
Bonjour et bienvenue sur Tech Review!
Dans cette vidéo, nous allons découvrir Chatterbox TTS.
N'oubliez pas de liker et de vous abonner.
Allez, c'est parti!
"""
```

### Transition
```python
texte = """
Maintenant que nous avons vu les bases,
passons aux fonctionnalités avancées.
"""
```

### Conclusion + CTA
```python
texte = """
Voilà, c'est tout pour aujourd'hui!
Si vous avez aimé cette vidéo, 
pensez à liker et à vous abonner.
À très bientôt pour un nouveau tutoriel!
"""
```

---

**BON PODCAST! 🎙️**

*Chatterbox TTS - Resemble.AI*  
*Licence MIT - Commercial autorisé*

---

**Navigation rapide:**
- [Vue d'ensemble](README_FR.md)
- [Guide complet](GUIDE_UTILISATION.md)
- [Installation](INSTALLATION.md)
- [Lanceur](DEMARRER_ICI.bat)
