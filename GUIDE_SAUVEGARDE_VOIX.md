# 💾 Guide de Sauvegarde des Voix Clonées

## Vue d'ensemble

L'application Chatterbox TTS permet maintenant de **sauvegarder et réutiliser les voix clonées** pour une utilisation ultérieure, sans avoir à re-télécharger le même fichier audio à chaque fois.

## Fonctionnalités

### 1. Sauvegarder une Voix

#### Méthode Simple
1. Téléchargez ou enregistrez un fichier audio de référence
2. (Optionnel) Entrez un nom pour la voix dans le champ "📝 Nom de la voix"
3. Cliquez sur "💾 Sauvegarder cette voix"
4. Un message de confirmation s'affiche : "✅ Voix sauvegardée : [nom_fichier]"

#### Nommage Automatique
- Si vous ne spécifiez pas de nom, le système génère automatiquement un nom avec horodatage
- Format : `voix_YYYYMMDD_HHMMSS.wav`
- Exemple : `voix_20241215_143522.wav`

### 2. Charger une Voix Sauvegardée

1. Cliquez sur le menu déroulant "💾 Charger une voix sauvegardée"
2. Sélectionnez la voix de votre choix
3. La voix est automatiquement chargée dans le champ audio de référence
4. Vous pouvez maintenant l'utiliser pour générer de l'audio

### 3. Organisation des Voix

Toutes les voix sont stockées dans le dossier `voix_sauvegardees/` à la racine du projet.

#### Structure
```
chatterbox/
├── gradio_tts_app.py
├── voix_sauvegardees/
│   ├── voix_homme_1.wav
│   ├── voix_femme_claire.wav
│   ├── voix_narrateur.mp3
│   ├── voix_20241215_143522.wav
│   └── ... autres voix
```

## Conseils de Nommage

### ✅ Bonnes Pratiques

#### Descriptif et Organisé
```
voix_homme_grave_30ans.wav
voix_femme_douce_soprano.wav
voix_enfant_garcon_8ans.wav
voix_narrateur_documentaire.wav
voix_personnage_robot.wav
```

#### Par Projet
```
podcast_host_principal.wav
podcast_invite_expert.wav
audiobook_narrateur_principal.wav
formation_instructeur.wav
```

#### Par Langue
```
voix_fr_homme_standard.wav
voix_en_female_american.wav
voix_es_mujer_castellano.wav
voix_de_mann_berlin.wav
```

### ❌ À Éviter

```
voice1.wav                    # Trop générique
x.wav                         # Non descriptif
mon_audio_final_v3_ok.wav    # Trop complexe
```

## Formats Supportés

L'application accepte les formats audio suivants :
- **WAV** (`.wav`) - Recommandé
- **MP3** (`.mp3`)
- **FLAC** (`.flac`)

### Format Recommandé : WAV

**Pourquoi WAV ?**
- Qualité maximale (sans perte)
- Compatibilité universelle
- Meilleure performance pour le clonage vocal

**Spécifications optimales :**
- Fréquence d'échantillonnage : 24 kHz ou 48 kHz
- Profondeur : 16-bit ou 24-bit
- Canaux : Mono ou Stéréo
- Durée : 3-10 secondes minimum

## Gestion des Voix

### Ajouter Manuellement une Voix

Vous pouvez aussi ajouter des fichiers directement dans le dossier :

```powershell
# Copier un fichier audio dans le dossier des voix
Copy-Item "C:\chemin\vers\mon_audio.wav" "c:\Users\adolk\Documents\Youtube ai audio\chatterbox\voix_sauvegardees\"
```

### Supprimer une Voix

Pour supprimer une voix sauvegardée :

```powershell
# Supprimer un fichier spécifique
Remove-Item "c:\Users\adolk\Documents\Youtube ai audio\chatterbox\voix_sauvegardees\voix_ancienne.wav"
```

### Lister les Voix Disponibles

```powershell
# Voir toutes les voix sauvegardées
Get-ChildItem "c:\Users\adolk\Documents\Youtube ai audio\chatterbox\voix_sauvegardees"
```

## Exemples d'Utilisation

### Scénario 1 : Podcast Récurrent

**Situation** : Vous créez un podcast hebdomadaire avec les mêmes voix

1. **Première fois** :
   - Enregistrez la voix de l'hôte principal
   - Sauvegardez comme `podcast_host_principal.wav`
   - Enregistrez la voix de l'invité régulier
   - Sauvegardez comme `podcast_invite_tech.wav`

2. **Episodes suivants** :
   - Sélectionnez `podcast_host_principal.wav` dans le menu
   - Générez l'intro avec cette voix
   - Sélectionnez `podcast_invite_tech.wav`
   - Générez les segments de l'invité

### Scénario 2 : Livre Audio avec Plusieurs Personnages

**Situation** : Un livre avec 3 personnages principaux

1. **Préparation** :
   ```
   personnage_jean_hero.wav
   personnage_marie_amie.wav
   personnage_dr_villain.wav
   narrateur_omniscient.wav
   ```

2. **Production** :
   - Chargez la voix appropriée selon le dialogue
   - Pas besoin de re-télécharger à chaque chapitre

### Scénario 3 : Contenu Multilingue

**Situation** : Formation dans 3 langues

1. **Voix par langue** :
   ```
   formation_fr_instructeur.wav
   formation_en_instructor.wav
   formation_es_instructor.wav
   ```

2. **Usage** :
   - Sélectionnez la langue dans "🌍 Langue du texte"
   - Chargez la voix correspondante
   - Générez le contenu

## Fonctionnalités Techniques

### Code d'Implémentation

```python
import os
import shutil
from datetime import datetime

SAVED_VOICES_DIR = "voix_sauvegardees"

def save_voice(audio_file, voice_name):
    """Sauvegarder une voix pour utilisation ultérieure"""
    if not voice_name:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        voice_name = f"voix_{timestamp}"
    
    ext = os.path.splitext(audio_file)[1]
    filename = f"{voice_name}{ext}"
    save_path = os.path.join(SAVED_VOICES_DIR, filename)
    
    shutil.copy2(audio_file, save_path)
    return f"✅ Voix sauvegardée : {filename}"

def load_saved_voice(voice_filename):
    """Charger une voix sauvegardée"""
    voice_path = os.path.join(SAVED_VOICES_DIR, voice_filename)
    if os.path.exists(voice_path):
        return voice_path
    return None
```

### Mise à Jour Dynamique

Le menu déroulant se met automatiquement à jour quand vous sauvegardez une nouvelle voix, sans avoir à recharger l'application.

## Avantages de la Sauvegarde

### ⚡ Gain de Temps
- Pas besoin de rechercher le fichier à chaque fois
- Sélection rapide dans le menu déroulant
- Workflow plus fluide

### 🎯 Cohérence
- Même voix pour tous les épisodes d'une série
- Qualité constante
- Identité sonore préservée

### 📁 Organisation
- Bibliothèque centralisée de toutes vos voix
- Nommage clair et descriptif
- Facile à gérer et à partager

### 💰 Économie
- Réutilisez les mêmes échantillons vocaux
- Moins de stockage redondant
- Partage facile entre projets

## Questions Fréquentes

### Q : Combien de voix puis-je sauvegarder ?
**R :** Autant que vous voulez ! La seule limite est l'espace disque disponible.

### Q : Les voix sauvegardées sont-elles accessibles à tous les utilisateurs ?
**R :** Oui, elles sont stockées localement sur le serveur et accessibles à tous les utilisateurs de l'application.

### Q : Puis-je partager mes voix avec d'autres ?
**R :** Oui, copiez simplement les fichiers du dossier `voix_sauvegardees/` vers un autre installation.

### Q : Que se passe-t-il si je sauvegarde deux voix avec le même nom ?
**R :** Le fichier existant sera écrasé. Utilisez des noms uniques pour éviter cela.

### Q : Les voix sauvegardées fonctionnent-elles avec toutes les langues ?
**R :** Oui, vous pouvez utiliser n'importe quelle voix sauvegardée avec n'importe quelle langue. Le modèle adapte la voix à la langue cible.

## Backup et Sécurité

### Sauvegarder Votre Bibliothèque

Il est recommandé de faire des backups réguliers de vos voix :

```powershell
# Créer une archive de toutes les voix
Compress-Archive -Path "c:\Users\adolk\Documents\Youtube ai audio\chatterbox\voix_sauvegardees\*" -DestinationPath "backup_voix_$(Get-Date -Format 'yyyyMMdd').zip"
```

### Restaurer des Voix

```powershell
# Extraire un backup
Expand-Archive -Path "backup_voix_20241215.zip" -DestinationPath "c:\Users\adolk\Documents\Youtube ai audio\chatterbox\voix_sauvegardees\"
```

## Limitations et Considérations

### Taille des Fichiers
- Les fichiers audio courts (3-10 secondes) suffisent généralement
- Des fichiers trop longs n'améliorent pas nécessairement la qualité
- Optimisez la taille pour un stockage efficace

### Qualité Audio
- Privilégiez les enregistrements sans bruit de fond
- Évitez la compression excessive (utilisez WAV si possible)
- Une bonne qualité d'entrée = meilleure qualité de sortie

### Droits d'Auteur
- Assurez-vous d'avoir les droits sur les voix que vous sauvegardez
- Ne partagez pas de voix protégées par le droit d'auteur
- Respectez la vie privée des personnes enregistrées

---

**Dernière mise à jour** : Décembre 2024
**Version** : 1.0 avec système de sauvegarde de voix
