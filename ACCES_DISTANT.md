# 🌐 ACCÈS DEPUIS D'AUTRES PC - GUIDE RAPIDE

> **Comment utiliser Chatterbox depuis n'importe quel appareil**

---

## 🚀 LANCEMENT

**Sur votre PC principal (celui avec le GPU) :**

1. Double-cliquez sur : `LANCER_INTERFACE.bat`
2. Attendez 20-30 secondes
3. **Cherchez le lien public** dans la console :

```
Running on public URL: https://xxxxxxxxxxxxx.gradio.live
```

**Ce lien ressemble à :**
- `https://a1b2c3d4e5f6g7h8.gradio.live`
- Valable pendant 72 heures
- Accessible depuis n'importe où dans le monde

---

## 📱 ACCÈS DEPUIS D'AUTRES APPAREILS

### Option 1 : Lien public (recommandé)

**Depuis n'importe quel appareil :**
- Smartphone (iPhone, Android)
- Tablette (iPad, etc.)
- Autre PC (Windows, Mac, Linux)
- N'importe où dans le monde (si connecté à Internet)

**Étapes :**
1. Copiez le lien `https://xxxxx.gradio.live`
2. Ouvrez-le dans un navigateur web
3. Utilisez l'interface normalement !

### Option 2 : Réseau local (même WiFi)

**Si les appareils sont sur le même réseau WiFi :**

1. **Trouvez l'IP locale de votre PC principal :**
   ```powershell
   ipconfig
   # Cherchez "Adresse IPv4" (ex: 192.168.1.100)
   ```

2. **Sur l'autre appareil, ouvrez :**
   ```
   http://192.168.1.100:7860
   ```
   (Remplacez par votre IP)

---

## 🎯 UTILISATION

**L'interface est identique partout :**

1. **Tapez votre texte** (français, anglais, etc.)
2. **Optionnel :** Uploadez un audio de référence pour cloner une voix
3. **Ajustez les paramètres** (expression, vitesse, etc.)
4. Cliquez sur **"Generate"**
5. **Écoutez et téléchargez** le résultat !

---

## 🔒 SÉCURITÉ

### ✅ Sécurisé

- Le lien public est **aléatoire** et difficile à deviner
- **Expire après 72 heures** (automatique)
- Pas de données personnelles exposées
- Seulement la génération de voix

### 💡 Conseils

1. **Ne partagez le lien qu'avec des personnes de confiance**
2. **Fermez l'interface** quand vous ne l'utilisez plus
3. **Le lien change** à chaque redémarrage

---

## ⚡ PERFORMANCES

### Sur le PC principal (GPU)
- Génération rapide (~30s pour 100 caractères)
- GPU RTX 3060 Ti utilisé

### Sur les autres appareils
- Interface fluide
- Génération effectuée sur le PC principal
- Seulement l'interface web sur l'appareil distant
- **Pas besoin de GPU sur les appareils distants**

---

## 📊 LIMITATIONS

### Lien public Gradio

| Aspect | Limite |
|--------|--------|
| **Durée** | 72 heures maximum |
| **Utilisateurs simultanés** | ~50 personnes |
| **Taille fichiers** | Pas de limite stricte |
| **Vitesse** | Dépend de votre connexion Internet |

### Réseau local

| Aspect | Détail |
|--------|--------|
| **Portée** | Même réseau WiFi uniquement |
| **Vitesse** | Très rapide |
| **Sécurité** | Plus sécurisé (réseau privé) |

---

## 🔧 DÉPANNAGE

### ❌ Le lien public ne fonctionne pas

**Causes possibles :**
1. Le lien a expiré (>72h)
2. Le PC principal est éteint
3. L'application est fermée

**Solutions :**
- Relancez `LANCER_INTERFACE.bat`
- Un nouveau lien sera généré

---

### ❌ "Connection failed" sur appareil distant

**Solutions :**
1. Vérifiez que le PC principal est allumé
2. Vérifiez que l'interface tourne (console ouverte)
3. Rechargez la page web
4. Essayez le lien public plutôt que l'IP locale

---

### ❌ Génération très lente depuis un smartphone

**Normal !**
- La génération se fait sur votre PC principal
- Le smartphone envoie juste la requête
- Temps = temps normal + transfert réseau
- Comptez 30-60s pour 100 caractères

---

## 💡 CAS D'USAGE

### 🎬 Production YouTube

**PC principal (bureau) :**
- Génère les audios avec le GPU
- Qualité maximale

**Laptop/Tablette (canapé) :**
- Accès via lien public
- Écriture des scripts confortablement
- Génération à distance

---

### 👥 Travail collaboratif

**Vous :**
- Hébergez l'interface sur votre PC
- Partagez le lien public

**Collaborateur :**
- Accède via le lien
- Génère ses propres audios
- Pas besoin d'installation

---

### 📱 Mobile workflow

**Smartphone :**
- Écrivez vos textes en déplacement
- Générez les audios
- Téléchargez directement sur le téléphone

**PC :**
- Récupérez les fichiers pour montage
- Post-production

---

## ⚖️ LICENCE

**Tout audio généré via l'interface (locale ou distante) :**

✅ **Licence MIT** - Monétisation YouTube autorisée
✅ **Usage commercial** permis
✅ **Aucune restriction** de distribution

**Même si accédé depuis un autre PC !**

---

## 📞 SUPPORT

### Problème d'accès distant ?

1. Vérifiez que `LANCER_INTERFACE.bat` tourne
2. Cherchez le lien public dans la console
3. Testez d'abord l'accès local : `http://127.0.0.1:7860`
4. Si local fonctionne, problème réseau uniquement

### Problème de génération ?

**Indépendant de l'appareil :**
- Qualité identique (local ou distant)
- Vérifiez ponctuation, texte, etc.
- Consultez `GUIDE_UTILISATION.md`

---

## 🎉 RÉSUMÉ

✅ **Lancez une fois** sur votre PC GPU
✅ **Partagez le lien** avec qui vous voulez
✅ **Accessible partout** (monde entier)
✅ **Pas d'installation** sur les autres appareils
✅ **Même qualité** pour tous
✅ **Monétisation YouTube** autorisée

**C'est aussi simple que ça !** 🚀

---

**Fichier à lancer :** `LANCER_INTERFACE.bat`  
**Documentation complète :** `GUIDE_UTILISATION.md`  
**Interface officielle :** Resemble.AI Chatterbox
