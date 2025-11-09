# 🌍 Guide de Sélection de Langue - Chatterbox TTS

## Vue d'ensemble

L'application Chatterbox TTS supporte maintenant **24 langues différentes** pour la synthèse vocale multilingue.

## Langues Supportées

| Code | Langue | Exemple d'utilisation |
|------|--------|----------------------|
| `ar` | Arabe (Arabic) | مرحبا بك في تطبيق النص إلى كلام |
| `da` | Danois (Danish) | Velkommen til text-to-speech |
| `de` | Allemand (German) | Willkommen bei Text-zu-Sprache |
| `el` | Grec (Greek) | Καλώς ήρθατε στο κείμενο σε ομιλία |
| `en` | Anglais (English) | Welcome to text-to-speech |
| `es` | Espagnol (Spanish) | Bienvenido a texto a voz |
| `fi` | Finnois (Finnish) | Tervetuloa tekstistä puheeksi |
| `fr` | Français (French) | Bienvenue dans la synthèse vocale |
| `he` | Hébreu (Hebrew) | ברוכים הבאים לטקסט לדיבור |
| `hi` | Hindi | टेक्स्ट टू स्पीच में आपका स्वागत है |
| `it` | Italien (Italian) | Benvenuto nella sintesi vocale |
| `ja` | Japonais (Japanese) | テキスト読み上げへようこそ |
| `ko` | Coréen (Korean) | 텍스트 음성 변환에 오신 것을 환영합니다 |
| `ms` | Malais (Malay) | Selamat datang ke teks ke pertuturan |
| `nl` | Néerlandais (Dutch) | Welkom bij tekst-naar-spraak |
| `no` | Norvégien (Norwegian) | Velkommen til tekst-til-tale |
| `pl` | Polonais (Polish) | Witamy w zamianie tekstu na mowę |
| `pt` | Portugais (Portuguese) | Bem-vindo ao texto para fala |
| `ru` | Russe (Russian) | Добро пожаловать в преобразование текста в речь |
| `sv` | Suédois (Swedish) | Välkommen till text-till-tal |
| `sw` | Swahili | Karibu kwenye matini hadi usemi |
| `tr` | Turc (Turkish) | Metin okumaya hoş geldiniz |
| `zh` | Chinois (Chinese) | 欢迎使用文本转语音 |

## Comment Utiliser

### Dans l'Interface Gradio

1. **Sélectionnez la langue** dans le menu déroulant "🌍 Langue du texte"
2. Les langues sont affichées avec leur nom complet et leur code
3. Par défaut, l'anglais (`en`) est sélectionné

### Conseils pour de Meilleurs Résultats

#### ✅ Bonnes Pratiques

- **Choisissez la bonne langue** : Assurez-vous que la langue sélectionnée correspond au texte
- **Texte cohérent** : N'utilisez qu'une seule langue par génération
- **Ponctuation appropriée** : Utilisez la ponctuation adaptée à chaque langue
- **Voix de référence** : Utilisez une voix de référence dans la même langue si possible

#### ❌ À Éviter

- Mélanger plusieurs langues dans un même texte
- Utiliser une langue différente de celle du texte
- Forcer des caractères spéciaux incompatibles

## Exemples d'Utilisation

### Français
```
Langue: Français (fr)
Texte: "Bonjour, bienvenue dans notre application de synthèse vocale. 
        Cette technologie peut générer des audios de plusieurs heures."
```

### Espagnol
```
Langue: Espagnol (es)
Texte: "Hola, bienvenido a nuestra aplicación de síntesis de voz. 
        Esta tecnología puede generar audios de varias horas."
```

### Allemand
```
Langue: Allemand (de)
Texte: "Hallo, willkommen in unserer Sprachsynthese-Anwendung. 
        Diese Technologie kann mehrere Stunden Audio generieren."
```

### Japonais
```
Langue: Japonais (ja)
Texte: "こんにちは、音声合成アプリケーションへようこそ。
        このテクノロジーは数時間のオーディオを生成できます。"
```

### Arabe
```
Langue: Arabe (ar)
Texte: "مرحبًا، مرحبًا بك في تطبيق تركيب الكلام الخاص بنا.
        يمكن لهذه التقنية إنشاء صوت لعدة ساعات."
```

## Fonctionnalités Techniques

### Modèle Multilingue

L'application utilise `ChatterboxMultilingualTTS` qui :
- Supporte 24 langues nativement
- Préserve les caractéristiques prosodiques de chaque langue
- Adapte automatiquement la phonétique

### Code d'Implémentation

```python
from chatterbox.mtl_tts import ChatterboxMultilingualTTS, SUPPORTED_LANGUAGES

# Charger le modèle
model = ChatterboxMultilingualTTS.from_pretrained(DEVICE)

# Générer avec une langue spécifique
wav = model.generate(
    language_id="fr",  # Code de langue
    text="Votre texte ici",
    audio_prompt_path="reference.wav",
    # autres paramètres...
)
```

## Questions Fréquentes

### Q : Puis-je mélanger plusieurs langues ?
**R :** Non, chaque génération doit utiliser une seule langue. Pour du contenu multilingue, générez séparément chaque partie.

### Q : Quelle langue choisir pour du texte avec des mots étrangers ?
**R :** Choisissez la langue principale du texte. Les mots étrangers occasionnels seront prononcés avec l'accent de la langue principale.

### Q : La voix de référence doit-elle être dans la même langue ?
**R :** Ce n'est pas obligatoire, mais recommandé pour de meilleurs résultats. Le modèle adapte la voix à la langue cible.

### Q : Comment savoir si ma langue est bien supportée ?
**R :** Toutes les langues listées ci-dessus sont officiellement supportées. Testez avec un court texte d'abord.

## Support et Dépannage

### Problèmes Courants

1. **Accent incorrect** : Vérifiez que la langue sélectionnée correspond au texte
2. **Prononciation étrange** : Assurez-vous d'utiliser la ponctuation appropriée
3. **Erreurs de génération** : Certains caractères spéciaux peuvent nécessiter une normalisation

### Contact

Pour des questions ou problèmes spécifiques à une langue, consultez la documentation du modèle Chatterbox ou créez un issue sur GitHub.

---

**Dernière mise à jour** : Décembre 2024
**Version** : 1.0 avec support multilingue
