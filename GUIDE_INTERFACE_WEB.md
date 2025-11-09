# 🌐 INTERFACE WEB GRAPHIQUE - GUIDE D'UTILISATION

> **Pour utilisateurs non-techniques** - Pas besoin de programmer !

---

## 🎯 POURQUOI UNE INTERFACE WEB?

L'interface web Gradio transforme Chatterbox en une **application facile à utiliser** :

- ✅ **Pas de ligne de commande** - Tout se fait avec des clics et des formulaires
- ✅ **Interface visuelle** - Boutons, zones de texte, lecteur audio intégré
- ✅ **Dans votre navigateur** - Chrome, Firefox, Edge, etc.
- ✅ **Simple et intuitive** - Conçue pour les débutants

---

## 🚀 LANCER L'INTERFACE WEB

### Méthode simple (recommandée)

**1. Double-cliquez sur le fichier :**

```
LANCER_INTERFACE_WEB.bat
```

**2. Attendez 20-30 secondes**
- Le chargement des bibliothèques prend du temps
- C'est normal, ne fermez pas la fenêtre !
- Vous verrez défiler du texte

**3. Votre navigateur s'ouvre automatiquement**
- L'interface apparaît dans votre navigateur web
- URL : `http://127.0.0.1:7860`
- Vous êtes prêt !

### En cas de problème

Si le navigateur ne s'ouvre pas automatiquement :

1. Regardez la fenêtre noire (console)
2. Cherchez une ligne comme : `Running on local URL:  http://127.0.0.1:7860`
3. Ouvrez votre navigateur manuellement
4. Tapez dans la barre d'adresse : `http://127.0.0.1:7860`

---

## 📋 UTILISATION DE L'INTERFACE

### ÉTAPE 1 : Charger le modèle (une seule fois)

Quand l'interface s'ouvre dans votre navigateur :

1. **Cliquez sur l'accordéon** "📥 ÉTAPE 1: Charger le modèle"
2. **Cliquez sur le gros bouton bleu** "🚀 Charger le modèle Chatterbox"
3. **Attendez 10-20 secondes** (chargement du modèle dans la mémoire GPU)
4. **Attendez le message de confirmation** : "✅ Modèle chargé avec succès!"

**Important:** Vous ne faites cette étape **qu'une seule fois** après avoir lancé l'interface.

---

### ÉTAPE 2 : Générer votre audio

Une fois le modèle chargé :

#### Option A : Utiliser un exemple (pour tester)

1. **Sélectionnez une langue** dans le menu déroulant (ex: "Français 🇫🇷")
2. **Cliquez sur "📝 Insérer un exemple"**
3. Un texte d'exemple apparaît dans la grande zone de texte
4. **Cliquez sur le gros bouton** "🎙️ GÉNÉRER L'AUDIO"
5. **Attendez 30-60 secondes** (la barre de progression vous informe)
6. **Écoutez votre audio !** Le lecteur audio apparaît automatiquement

#### Option B : Écrire votre propre texte

1. **Tapez ou collez votre texte** dans la grande zone (max 1000 caractères)
2. **Vérifiez la ponctuation** (. , ! ?)
3. **Cliquez sur "🎙️ GÉNÉRER L'AUDIO"**
4. **Attendez la génération**
5. **Écoutez et téléchargez !**

---

## ⚙️ OPTIONS AVANCÉES (OPTIONNEL)

Cliquez sur "⚙️ Options avancées" pour personnaliser :

### 💾 Nom du fichier
- **Laissez vide** : Le système génère un nom automatiquement (`podcast_20251102_123456.wav`)
- **Entrez un nom** : Par exemple `intro_episode01` (le `.wav` est ajouté automatiquement)

### 🎭 Émotion
- **neutral** : Voix neutre (par défaut)
- **happy** : Voix joyeuse
- **sad** : Voix triste
- **angry** : Voix en colère
- **surprised** : Voix surprise

### ⚡ Vitesse
- **0.5** : Très lent
- **0.8** : Lent
- **1.0** : Normal (par défaut)
- **1.2** : Rapide
- **1.5** : Très rapide
- **2.0** : Maximum

---

## 💡 EXEMPLES PRATIQUES

### Exemple 1 : Intro YouTube

```
Bonjour et bienvenue sur ma chaîne YouTube ! 
Aujourd'hui, nous allons découvrir un sujet passionnant. 
N'oubliez pas de vous abonner et d'activer la cloche !
```

**Nom du fichier:** `intro_youtube`
**Émotion:** happy
**Vitesse:** 1.0

---

### Exemple 2 : Narration documentaire

```
Au cœur de la forêt amazonienne, 
une découverte extraordinaire vient d'être faite. 
Des scientifiques ont identifié une nouvelle espèce d'insecte.
```

**Nom du fichier:** `documentaire_amazonie`
**Émotion:** neutral
**Vitesse:** 0.9 (plus lent pour bien articuler)

---

### Exemple 3 : Publicité dynamique

```
Profitez de notre offre exceptionnelle ! 
Seulement ce week-end, moins cinquante pourcent 
sur tous nos produits. Ne manquez pas cette opportunité unique !
```

**Nom du fichier:** `pub_promo`
**Émotion:** happy
**Vitesse:** 1.2 (plus rapide, énergique)

---

## 📥 TÉLÉCHARGER VOS AUDIOS

### Depuis l'interface

Après génération, un **lecteur audio** apparaît :

1. **Écoutez** en cliquant sur ▶️ (play)
2. **Téléchargez** en cliquant sur les **trois petits points** (⋮) → "Download"

### Trouver vos fichiers sur votre PC

Tous vos audios sont automatiquement enregistrés dans :

```
C:\Users\adolk\Documents\Youtube ai audio\chatterbox\podcasts_web\
```

**Format:** WAV 24kHz (haute qualité professionnelle)

---

## ✅ CONSEILS POUR UN MEILLEUR RÉSULTAT

### ✅ À FAIRE

1. **Ponctuation correcte**
   - ❌ `Bonjour bienvenue sur ma chaîne`
   - ✅ `Bonjour ! Bienvenue sur ma chaîne.`

2. **Nombres en lettres**
   - ❌ `J'ai 23 ans`
   - ✅ `J'ai vingt-trois ans`

3. **Phrases courtes**
   - ❌ Une phrase de 300 caractères sans ponctuation
   - ✅ Plusieurs phrases de 50-100 caractères avec ponctuation

4. **Éviter les abréviations**
   - ❌ `Mr. Dupont habite au n°5`
   - ✅ `Monsieur Dupont habite au numéro cinq`

### ❌ À ÉVITER

- ❌ Textes sans ponctuation
- ❌ TEXTE EN MAJUSCULES (utiliser majuscules normalement)
- ❌ Symboles spéciaux (@, #, $, etc.)
- ❌ Mélanger plusieurs langues dans un même texte
- ❌ Dépasser 1000 caractères

---

## 🌍 LANGUES SUPPORTÉES

L'interface supporte **23 langues** !

**Exemples disponibles dans le menu :**
- Français 🇫🇷
- English 🇬🇧🇺🇸
- Español 🇪🇸
- Deutsch 🇩🇪
- Italiano 🇮🇹
- Português 🇵🇹
- 中文 🇨🇳
- 日本語 🇯🇵
- 한국어 🇰🇷

**Note:** Le modèle détecte automatiquement la langue de votre texte !

---

## 🔧 DÉPANNAGE

### L'interface ne se charge pas

**Symptôme:** Le navigateur n'affiche rien ou message d'erreur

**Solutions:**
1. Attendez encore 10-20 secondes (le chargement peut être long)
2. Vérifiez la console (fenêtre noire) pour les messages
3. Relancez `LANCER_INTERFACE_WEB.bat`
4. Vérifiez que le port 7860 n'est pas déjà utilisé

---

### Le modèle ne se charge pas

**Symptôme:** Message d'erreur après avoir cliqué "Charger le modèle"

**Solutions:**
1. Vérifiez que votre GPU NVIDIA est détecté
2. Fermez et relancez l'interface
3. Vérifiez l'installation de CUDA
4. Consultez `test_chatterbox.py` pour tester l'installation

---

### L'audio a une mauvaise qualité

**Symptôme:** Voix robot, mots mal prononcés, coupures

**Solutions:**
1. **Ajoutez de la ponctuation** (. , ! ?)
2. **Écrivez les nombres en lettres**
3. **Divisez les phrases trop longues**
4. **Évitez les abréviations et symboles**
5. **Testez avec un exemple** d'abord

---

### La génération est très lente

**Symptôme:** Plus de 2 minutes pour 100 caractères

**Solutions:**
1. C'est normal la **première fois** (chargement du modèle)
2. Vérifiez que le **GPU est utilisé** (message de confirmation du modèle)
3. Fermez les autres applications qui utilisent le GPU
4. Les générations suivantes seront plus rapides

---

### Fichier audio introuvable

**Symptôme:** "Fichier sauvegardé" mais impossible de le trouver

**Solutions:**
1. Ouvrez l'explorateur Windows
2. Naviguez vers : `C:\Users\adolk\Documents\Youtube ai audio\chatterbox\podcasts_web\`
3. Triez par date de modification (les plus récents en haut)
4. Ou téléchargez directement depuis le lecteur audio de l'interface

---

## 🎬 WORKFLOW YOUTUBE COMPLET

### 1. Préparation du script

Écrivez votre script dans un document texte :
- Introduction (50-100 caractères)
- Contenu principal (par segments de 150-300 caractères)
- Conclusion (50-100 caractères)

### 2. Génération des audios

Dans l'interface web :
1. Copiez un segment de texte
2. Collez dans l'interface
3. Donnez un nom explicite (`intro`, `partie1`, `partie2`, `conclusion`)
4. Cliquez "Générer"
5. Téléchargez l'audio
6. Répétez pour chaque segment

### 3. Post-production (optionnel)

Ouvrez avec **Audacity** (gratuit) :
- Normalisez le volume
- Ajoutez de la musique de fond
- Équilibrez les fréquences
- Exportez en MP3 320kbps

### 4. Montage vidéo

Importez dans votre logiciel de montage :
- DaVinci Resolve (gratuit)
- Adobe Premiere Pro
- CapCut
- Etc.

### 5. Publication YouTube

- Upload de la vidéo
- Ajoutez la mention de licence dans la description :
  ```
  🎙️ Audio généré avec Chatterbox TTS (Resemble.AI)
  https://github.com/resemble-ai/chatterbox
  Licence: MIT - Monétisation autorisée
  ```

---

## ⚖️ MONÉTISATION YOUTUBE - C'EST LÉGAL !

### ✅ VOUS POUVEZ :

- 💰 **Monétiser vos vidéos YouTube** avec cet audio
- 🎙️ **Créer des podcasts commerciaux**
- 📚 **Vendre des audiolivres**
- 📺 **Utiliser dans des publicités**
- 🌐 **Distribution commerciale illimitée**

**Licence:** MIT - Usage commercial totalement autorisé

### 💡 RECOMMANDATION :

Mentionnez Chatterbox dans vos descriptions :

```
🎙️ Audio généré avec Chatterbox TTS (Resemble.AI)
Technologie: https://github.com/resemble-ai/chatterbox
Licence: MIT - Open Source
```

---

## 🛑 ARRÊTER L'INTERFACE

Pour fermer l'interface web :

**Méthode 1 : Fermer le navigateur**
- Fermez simplement l'onglet ou la fenêtre du navigateur
- L'interface continuera de tourner en arrière-plan

**Méthode 2 : Arrêter complètement**
- Allez dans la console (fenêtre noire)
- Appuyez sur `Ctrl + C`
- Confirmez si demandé
- Fermez la fenêtre

**Pour relancer :** Double-cliquez à nouveau sur `LANCER_INTERFACE_WEB.bat`

---

## 📞 BESOIN D'AIDE ?

### Documentation complète

- **GUIDE_UTILISATION.md** - Guide complet Chatterbox
- **AIDE_RAPIDE.md** - Référence rapide
- **README_FR.md** - Vue d'ensemble

### Support en ligne

- **GitHub Issues:** https://github.com/resemble-ai/chatterbox/issues
- **Site officiel:** https://www.resemble.ai/

---

## 🎉 BON PODCAST !

Vous avez maintenant une **interface graphique professionnelle** pour créer vos podcasts IA !

**Points clés à retenir :**

1. ✅ Lancez avec `LANCER_INTERFACE_WEB.bat`
2. ✅ Chargez le modèle (une seule fois)
3. ✅ Écrivez ou collez votre texte
4. ✅ Cliquez "Générer"
5. ✅ Téléchargez et utilisez !

**C'est aussi simple que ça !** 🎙️

---

**Créé pour faciliter l'utilisation de Chatterbox TTS**  
*Interface web Gradio - Conçue pour les utilisateurs non-techniques*  
*Monétisation YouTube autorisée - Licence MIT*
