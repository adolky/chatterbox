# 🧪 Test des Nouvelles Fonctionnalités - v1.1

## Test 1 : Vérification du Support Multilingue

```powershell
# Tester l'import et afficher les langues
venv\Scripts\python.exe -c "from chatterbox.mtl_tts import ChatterboxMultilingualTTS, SUPPORTED_LANGUAGES; print('Langues:', list(SUPPORTED_LANGUAGES.keys()))"
```

**Résultat attendu** : Liste de 23-24 codes de langues

---

## Test 2 : Vérification du Dossier de Sauvegarde

```powershell
# Vérifier que le dossier existe
Test-Path "voix_sauvegardees"
```

**Résultat attendu** : `True`

---

## Test 3 : Lancer l'Application Complète

```powershell
# Lancer l'application avec les nouvelles fonctionnalités
venv\Scripts\python.exe gradio_tts_app.py
```

**Points à vérifier dans l'interface** :

### Interface Langue
- [ ] Menu déroulant "🌍 Langue du texte" visible
- [ ] Liste de 23+ langues disponibles
- [ ] Langue par défaut = "English (en)"

### Interface Sauvegarde de Voix
- [ ] Section "💾 Charger une voix sauvegardée" visible
- [ ] Champ de texte "📝 Nom de la voix" visible
- [ ] Bouton "💾 Sauvegarder cette voix" visible
- [ ] Message de statut de sauvegarde visible

---

## Test 4 : Test Fonctionnel Complet

### Étape 1 : Sauvegarder une Voix

1. Téléchargez un fichier audio dans "🎤 Fichier Audio de Référence"
2. Entrez un nom : "test_voice_fr"
3. Cliquez sur "💾 Sauvegarder cette voix"
4. **Vérifier** : Message "✅ Voix sauvegardée : test_voice_fr.wav"
5. **Vérifier** : Le menu déroulant se met à jour avec la nouvelle voix

### Étape 2 : Charger une Voix Sauvegardée

1. Sélectionnez "test_voice_fr.wav" dans le menu déroulant
2. **Vérifier** : Le fichier audio se charge dans le composant audio

### Étape 3 : Générer avec une Langue Spécifique

1. Sélectionnez "Français (fr)" dans le menu langue
2. Entrez du texte en français : "Bonjour, ceci est un test."
3. Cliquez sur "🎬 Générer l'Audio"
4. **Vérifier** : Audio généré avec accent français

### Étape 4 : Tester une Autre Langue

1. Sélectionnez "Espagnol (es)"
2. Entrez du texte en espagnol : "Hola, esto es una prueba."
3. Utilisez la même voix sauvegardée
4. Cliquez sur "🎬 Générer l'Audio"
5. **Vérifier** : Audio généré avec accent espagnol

---

## Test 5 : Vérification des Fichiers

```powershell
# Lister les voix sauvegardées
Get-ChildItem "voix_sauvegardees"
```

**Résultat attendu** : Liste des fichiers .wav/.mp3/.flac sauvegardés

---

## Test 6 : Test de Nommage Automatique

1. Téléchargez un fichier audio
2. **Ne remplissez pas** le champ "Nom de la voix"
3. Cliquez sur "💾 Sauvegarder cette voix"
4. **Vérifier** : Nom automatique avec format `voix_YYYYMMDD_HHMMSS.wav`

---

## Test 7 : Test de Tous les Formats

### WAV
1. Upload fichier .wav
2. Sauvegarder comme "test_wav"
3. **Vérifier** : Sauvegardé avec extension .wav

### MP3
1. Upload fichier .mp3
2. Sauvegarder comme "test_mp3"
3. **Vérifier** : Sauvegardé avec extension .mp3

### FLAC
1. Upload fichier .flac
2. Sauvegarder comme "test_flac"
3. **Vérifier** : Sauvegardé avec extension .flac

---

## Test 8 : Test de Langues Multiples

Testez avec différentes langues pour vérifier la qualité :

| Langue | Code | Texte de Test | Statut |
|--------|------|---------------|---------|
| Anglais | en | "Hello, this is a test." | [ ] |
| Français | fr | "Bonjour, ceci est un test." | [ ] |
| Espagnol | es | "Hola, esto es una prueba." | [ ] |
| Allemand | de | "Hallo, das ist ein Test." | [ ] |
| Italien | it | "Ciao, questo è un test." | [ ] |
| Japonais | ja | "こんにちは、これはテストです。" | [ ] |
| Chinois | zh | "你好，这是一个测试。" | [ ] |
| Arabe | ar | "مرحبا، هذا اختبار." | [ ] |

---

## Test 9 : Test de Robustesse

### Cas Limites

1. **Aucun nom de voix** → Doit générer nom automatique
2. **Nom très long** → Doit accepter et sauvegarder
3. **Caractères spéciaux dans le nom** → Doit gérer ou nettoyer
4. **Aucun fichier audio** → Doit afficher message d'erreur
5. **Sélection langue sans texte** → Doit afficher erreur appropriée

---

## Test 10 : Test de Performance

### Génération Longue avec Langue

1. Chargez un fichier texte de 5000+ mots
2. Sélectionnez une langue non-anglaise (ex: français)
3. Lancez la génération
4. **Vérifier** : 
   - Pas d'erreur pendant la génération
   - Qualité audio acceptable
   - Accent correct pour la langue

---

## Checklist Finale

### Fonctionnalités de Base (Conservées)
- [ ] Génération audio longue durée (1-2h+)
- [ ] Upload de fichiers texte
- [ ] Estimation de durée
- [ ] Paramètres avancés fonctionnels
- [ ] Partage Gradio actif
- [ ] Interface en français

### Nouvelles Fonctionnalités
- [ ] Sélection de langue (24 langues)
- [ ] Sauvegarde de voix avec nom personnalisé
- [ ] Sauvegarde automatique avec horodatage
- [ ] Menu déroulant de voix sauvegardées
- [ ] Chargement automatique des voix
- [ ] Support WAV, MP3, FLAC
- [ ] Mise à jour dynamique de la liste
- [ ] Dossier `voix_sauvegardees/` créé

### Interface Utilisateur
- [ ] Nouveau menu déroulant langue visible
- [ ] Section gestion des voix visible
- [ ] Messages de confirmation fonctionnels
- [ ] Interface cohérente et claire
- [ ] Aucune régression visuelle

### Documentation
- [ ] `GUIDE_LANGUES.md` créé
- [ ] `GUIDE_SAUVEGARDE_VOIX.md` créé
- [ ] `NOUVEAUTES_V1.1.md` créé
- [ ] Tous les guides à jour

---

## Rapport de Bugs (Si Applicable)

Utilisez ce template pour signaler des problèmes :

```
**Problème** : [Description courte]
**Étapes pour reproduire** :
1. [Étape 1]
2. [Étape 2]
3. [Étape 3]

**Résultat attendu** : [Ce qui devrait se passer]
**Résultat observé** : [Ce qui s'est passé]
**Logs/Erreurs** : [Copier les messages d'erreur]
**Configuration** : [OS, Python version, etc.]
```

---

## Notes de Test

**Date** : _____________  
**Testeur** : _____________  
**Version** : 1.1.0

**Commentaires généraux** :
```
[Vos observations ici]
```

**Bugs trouvés** :
```
[Liste des bugs]
```

**Améliorations suggérées** :
```
[Vos suggestions]
```

---

**Status Global** : [ ] Tous les tests passent | [ ] Quelques échecs | [ ] Tests incomplets
