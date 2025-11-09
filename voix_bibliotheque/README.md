# 🎤 Bibliothèque de Voix

## 📁 Structure

Placez vos fichiers audio de référence dans ce dossier pour créer votre bibliothèque de voix personnalisée.

## 🗂️ Organisation recommandée

```
voix_bibliotheque/
├── homme/
│   ├── voix_homme_neutre.wav
│   ├── voix_homme_grave.wav
│   └── voix_homme_dynamique.wav
├── femme/
│   ├── voix_femme_neutre.wav
│   ├── voix_femme_douce.wav
│   └── voix_femme_energique.wav
└── autres/
    └── voix_enfant.wav
```

## ✅ Critères pour une bonne voix de référence

**Durée optimale :** 20-30 secondes
**Format :** WAV ou MP3
**Qualité :** Propre, sans bruit de fond
**Contenu :** Phrases naturelles avec intonation variée

## 📝 Nommer vos fichiers

Utilisez des noms descriptifs :
- `voix_homme_journaliste.wav`
- `voix_femme_podcast_fr.wav`
- `voix_prof_tutoriel.wav`
- `voix_meditation_douce.wav`

## 🎙️ Où trouver des voix ?

1. **Vos propres enregistrements** (recommandé)
   - Enregistrez-vous pendant 20-30s
   - Lisez un texte naturel avec intonation

2. **Voix libres de droits**
   - OpenVoice (CC-BY-SA)
   - Common Voice (Mozilla)
   - LibriVox (domaine public)

3. **Synthèse pour bootstrap**
   - Générez une première voix avec Chatterbox
   - Utilisez-la comme référence pour la suite

## 🚀 Utilisation

### Mode interactif
```powershell
python generer_long_audio_interactive.py
# Sélectionnez "2" pour choisir dans la bibliothèque
```

### Ligne de commande
```powershell
python generer_long_audio_interactive.py \
  --texte script.txt \
  --voix voix_bibliotheque/homme/voix_homme_neutre.wav \
  --ton journaliste
```

## 📊 Voix disponibles actuellement

**Voix par défaut de Chatterbox :**
- 🤖 Voix synthétique neutre (aucune référence fournie)
- Supporte toutes les langues
- Qualité professionnelle

**Vos voix personnalisées :**
(Ajoutez vos fichiers dans ce dossier)

## 💡 Conseils

- **Testez plusieurs voix** pour trouver celle qui correspond à votre contenu
- **Créez des collections** par type de contenu (podcast, actualités, méditation)
- **Nettoyez vos enregistrements** avec Audacity avant utilisation
- **Sauvegardez vos meilleures voix** dans ce dossier

## 🔧 Maintenance

Pour lister toutes vos voix :
```powershell
python gestionnaire_voix.py --liste
```

Pour tester une voix :
```powershell
python gestionnaire_voix.py --test voix_homme_neutre.wav
```
