# 🎙️ Guide d'Utilisation - Chatterbox TTS Longue Durée

## ✨ Nouvelles Fonctionnalités

L'application Gradio Chatterbox a été améliorée pour supporter :
- ✅ **Textes illimités** (parfait pour 1-2h+ d'audio)
- ✅ **Chargement de fichiers texte** (.txt, .md, etc.)
- ✅ **Estimation automatique de la durée**
- ✅ **Interface améliorée** en français

---

## 🚀 Démarrage Rapide

### Méthode 1 : Lancer l'application

```bash
cd chatterbox
python gradio_tts_app.py
```

L'interface s'ouvrira automatiquement dans votre navigateur à l'adresse :
- **Local** : http://localhost:7860
- **Réseau** : http://0.0.0.0:7860
- **Public** : Un lien Gradio Share sera également généré

---

## 📝 Comment Utiliser

### Option 1 : Charger un fichier texte

1. Cliquez sur "📁 Option 1 : Charger un fichier texte"
2. Sélectionnez votre fichier (.txt, .md, etc.)
3. Le texte sera automatiquement chargé dans la zone de texte
4. L'estimation de durée sera mise à jour automatiquement

### Option 2 : Coller du texte directement

1. Copiez votre texte
2. Collez-le dans "✍️ Option 2 : Saisir ou coller le texte directement"
3. L'estimation de durée sera mise à jour en temps réel

---

## ⏱️ Estimations de Durée

| Durée Audio | Nombre de Mots | Nombre de Caractères (approx.) |
|-------------|----------------|----------------------------------|
| 10 minutes  | ~1,500 mots    | ~9,000 caractères                |
| 30 minutes  | ~4,500 mots    | ~27,000 caractères               |
| 1 heure     | ~9,000 mots    | ~54,000 caractères               |
| 2 heures    | ~18,000 mots   | ~108,000 caractères              |

*Basé sur un débit moyen de 150 mots/minute*

---

## 🎵 Paramètres Audio

### Paramètres Principaux

- **🎤 Fichier Audio de Référence** : Upload d'un échantillon de voix (optionnel)
- **Exagération** : Contrôle l'expressivité (0.5 = neutre)
- **CFG/Rythme** : Contrôle le rythme de la parole (0.5 recommandé)

### Paramètres Avancés

- **Graine aléatoire** : Pour reproductibilité (0 = aléatoire)
- **Température** : Contrôle la variation (0.8 recommandé)
- **min_p** : Sampler moderne (0.05 recommandé)
- **top_p** : Sampler classique (1.0 = désactivé)
- **Pénalité de répétition** : Évite les répétitions (1.2 recommandé)

---

## 💡 Conseils pour les Longs Textes

### ✅ Bonnes Pratiques

1. **Divisez en paragraphes** : Facilitez le traitement naturel
2. **Ponctuation claire** : Utilisez des points, virgules, etc.
3. **Évitez les caractères spéciaux** : Limitez les symboles complexes
4. **Testez d'abord** : Commencez avec un court extrait
5. **Patience** : Les longs textes prennent du temps à générer

### ⚠️ À Éviter

- ❌ Texte non structuré (tout en une ligne)
- ❌ Trop de caractères spéciaux
- ❌ Textes avec beaucoup de code ou formules
- ❌ Générer plusieurs audios longs simultanément

---

## 📁 Fichiers d'Exemple

Un fichier d'exemple est fourni : `exemple_texte_long.txt`

Vous pouvez :
1. Le modifier avec votre contenu
2. L'utiliser comme template
3. Créer vos propres fichiers texte

---

## 🔧 Dépannage

### L'application ne démarre pas
```bash
# Vérifiez que toutes les dépendances sont installées
pip install -r requirements.txt
```

### Erreur de mémoire pour de très longs textes
- Divisez votre texte en plusieurs fichiers
- Générez plusieurs audios séparément
- Fusionnez-les ensuite avec un outil audio

### L'estimation de durée ne se met pas à jour
- Tapez du texte ou modifiez-le légèrement
- Rechargez la page si nécessaire

---

## 🎯 Exemples d'Utilisation

### Générer un audiobook d'1 heure

1. Préparez un fichier texte de ~9,000 mots
2. Chargez-le dans l'interface
3. Vérifiez l'estimation (~1h)
4. Ajustez les paramètres si nécessaire
5. Cliquez sur "🎬 Générer l'Audio"
6. Attendez la génération (peut prendre plusieurs minutes)
7. Téléchargez l'audio généré

### Générer un podcast de 2 heures

1. Préparez un script de ~18,000 mots
2. Divisez-le en paragraphes clairs
3. Chargez dans l'interface
4. Utilisez un audio de référence pour la voix
5. Ajustez l'exagération pour plus d'expressivité
6. Générez et téléchargez

---

## 📊 Performances

- **GPU recommandé** : CUDA compatible pour génération rapide
- **CPU possible** : Mais beaucoup plus lent
- **RAM recommandée** : 8 Go minimum, 16 Go+ pour longs textes
- **Stockage** : Prévoir de l'espace pour les fichiers audio générés

---

## 🆘 Support

Pour toute question ou problème :
1. Consultez les fichiers AIDE_RAPIDE.md et GUIDE_UTILISATION.md
2. Vérifiez les logs dans le terminal
3. Testez avec un texte court d'abord

---

**Bonne génération audio ! 🎉**
