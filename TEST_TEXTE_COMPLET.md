# Test de génération complète - 11 novembre 2025

## Texte français qui s'arrêtait à "accord"
```
Les pourparlers de paix entre le M23 et la RDC à Doha sont au point mort : quelle suite ?

Les deux camps s'accusent mutuellement de violer les termes d'un accord précédent négocié par le Qatar.

Le groupe rebelle M23 et le gouvernement de la République démocratique du Congo (RDC) n'ont pas réussi à signer l'accord de paix définitif prévu pour lundi, les rebelles accusant l'armée congolaise d'avoir enfreint un accord antérieur censé mener à un accord de paix global.
```

**Problème :** S'arrêtait à "accord" (dernière ligne)
**Cause :** Modèle compilé UNE FOIS avec analyzer activé, jamais recompilé
**Solution :** Ajout de `needs_recompile` check basé sur `_last_analyzer_setting`

## Texte anglais qui s'arrêtait à "earlier"
```
23-DR Congo peace talks in Doha stalled: What next?
Both sides accuse the other of violating the terms of an earlier deal mediated by Qatar.

The rebel group M23 and the government of the Democratic Republic of the Congo (DRC) have failed to sign a final peace accord scheduled for Monday after the rebels accused the Congolese army of breaking an earlier agreement intended to lead to a full peace deal.
```

**Problème :** S'arrêtait à "earlier" (ligne 2)
**Cause :** Même problème que français
**Solution :** Recompilation automatique quand use_alignment_analyzer change

## Test après fix
1. Redémarrer l'interface pour forcer recompilation
2. Tester français avec ce texte
3. Tester anglais avec ce texte
4. Vérifier que les deux génèrent le texte COMPLET

## Paramètres à vérifier dans console
- `Analyzer: DISABLED` doit apparaître
- `Using ChatterboxMultilingualTTS (fr)` ou `(en)`
- Pas de message "forcing EOS token"
- Pas de warning "detected repetition"
