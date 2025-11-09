# 🎙️ Chatterbox TTS - Version Longue Durée

## ⚡ Démarrage Rapide

### Lancer l'Application

**Option 1 - Double-clic** :
```
LANCER_INTERFACE_LONGUE_DUREE.bat
```

**Option 2 - Terminal** :
```bash
python gradio_tts_app.py
```

L'interface s'ouvrira automatiquement sur : **http://localhost:7860**

---

## 🎯 Fonctionnalités Principales

### ✅ Ce Qui a Changé

| Fonctionnalité | Description |
|----------------|-------------|
| 📁 **Chargement de fichiers** | Importez des fichiers .txt, .md directement |
| 📝 **Texte illimité** | Plus de limite de caractères ! |
| ⏱️ **Estimation de durée** | Calcul automatique du temps audio |
| 🇫🇷 **Interface française** | Labels et messages en français |
| 📊 **Statistiques** | Nombre de mots et caractères |

---

## 📖 Utilisation

### Option 1 : Charger un Fichier Texte

1. Cliquez sur **"📁 Option 1 : Charger un fichier texte"**
2. Sélectionnez votre fichier (.txt, .md)
3. Le texte apparaît automatiquement
4. L'estimation de durée est calculée

### Option 2 : Copier-Coller le Texte

1. Copiez votre texte
2. Collez dans **"✍️ Option 2 : Saisir ou coller le texte"**
3. L'estimation se met à jour en temps réel

### Générer l'Audio

1. Ajustez les paramètres (optionnel)
2. Cliquez sur **"🎬 Générer l'Audio"**
3. Attendez la génération
4. Téléchargez l'audio

---

## ⏱️ Estimations

| Durée | Mots | Caractères (approx.) |
|-------|------|----------------------|
| 10 min | 1,500 | 9,000 |
| 30 min | 4,500 | 27,000 |
| 1 heure | 9,000 | 54,000 |
| 2 heures | 18,000 | 108,000 |

*Base : 150 mots/minute*

---

## 🎵 Paramètres

### Basiques
- **Audio de référence** : Échantillon de voix (optionnel)
- **Exagération** : 0.5 = neutre
- **CFG/Rythme** : 0.5 recommandé

### Avancés
- **Température** : 0.8 (variation)
- **min_p** : 0.05 (sampler moderne)
- **top_p** : 1.0 (désactivé)
- **Répétition** : 1.2 (évite les répétitions)

---

## 💡 Conseils

### ✅ Bonnes Pratiques
- Divisez en paragraphes naturels
- Utilisez une ponctuation claire
- Testez avec un court texte d'abord
- Soyez patient pour les longs textes

### ⚠️ À Éviter
- Tout en une seule ligne
- Trop de caractères spéciaux
- Code ou formules complexes

---

## 📁 Fichiers Inclus

- **`gradio_tts_app.py`** - Application principale
- **`exemple_texte_long.txt`** - Exemple de fichier texte
- **`GUIDE_AUDIO_LONGUE_DUREE.md`** - Guide détaillé
- **`MODIFICATIONS_LONGUE_DUREE.md`** - Détails techniques
- **`LANCER_INTERFACE_LONGUE_DUREE.bat`** - Lanceur rapide

---

## 🆘 Dépannage

### L'application ne démarre pas
```bash
pip install gradio torch numpy
```

### Erreur de mémoire
- Divisez le texte en plusieurs parties
- Fermez les autres applications
- Utilisez un GPU si disponible

### Audio ne se génère pas
- Vérifiez que le texte n'est pas vide
- Regardez les messages d'erreur dans le terminal
- Testez avec le texte par défaut d'abord

---

## 📞 Support

Consultez les guides :
- `GUIDE_AUDIO_LONGUE_DUREE.md` - Guide complet
- `GUIDE_UTILISATION.md` - Guide général
- `AIDE_RAPIDE.md` - Aide rapide

---

## 🎉 Exemple Complet

1. **Lancez** : Double-clic sur `LANCER_INTERFACE_LONGUE_DUREE.bat`
2. **Chargez** : `exemple_texte_long.txt`
3. **Vérifiez** : L'estimation de durée
4. **Ajustez** : Les paramètres si nécessaire
5. **Générez** : Cliquez sur le bouton
6. **Téléchargez** : Votre audio !

---

**Bon audio ! 🎙️✨**
