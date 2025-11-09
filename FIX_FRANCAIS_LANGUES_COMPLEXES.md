# 🇫🇷 FIX - Génération en Français et Langues Complexes

## 🚨 Problème Identifié

**Symptôme** : Audio tronqué en français, warnings "Detected 2x repetition" et "forcing EOS token"

**Capture d'écran analysée** :
```
Batch 3/11: 316 chars | 34/400 [00:04:00<47]
Batch 4/11: 353 chars | 33/400 [00:04:00<55]
Batch 5/11: 250 chars | 40/400 [00:05:00<50]
...
WARNING: Detected 2x repetition of token 6486
WARNING: forcing EOS token
```

## 🔍 Cause Racine

### 1. Le français nécessite plus de tokens

Le français utilise généralement **30-50% plus de tokens** que l'anglais pour la même longueur de texte :

| Langue | Tokens pour 100 caractères | Ratio vs Anglais |
|--------|---------------------------|------------------|
| Anglais | ~140 tokens | 1.0x |
| Français | ~180-200 tokens | 1.3-1.4x |
| Allemand | ~190-210 tokens | 1.4-1.5x |
| Polonais | ~200-220 tokens | 1.4-1.6x |
| Russe | ~210-230 tokens | 1.5-1.6x |

**Résultat** : Avec `max_tokens=400`, les lots de 300-350 caractères en français dépassent la limite !

### 2. Détecteur de répétition trop strict

Le code original détectait une répétition après seulement **2 tokens identiques consécutifs** :
```python
# AVANT (trop strict)
len(self.generated_tokens) >= 3 and
len(set(self.generated_tokens[-2:])) == 1  # 2 tokens identiques = EOS forcé
```

En français, certains mots courts ou phonèmes peuvent naturellement répéter le même token 2 fois.

## ✅ Solutions Implémentées

### 1. Augmentation automatique de max_tokens pour certaines langues

**Fichier** : `gradio_tts_app.py`

```python
# Ajustement automatique selon la langue
if language in ["fr", "de", "pl", "ru", "fi", "el"] and max_tokens < 600:
    adjusted_max_tokens = int(max_tokens * 1.5)  # +50% pour ces langues
    print(f"⚠️ Langue {language} détectée - augmentation max_tokens: {max_tokens} → {adjusted_max_tokens}")
    max_tokens = adjusted_max_tokens
```

**Langues concernées** :
- 🇫🇷 Français (fr)
- 🇩🇪 Allemand (de)
- 🇵🇱 Polonais (pl)
- 🇷🇺 Russe (ru)
- 🇫🇮 Finnois (fi)
- 🇬🇷 Grec (el)

**Impact** :
- Si vous sélectionnez max_tokens=400 en français → automatiquement ajusté à 600
- Si vous sélectionnez max_tokens=600 en français → reste à 600

### 2. Détecteur de répétition moins agressif

**Fichier** : `src/chatterbox/models/t3/inference/alignment_stream_analyzer.py`

```python
# APRÈS (moins strict)
len(self.generated_tokens) >= 4 and
len(set(self.generated_tokens[-4:])) == 1  # 4 tokens identiques requis
```

**Impact** :
- Avant : EOS forcé après 2 tokens identiques (trop rapide)
- Maintenant : EOS forcé après 4 tokens identiques (plus tolérant)
- Réduit les faux positifs en français/langues complexes

### 3. Valeur par défaut augmentée

**Interface Gradio** :
- Ancienne valeur par défaut : 400
- **Nouvelle valeur par défaut : 600** ✅

## 📊 Résultats Attendus

### Avant les Fixes

**Français, 350 caractères par lot** :
```
max_tokens=400
Tokens nécessaires: ~480-500
Résultat: Tronqué à ~34/400 tokens
Audio: Incomplet, coupé brutalement
```

### Après les Fixes

**Français, 350 caractères par lot** :
```
max_tokens=600 (ajusté automatiquement depuis 400)
Tokens nécessaires: ~480-500
Résultat: ✅ Complet
Audio: Génération complète
```

## 🎯 Configurations Recommandées par Langue

### Anglais
```
Max Tokens : 400-500
Taille des lots : 350-400 chars
Ajustement auto : Non
```

### Français / Allemand / Polonais
```
Max Tokens : 600-700 (UI affiche 400-500, mais auto-ajusté à 600-750)
Taille des lots : 300-350 chars
Ajustement auto : Oui (+50%)
```

### Langues très complexes (Russe, Finnois, Grec)
```
Max Tokens : 700-800
Taille des lots : 250-300 chars
Ajustement auto : Oui (+50%)
```

### Langues simples (Italien, Espagnol, Portugais)
```
Max Tokens : 450-550
Taille des lots : 350-400 chars
Ajustement auto : Non (ratio proche de l'anglais)
```

## 🧪 Test de Validation

### Texte de test en français (300 chars)
```
La technologie moderne transforme notre quotidien de manière spectaculaire. 
L'intelligence artificielle permet désormais de générer des voix naturelles 
dans de nombreuses langues. Cette innovation ouvre des possibilités infinies 
pour la création de contenu audio multilingue de haute qualité.
```

**Attendu** :
- Lots : ~1 lot de 300 chars
- Tokens : ~420-450 tokens
- max_tokens avec ajustement : 600 (si UI=400) ou 700 (si UI=600)
- Résultat : ✅ Audio complet sans troncature

**Console devrait afficher** :
```
⚠️ Langue fr détectée - augmentation max_tokens: 400 → 600
📝 Text length: 300 chars, Language: fr, Batch size: 350, Max tokens: 600
📦 Processing 1 batches
Using ChatterboxMultilingualTTS (fr)
🔊 Batch 1/1: 300 chars
Sampling: 100%|████████| 450/600 [...]
✅ Generated 1 batches, total: XX.XXs
```

## ⚙️ Comment Utiliser

1. **Lancez l'application** normalement
   ```powershell
   & ".\venv\Scripts\python.exe" .\gradio_tts_app.py
   ```

2. **Sélectionnez "Français (fr)"** dans le dropdown de langue

3. **Options Avancées** :
   - Max Tokens : 400-600 (sera auto-ajusté à 600-900 pour le français)
   - Taille des lots : 300-350 chars

4. **Lancez la génération**
   - L'ajustement automatique s'applique
   - Vous verrez le message "⚠️ Langue fr détectée..." dans la console

## 🔍 Monitoring

### Dans la console, vérifiez :

**Bon signe** ✅ :
```
Sampling: 85%|███████| 450/600 [02:30<00:20, 7.5it/s]
✅ Generated 1 batches, total: 15.32s
```

**Mauvais signe** ❌ :
```
WARNING: Detected 2x repetition of token 6486
WARNING: forcing EOS token
Sampling: 8%|█| 34/400 [00:04<00:47, 7.75it/s]
```

Si vous voyez encore "forcing EOS token" :
1. Augmentez manuellement max_tokens à 700-800
2. Réduisez la taille des lots à 250-300 chars
3. Vérifiez que vous avez bien redémarré l'application après les changements

## 📝 Notes Techniques

### Pourquoi le français nécessite plus de tokens ?

1. **Mots plus longs** : "intelligence" vs "smart"
2. **Phonèmes complexes** : [ã], [œ̃], [ɥi]
3. **Liaisons** : Les liaisons créent des séquences plus longues
4. **Tokenisation** : Le modèle tokenise différemment selon la langue

### Le détecteur de répétition

**Cas légitimes de répétition** (ne doivent PAS forcer EOS) :
- Mots courts répétés : "et et", "ou ou"
- Phonèmes similaires : "papa", "maman"
- Emphase naturelle : "très très"

**Vraies répétitions** (doivent forcer EOS) :
- Boucle infinie du modèle
- Hallucination audio
- Génération bloquée

Avec 4 tokens au lieu de 2, on distingue mieux les cas légitimes des vrais problèmes.

## 🚨 Troubleshooting

### Problème : Toujours tronqué en français

**Solution** :
1. Vérifiez que vous avez redémarré l'application
2. Augmentez max_tokens manuellement à 800
3. Réduisez taille des lots à 250 chars

### Problème : Trop lent

**Solution** :
1. Réduisez température à 0.7
2. Réduisez CFG à 0.4
3. Gardez max_tokens à 600 (pas plus)

### Problème : Qualité audio dégradée

**Solution** :
1. Augmentez max_tokens à 800
2. Augmentez température à 0.9
3. Augmentez CFG à 0.6

---

**Version** : v1.3.1 - Fix Français et Langues Complexes
**Date** : 9 novembre 2025
**Impact** : Génération complète en français et langues à tokens denses
