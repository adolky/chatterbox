# FIX : Texte incomplet (tronqué prématurément)

**Date :** 11 novembre 2025  
**Problème :** Textes français et anglais s'arrêtaient au milieu (à "accord" ou "earlier")  
**Cause racine :** Modèle compilé UNE SEULE FOIS, gardant l'analyzer même quand use_alignment_analyzer=False

---

## 🔍 Symptômes observés

### Français
Texte s'arrêtait à : **"accord"**
```
...l'armée congolaise d'avoir enfreint un accord [STOP ICI]
```
Texte manquant : "antérieur censé mener à un accord de paix global."

### Anglais  
Texte s'arrêtait à : **"earlier"**
```
...violating the terms of an earlier [STOP ICI]
```
Texte manquant : "deal mediated by Qatar."

---

## 🐛 Cause racine identifiée

### Problème dans `src/chatterbox/models/t3/t3.py` (ligne 257)

```python
# AVANT LE FIX (PROBLÉMATIQUE)
self.compiled = False

if not self.compiled:
    # Compile le modèle UNE SEULE FOIS
    alignment_stream_analyzer = None
    should_use_analyzer = use_alignment_analyzer if use_alignment_analyzer is not None else self.hp.is_multilingual
    if should_use_analyzer:
        alignment_stream_analyzer = AlignmentStreamAnalyzer(...)
    
    patched_model = T3HuggingfaceBackend(..., alignment_stream_analyzer=alignment_stream_analyzer)
    self.compiled = True  # ❌ JAMAIS RECOMPILÉ ENSUITE !
```

**Scénario du bug :**
1. Premier appel : Modèle chargé AVANT notre modification → `use_alignment_analyzer=None` → Devient `True` (multilingue)
2. Analyzer créé et compilé dans le modèle
3. `self.compiled = True` → Plus jamais de recompilation
4. Appels suivants avec `use_alignment_analyzer=False` → **IGNORÉ** car `if not self.compiled` est `False`
5. L'analyzer reste actif et force l'EOS prématurément via `long_tail` ou `alignment_repetition`

---

## ✅ Solution implémentée

### Modification dans `src/chatterbox/models/t3/t3.py`

```python
# APRÈS LE FIX (CORRIGÉ)
# Default to None for English models, only create for multilingual
alignment_stream_analyzer = None
should_use_analyzer = use_alignment_analyzer if use_alignment_analyzer is not None else self.hp.is_multilingual

# Check if we need to recompile due to analyzer setting change
needs_recompile = (
    not hasattr(self, 'compiled') or 
    not self.compiled or 
    not hasattr(self, '_last_analyzer_setting') or
    self._last_analyzer_setting != should_use_analyzer  # ✅ Détecte changement !
)

if needs_recompile:  # ✅ Recompile si nécessaire
    if should_use_analyzer:
        alignment_stream_analyzer = AlignmentStreamAnalyzer(...)
    
    patched_model = T3HuggingfaceBackend(..., alignment_stream_analyzer=alignment_stream_analyzer)
    self.compiled = True
    self._last_analyzer_setting = should_use_analyzer  # ✅ Mémorise le setting
```

**Avantages :**
- ✅ Détecte si `use_alignment_analyzer` a changé depuis la dernière compilation
- ✅ Recompile automatiquement le modèle si nécessaire
- ✅ Évite les recompilations inutiles si le setting n'a pas changé
- ✅ Fonctionne même si le modèle a été chargé avant notre modification

---

## 🧪 Tests à effectuer

### 1. Texte français (qui s'arrêtait à "accord")
```
Les pourparlers de paix entre le M23 et la RDC à Doha sont au point mort : quelle suite ?

Les deux camps s'accusent mutuellement de violer les termes d'un accord précédent négocié par le Qatar.

Le groupe rebelle M23 et le gouvernement de la République démocratique du Congo (RDC) n'ont pas réussi à signer l'accord de paix définitif prévu pour lundi, les rebelles accusant l'armée congolaise d'avoir enfreint un accord antérieur censé mener à un accord de paix global.
```

**Attendu :** Génération COMPLÈTE jusqu'à "accord de paix global."

### 2. Texte anglais (qui s'arrêtait à "earlier")
```
23-DR Congo peace talks in Doha stalled: What next?
Both sides accuse the other of violating the terms of an earlier deal mediated by Qatar.

The rebel group M23 and the government of the Democratic Republic of the Congo (DRC) have failed to sign a final peace accord scheduled for Monday after the rebels accused the Congolese army of breaking an earlier agreement intended to lead to a full peace deal.
```

**Attendu :** Génération COMPLÈTE jusqu'à "full peace deal."

### 3. Vérifications dans la console
- ✅ `Analyzer: DISABLED` doit apparaître
- ✅ `Using ChatterboxMultilingualTTS (fr)` ou `(en)`
- ❌ Aucun message `forcing EOS token`
- ❌ Aucun warning de répétition

---

## 📊 Paramètres unifiés pour toutes les langues

Maintenant **TOUTES** les langues (français, anglais, et 22 autres) utilisent :

| Paramètre | Valeur | Effet |
|-----------|--------|-------|
| `use_alignment_analyzer` | `False` | ✅ Pas de détection de répétition agressive |
| `max_new_tokens` | `350` | ✅ Génération rapide ET qualité |
| `batch_size` | `300` chars | ✅ Traitement par lots optimisé |
| Modèle | `ChatterboxMultilingualTTS` | ✅ Unique pour toutes les langues |

**Avant :** Anglais → ChatterboxTTS, Autres → ChatterboxMultilingualTTS (incohérent)  
**Après :** Toutes les langues → ChatterboxMultilingualTTS avec mêmes paramètres (cohérent)

---

## 🎯 Résultat attendu

- ✅ Textes générés **complètement** sans troncature
- ✅ Performance identique pour toutes les langues (~12-15min par 3000 caractères)
- ✅ Qualité audio excellente
- ✅ Pas de messages d'erreur "forcing EOS"
- ✅ Cohérence entre français, anglais et toutes les autres langues

---

## 📝 Historique des fixes liés

1. **v1.3** - max_new_tokens configurable (1000 → 400)
2. **v1.3.1** - Seuil de répétition augmenté (2x → 6x)
3. **v1.4** - token_repetition retiré de la condition EOS
4. **v1.4** - use_alignment_analyzer=False pour français
5. **v1.4** - Unification : ChatterboxMultilingualTTS pour toutes les langues
6. **v1.4.1** (CE FIX) - Recompilation automatique quand use_alignment_analyzer change

---

## 🚀 Pour démarrer l'interface

```powershell
cd "c:\Users\adolk\Documents\Youtube ai audio\chatterbox"
.\venv\Scripts\Activate.ps1
python gradio_tts_app.py
```

L'interface sera accessible à : **http://127.0.0.1:7860**
