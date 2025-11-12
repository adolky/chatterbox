# 🎙️ Chatterbox TTS - Guide d'Utilisation Final

## 📌 Vue d'Ensemble

Application de synthèse vocale (Text-to-Speech) multilingue avec support de **24 langues**, optimisée pour générer des audios de longue durée (1-2h+) avec une qualité professionnelle.

---

## 🚀 Démarrage Rapide

### **1. Lancer l'application**

Double-cliquez sur : **`LANCER.bat`**

Ou ouvrez PowerShell et exécutez :
```powershell
cd "c:\Users\adolk\Documents\Youtube ai audio\chatterbox"
.\venv\Scripts\Activate.ps1
python gradio_tts_app.py
```

### **2. Accéder à l'interface**

L'application s'ouvre automatiquement dans votre navigateur à l'adresse :
```
http://localhost:7860
```

---

## 🌍 Langues Supportées (24)

| Région | Langues |
|--------|---------|
| **Europe** | 🇬🇧 Anglais • 🇫🇷 Français • 🇪🇸 Espagnol • 🇮🇹 Italien • 🇵🇹 Portugais • 🇩🇪 Allemand • 🇳🇱 Néerlandais • 🇷🇺 Russe • 🇵🇱 Polonais • 🇸🇪 Suédois • 🇳🇴 Norvégien • 🇩🇰 Danois • 🇫🇮 Finnois • 🇬🇷 Grec |
| **Asie** | 🇯🇵 Japonais • 🇨🇳 Chinois • 🇰🇷 Coréen • 🇮🇳 Hindi • 🇲🇾 Malais |
| **Moyen-Orient** | 🇸🇦 Arabe • 🇮🇱 Hébreu • 🇹🇷 Turc |
| **Afrique** | Swahili |

---

## 📝 Utilisation de l'Interface

### **Zone de Texte**
- Collez votre texte directement (jusqu'à plusieurs milliers de mots)
- **OU** utilisez le bouton "📁 Charger fichier" pour importer un fichier .txt

### **Paramètres Essentiels**

#### **1. Langue** 🌍
Sélectionnez la langue du texte à générer.
- Auto-optimisé pour chaque langue
- Paramètres spécifiques selon la complexité phonétique

#### **2. Voix (Audio Prompt)** 🎤
- **Optionnel** : Laissez vide pour la voix par défaut
- **Clonage de voix** : Uploadez un fichier audio (5-30s) de la voix à cloner

#### **3. Exagération** 🎭
- **0.0** : Neutre, monotone
- **0.5** : Équilibré (recommandé)
- **1.0** : Très expressif, dramatique

### **Options Avancées** ⚙️

#### **Max Tokens** 🚀
- **Par défaut** : 650
- **Auto-ajusté** : 500-650 selon la longueur du batch
- Plus haut = texte plus complet (mais plus lent)

#### **Taille des lots (Batch Size)** ⚡
- **Anglais** : 400 caractères
- **Français** : 280 caractères
- **Autres langues** : 250-350 caractères
- Auto-optimisé par langue

#### **Autres Paramètres**
- **Température (0.8)** : Créativité de la voix
- **min_p (0.05)** : Contrôle de la probabilité minimale
- **top_p (0.95)** : Échantillonnage nucléaire
- **Repetition Penalty (1.0)** : Évite les répétitions

---

## ⏱️ Estimation du Temps & Progression

### **Avant la Génération**
```
⏱️  ESTIMATION DE TEMPS:
   📝 Texte: 2847 caractères
   📦 Batches: 12
   ⏰ Temps estimé: 16.0 minutes (16min 0s)
   🚀 Démarrage de la génération...
```

### **Pendant la Génération**

La barre de progression affiche en temps réel :
```
🎙️ Batch 5/12 | ⏱️ 6.5min écoulées | ~9.5min restantes
⏰ Temps estimé total: 16.0 minutes
```

**Informations affichées :**
- ✅ Progression exacte (Batch actuel/Total)
- ⏱️ Temps écoulé depuis le début
- 🔮 Temps restant (recalculé dynamiquement)
- ⏰ Estimation totale (fixe)

### **Résumé Final**
```
============================================================
✅ GÉNÉRATION TERMINÉE !
============================================================
📊 Statistiques:
   ✅ Batches générés: 12/12
   🎵 Audio généré: 215.32s (3.59 min)
   ⏱️  Temps de génération: 18.45 min
   ⚡ Vitesse: 0.19x temps réel
   📝 Texte: 2847 caractères

🎯 Précision de l'estimation:
   Estimé: 16.0 min
   Réel: 18.5 min
   Précision: 115%
============================================================
```

---

## 🎯 Optimisations Appliquées

### **1. Découpage Intelligent par Phrases** ✂️
- **RÈGLE** : Ne JAMAIS couper avant un point (.)
- Chaque batch contient des phrases complètes
- Garantit qu'aucun mot n'est sauté

### **2. Tokens Dynamiques** 🎲
- **Range** : 500 (batch court) → 650 (batch long)
- Ajustement automatique selon la longueur du texte
- Maximum 650 tokens pour toutes les langues

### **3. Cleanup GPU Optimisé** 🧹
- Nettoyage mémoire tous les **8 batches** (au lieu de chaque batch)
- Gain de vitesse : ~5-10 secondes par génération
- Cleanup final à la fin pour libérer la mémoire

### **4. Optimisations par Langue** 🌍

| Langue | Max Tokens | Batch Size | Notes |
|--------|-----------|------------|-------|
| 🇬🇧 EN | 650 | 400 | Mots courts, rapide |
| 🇫🇷 FR | 650 | 280 | Liaisons complexes |
| 🇪🇸🇮🇹🇵🇹 | 650 | 350 | Langues romanes |
| 🇩🇪🇳🇱 | 650 | 320 | Mots très longs |
| 🇯🇵🇨🇳🇰🇷 | 650 | 250 | Caractères complexes |
| 🇸🇦🇮🇱 | 650 | 280 | Écriture RTL |
| 🇷🇺🇵🇱 | 650 | 300 | Déclinaisons |

---

## 📈 Performance Attendue

### **Texte Court (500 mots, ~3 min d'audio)**
- **Batches** : 8-10
- **Temps estimé** : 10-12 minutes
- **Vitesse** : ~0.3x temps réel

### **Texte Moyen (1500 mots, ~10 min d'audio)**
- **Batches** : 25-30
- **Temps estimé** : 30-35 minutes
- **Vitesse** : ~0.3x temps réel

### **Texte Long (5000 mots, ~30 min d'audio)**
- **Batches** : 80-100
- **Temps estimé** : 100-120 minutes (1h40-2h)
- **Vitesse** : ~0.25x temps réel

**Note** : Les temps varient selon votre GPU (RTX 3060/4090/etc.)

---

## 🎵 Qualité Audio

### **Caractéristiques**
- **Fréquence d'échantillonnage** : 24kHz (haute qualité)
- **Format de sortie** : WAV
- **Voix naturelle** avec intonations et émotions
- **Support du clonage de voix** pour personnalisation

### **Conseils pour Meilleure Qualité**
1. **Texte bien formaté** : Ponctuation correcte (. ! ?)
2. **Phrases complètes** : Éviter les abréviations
3. **Voix claire** pour le clonage : Audio de 10-20s minimum
4. **Exagération** : 0.3-0.7 pour narration, 0.8-1.0 pour dialogue

---

## 🔧 Dépannage

### **Problème : Texte Coupé / Mots Manquants**
✅ **Solution** : C'est corrigé ! Le système garantit maintenant :
- Découpage uniquement sur les points (.)
- Tokens suffisants (500-650)
- Phrases toujours complètes

### **Problème : Génération Trop Lente**
✅ **Solutions** :
- Réduire le batch size (mais garder > 250)
- Cleanup GPU optimisé (8 batches)
- Utiliser une GPU plus puissante

### **Problème : Erreur de Mémoire GPU**
✅ **Solutions** :
- Fermer les autres applications utilisant le GPU
- Réduire le batch size à 200-250
- Le cleanup automatique tous les 8 batches aide

### **Problème : Interface Ne S'Ouvre Pas**
✅ **Solutions** :
1. Vérifier que le port 7860 est libre
2. Relancer `LANCER.bat`
3. Ouvrir manuellement : `http://localhost:7860`

---

## 📁 Structure des Fichiers

```
chatterbox/
├── LANCER.bat                  ← Démarrer l'application
├── gradio_tts_app.py          ← Application principale
├── README.md                   ← README original du projet
├── GUIDE_FINAL.md             ← Ce guide (vous êtes ici)
├── LICENSE                     ← Licence du projet
│
├── src/chatterbox/            ← Code source du modèle
│   ├── tts.py
│   ├── mtl_tts.py
│   └── models/
│
├── venv/                       ← Environnement virtuel Python
│
├── podcasts_generes/          ← Audios générés (sauvegarde auto)
├── voix_bibliotheque/         ← Bibliothèque de voix
│   ├── homme/
│   ├── femme/
│   └── autres/
│
└── voix_sauvegardees/         ← Vos voix personnalisées
```

---

## 🎓 Exemples d'Utilisation

### **Exemple 1 : Narration Simple**
```
Texte : Article de blog (1000 mots)
Langue : Français
Voix : Par défaut
Exagération : 0.5
→ Résultat : 6-7 minutes d'audio, ~15 min de génération
```

### **Exemple 2 : Podcast avec Voix Clonée**
```
Texte : Script de podcast (3000 mots)
Langue : Anglais
Voix : Fichier audio de votre voix (15s)
Exagération : 0.7
→ Résultat : 20 minutes d'audio, ~50 min de génération
```

### **Exemple 3 : Audiobook**
```
Texte : Chapitre de livre (8000 mots)
Langue : Espagnol
Voix : Voix professionnelle
Exagération : 0.4
→ Résultat : 1 heure d'audio, ~3h de génération
```

---

## 🔐 Sécurité et Confidentialité

- **Tout est local** : Aucune donnée envoyée sur internet
- **Votre GPU** : Traitement sur votre machine uniquement
- **Fichiers audio** : Sauvegardés localement dans `podcasts_generes/`
- **Pas de tracking** : Aucune télémétrie ou analyse

---

## 📞 Support et Communauté

### **Documentation Originale**
Voir `README.md` pour les détails techniques du projet Chatterbox.

### **Problèmes Connus**
1. ✅ **Texte coupé** : RÉSOLU avec découpage par phrases complètes
2. ✅ **Mots sautés** : RÉSOLU avec tokens 500-650
3. ✅ **Génération lente** : OPTIMISÉ avec cleanup GPU réduit
4. ✅ **Progression floue** : RÉSOLU avec barre de progression précise

---

## 🎉 Fonctionnalités Principales

✅ **24 langues** supportées avec optimisations spécifiques  
✅ **Audios longs** (1-2h+) sans limitation  
✅ **Clonage de voix** pour personnalisation  
✅ **Barre de progression** en temps réel avec estimation  
✅ **Découpage intelligent** par phrases complètes  
✅ **Tokens dynamiques** (500-650) pour qualité optimale  
✅ **Cleanup GPU optimisé** pour rapidité  
✅ **Interface simple** et intuitive  
✅ **100% local** pour confidentialité  

---

## 📜 Licence

Ce projet utilise la licence spécifiée dans le fichier `LICENSE` du projet original Chatterbox.

---

## 🙏 Crédits

Application basée sur **Chatterbox TTS** avec personnalisations et optimisations pour :
- Support multilingue étendu (24 langues)
- Génération d'audios de longue durée
- Interface utilisateur améliorée
- Optimisations de performance

---

**Version Finale - 11 novembre 2025**  
**Application prête à l'emploi**

Pour démarrer : Double-cliquez sur **`LANCER.bat`** ! 🚀
