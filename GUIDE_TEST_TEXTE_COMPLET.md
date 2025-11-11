# 🧪 GUIDE TEST - Texte complet après fix

**Date :** 11 novembre 2025  
**Fix appliqué :** Recompilation automatique quand `use_alignment_analyzer` change

---

## 🚀 Comment démarrer l'interface

```powershell
cd "c:\Users\adolk\Documents\Youtube ai audio\chatterbox"
.\LANCER_INTERFACE_WEB.bat
```

**OU directement :**
```powershell
cd "c:\Users\adolk\Documents\Youtube ai audio\chatterbox"
.\venv\Scripts\Activate.ps1
python gradio_tts_app.py
```

---

## 📝 Textes de test

### TEST 1 : Français (s'arrêtait à "accord")

```
Les pourparlers de paix entre le M23 et la RDC à Doha sont au point mort : quelle suite ?

Les deux camps s'accusent mutuellement de violer les termes d'un accord précédent négocié par le Qatar.

Le groupe rebelle M23 et le gouvernement de la République démocratique du Congo (RDC) n'ont pas réussi à signer l'accord de paix définitif prévu pour lundi, les rebelles accusant l'armée congolaise d'avoir enfreint un accord antérieur censé mener à un accord de paix global.
```

**Langue :** Français (fr)  
**Voix :** Votre voix clonée sauvegardée  
**Attendu :** Audio complet jusqu'à "accord de paix global."

---

### TEST 2 : Anglais (s'arrêtait à "earlier")

```
23-DR Congo peace talks in Doha stalled: What next?
Both sides accuse the other of violating the terms of an earlier deal mediated by Qatar.

The rebel group M23 and the government of the Democratic Republic of the Congo (DRC) have failed to sign a final peace accord scheduled for Monday after the rebels accused the Congolese army of breaking an earlier agreement intended to lead to a full peace deal.
```

**Langue :** English (en)  
**Voix :** Votre voix clonée sauvegardée  
**Attendu :** Audio complet jusqu'à "full peace deal."

---

## ✅ Vérifications dans la console

Pendant la génération, vous devriez voir :

```
📝 Text: XXX chars | Language: fr | Batch: 300 | Max tokens: 350 | Analyzer: DISABLED
Using ChatterboxMultilingualTTS (fr) - Unified settings
🔊 Batch 1/1: XXX chars
✅ Generated 1 batches, total: X.XXs
```

**Points critiques à vérifier :**
- ✅ `Analyzer: DISABLED` (pas `Analyzer: ENABLED`)
- ✅ `Using ChatterboxMultilingualTTS (fr)` ou `(en)` pour TOUTES les langues
- ❌ **PAS** de message `forcing EOS token` dans la console
- ❌ **PAS** de warning `detected repetition`

---

## 🎯 Résultats attendus

### Génération complète
- **Français :** Audio complet avec la phrase finale "...censé mener à un accord de paix global."
- **Anglais :** Audio complet avec la phrase finale "...intended to lead to a full peace deal."

### Performance
- **Temps :** ~12-15 minutes pour 3000 caractères (paramètres optimisés)
- **Qualité :** Excellente, sans troncature
- **Cohérence :** Mêmes paramètres pour toutes les langues

### Console propre
- Pas d'erreurs
- Pas de warnings de répétition
- Pas de messages "forcing EOS"
- Compilation automatique si nécessaire (message visible la première fois)

---

## 🔧 Si problème persiste

### 1. Vérifier que le fix est appliqué
```powershell
# Ouvrir src/chatterbox/models/t3/t3.py
# Ligne ~257, doit contenir :
needs_recompile = (
    not hasattr(self, 'compiled') or 
    not self.compiled or 
    not hasattr(self, '_last_analyzer_setting') or
    self._last_analyzer_setting != should_use_analyzer
)
```

### 2. Nettoyer le cache Python
```powershell
cd "c:\Users\adolk\Documents\Youtube ai audio\chatterbox"
Get-ChildItem -Recurse -Filter "*.pyc" | Remove-Item -Force
Get-ChildItem -Recurse -Directory -Filter "__pycache__" | Remove-Item -Recurse -Force
```

### 3. Redémarrer l'interface
Fermez complètement et relancez `LANCER_INTERFACE_WEB.bat`

---

## 📊 Comparaison avant/après

| Aspect | AVANT (bugué) | APRÈS (fixé) |
|--------|---------------|--------------|
| **Français** | S'arrête à "accord" | ✅ Complet jusqu'à la fin |
| **Anglais** | S'arrête à "earlier" | ✅ Complet jusqu'à la fin |
| **Recompilation** | ❌ Une seule fois | ✅ Auto si paramètre change |
| **Analyzer** | ❌ Parfois actif | ✅ Toujours désactivé |
| **Console** | ⚠️ Messages "forcing EOS" | ✅ Propre |
| **Performance** | ~12-15 min / 3000 chars | ~12-15 min / 3000 chars |

---

## 🎉 Confirmation du succès

Vous saurez que le fix fonctionne si :

1. ✅ Les deux textes (français ET anglais) sont générés **complètement**
2. ✅ La console affiche `Analyzer: DISABLED` pour les deux langues
3. ✅ Aucun message `forcing EOS token` n'apparaît
4. ✅ La qualité audio est excellente jusqu'à la fin
5. ✅ Le temps de génération est similaire pour français et anglais

**Bonne chance avec les tests ! 🚀**
