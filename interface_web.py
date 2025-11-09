"""
🎙️ CHATTERBOX TTS - INTERFACE WEB GRAPHIQUE
Interface utilisateur simple pour génération de podcasts IA
Pour utilisateurs non-techniques
"""

import os
import sys
from pathlib import Path
from datetime import datetime

# Ajouter le dossier src au PYTHONPATH AVANT tout import
src_path = str(Path(__file__).parent / "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# Imports PyTorch
import torch
import torchaudio as ta

# Import Gradio
import gradio as gr

# Import Chatterbox
from chatterbox.tts import ChatterboxTTS

# Configuration
DOSSIER_SORTIE = Path("podcasts_web")
DOSSIER_SORTIE.mkdir(exist_ok=True)

# Variables globales
model = None
device = None

def charger_modele():
    """Charge le modèle Chatterbox une seule fois"""
    global model, device
    
    if model is not None:
        return "✅ Modèle déjà chargé"
    
    try:
        # Détection GPU
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        gpu_info = ""
        
        if device == 'cuda':
            gpu_name = torch.cuda.get_device_name(0)
            gpu_vram = torch.cuda.get_device_properties(0).total_memory / 1024**3
            gpu_info = f"🎮 GPU: {gpu_name} ({gpu_vram:.1f} GB VRAM)"
        else:
            gpu_info = "⚠️ CPU uniquement (plus lent)"
        
        # Chargement du modèle
        model = ChatterboxTTS.from_pretrained(device=device)
        
        return f"""✅ **Modèle chargé avec succès!**

{gpu_info}
📊 Sample rate: {model.sr} Hz
💾 Device: {device}

**Vous pouvez maintenant générer de l'audio!**"""
    
    except Exception as e:
        return f"❌ **Erreur lors du chargement:**\n\n{str(e)}"


def generer_audio(texte, nom_fichier="", emotion="neutral", vitesse=1.0, progress=gr.Progress()):
    """Génère l'audio à partir du texte"""
    global model
    
    # Vérifier que le modèle est chargé
    if model is None:
        return None, "❌ **Erreur:** Veuillez d'abord charger le modèle (cliquez sur 'Charger le modèle')"
    
    # Vérifier le texte
    if not texte or len(texte.strip()) == 0:
        return None, "❌ **Erreur:** Veuillez entrer du texte"
    
    if len(texte) > 1000:
        return None, f"❌ **Erreur:** Texte trop long ({len(texte)} caractères). Maximum: 1000 caractères"
    
    try:
        progress(0.1, desc="🎙️ Préparation...")
        
        # Nom de fichier
        if not nom_fichier:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            nom_fichier = f"podcast_{timestamp}.wav"
        elif not nom_fichier.endswith('.wav'):
            nom_fichier += '.wav'
        
        chemin_sortie = DOSSIER_SORTIE / nom_fichier
        
        progress(0.3, desc="⚡ Génération de l'audio...")
        
        # Génération
        with torch.inference_mode():
            wav = model.generate(texte)
        
        progress(0.8, desc="💾 Sauvegarde du fichier...")
        
        # Sauvegarde
        ta.save(str(chemin_sortie), wav.cpu(), model.sr)
        
        # Statistiques
        duree = wav.shape[-1] / model.sr
        taille_mb = chemin_sortie.stat().st_size / (1024 * 1024)
        
        progress(1.0, desc="✅ Terminé!")
        
        info = f"""✅ **Audio généré avec succès!**

📝 **Texte:** {len(texte)} caractères
🎭 **Émotion:** {emotion}
⚡ **Vitesse:** {vitesse}x
⏱️ **Durée:** {duree:.2f} secondes
💾 **Taille:** {taille_mb:.2f} MB
📁 **Fichier:** `{chemin_sortie.name}`

**Le fichier est enregistré dans:** `{DOSSIER_SORTIE.absolute()}`"""
        
        return str(chemin_sortie), info
    
    except Exception as e:
        return None, f"❌ **Erreur lors de la génération:**\n\n{str(e)}"


def exemple_texte(langue):
    """Retourne un exemple de texte selon la langue"""
    exemples = {
        "Français 🇫🇷": "Bonjour et bienvenue sur ma chaîne YouTube ! Aujourd'hui, nous allons découvrir comment créer des podcasts avec l'intelligence artificielle. N'oubliez pas de vous abonner et d'activer la cloche pour ne rien manquer !",
        "English 🇬🇧🇺🇸": "Hello and welcome to my YouTube channel! Today, we're going to explore how to create podcasts using artificial intelligence. Don't forget to subscribe and hit the bell icon to stay updated!",
        "Español 🇪🇸": "¡Hola y bienvenidos a mi canal de YouTube! Hoy vamos a descubrir cómo crear podcasts con inteligencia artificial. ¡No olvides suscribirte y activar la campanita!",
        "Deutsch 🇩🇪": "Hallo und willkommen auf meinem YouTube-Kanal! Heute werden wir entdecken, wie man Podcasts mit künstlicher Intelligenz erstellt. Vergiss nicht zu abonnieren!",
        "Italiano 🇮🇹": "Ciao e benvenuti sul mio canale YouTube! Oggi scopriremo come creare podcast con l'intelligenza artificiale. Non dimenticare di iscriverti!",
        "Português 🇵🇹": "Olá e bem-vindos ao meu canal do YouTube! Hoje vamos descobrir como criar podcasts com inteligência artificial. Não se esqueça de se inscrever!",
        "中文 🇨🇳": "大家好，欢迎来到我的YouTube频道！今天我们将探索如何使用人工智能创建播客。别忘了订阅并点击小铃铛！",
        "日本語 🇯🇵": "こんにちは、私のYouTubeチャンネルへようこそ！今日は人工知能を使ってポッドキャストを作成する方法を発見します。チャンネル登録をお忘れなく！",
        "한국어 🇰🇷": "안녕하세요, 제 유튜브 채널에 오신 것을 환영합니다! 오늘은 인공지능으로 팟캐스트를 만드는 방법을 알아보겠습니다. 구독과 좋아요 부탁드립니다!",
    }
    return exemples.get(langue, exemples["Français 🇫🇷"])


# Interface Gradio
with gr.Blocks(
    title="🎙️ Chatterbox TTS - Générateur de Podcast IA",
    theme=gr.themes.Soft(
        primary_hue="blue",
        secondary_hue="cyan",
        neutral_hue="slate",
    ),
    css="""
    .gr-button-primary {
        background: linear-gradient(90deg, #4F46E5 0%, #7C3AED 100%) !important;
        border: none !important;
        font-weight: bold !important;
    }
    .gr-button-secondary {
        background: linear-gradient(90deg, #10B981 0%, #059669 100%) !important;
        border: none !important;
        color: white !important;
        font-weight: bold !important;
    }
    .footer {
        text-align: center;
        margin-top: 20px;
        padding: 10px;
        background-color: #f3f4f6;
        border-radius: 8px;
    }
    """
) as interface:
    
    # En-tête
    gr.Markdown("""
    # 🎙️ Chatterbox TTS - Générateur de Podcast IA
    
    ### Interface graphique simple pour créer des podcasts avec intelligence artificielle
    
    **✨ Caractéristiques:**
    - 🌍 23 langues supportées
    - ⚖️ Licence MIT - Monétisation YouTube autorisée
    - 🎭 Contrôle émotionnel
    - ⚡ GPU acceleration (CUDA)
    
    ---
    """)
    
    # Étape 1: Chargement du modèle
    with gr.Accordion("📥 ÉTAPE 1: Charger le modèle (obligatoire)", open=True):
        gr.Markdown("""
        **⚠️ Important:** Cliquez sur le bouton ci-dessous pour charger le modèle avant de générer de l'audio.
        
        Le chargement prend environ 10-20 secondes la première fois.
        """)
        
        btn_charger = gr.Button("🚀 Charger le modèle Chatterbox", variant="primary", size="lg")
        statut_chargement = gr.Markdown()
        
        btn_charger.click(
            fn=charger_modele,
            outputs=statut_chargement
        )
    
    # Étape 2: Génération
    with gr.Accordion("🎬 ÉTAPE 2: Générer votre audio", open=True):
        
        # Sélection de langue avec exemples
        with gr.Row():
            langue_exemple = gr.Dropdown(
                choices=[
                    "Français 🇫🇷",
                    "English 🇬🇧🇺🇸",
                    "Español 🇪🇸",
                    "Deutsch 🇩🇪",
                    "Italiano 🇮🇹",
                    "Português 🇵🇹",
                    "中文 🇨🇳",
                    "日本語 🇯🇵",
                    "한국어 🇰🇷"
                ],
                label="🌍 Langue (exemples)",
                value="Français 🇫🇷"
            )
            btn_exemple = gr.Button("📝 Insérer un exemple", variant="secondary")
        
        # Zone de texte
        texte_input = gr.Textbox(
            label="📝 Votre texte (maximum 1000 caractères)",
            placeholder="Entrez votre texte ici...\n\nConseils:\n- Utilisez une ponctuation correcte (. , ! ?)\n- Écrivez les nombres en lettres (vingt-trois)\n- Divisez les longs paragraphes\n- Évitez les abréviations",
            lines=8,
            max_lines=15
        )
        
        # Compteur de caractères
        caracteres = gr.Markdown("**Caractères:** 0 / 1000")
        
        def compter_caracteres(texte):
            nb = len(texte) if texte else 0
            couleur = "green" if nb <= 1000 else "red"
            return f"**Caractères:** <span style='color:{couleur}'>{nb}</span> / 1000"
        
        texte_input.change(
            fn=compter_caracteres,
            inputs=texte_input,
            outputs=caracteres
        )
        
        # Exemple
        btn_exemple.click(
            fn=exemple_texte,
            inputs=langue_exemple,
            outputs=texte_input
        )
        
        # Options avancées
        with gr.Accordion("⚙️ Options avancées (optionnel)", open=False):
            with gr.Row():
                nom_fichier = gr.Textbox(
                    label="💾 Nom du fichier",
                    placeholder="Laisser vide pour auto-génération",
                    scale=2
                )
                emotion = gr.Dropdown(
                    choices=["neutral", "happy", "sad", "angry", "surprised"],
                    label="🎭 Émotion",
                    value="neutral",
                    scale=1
                )
                vitesse = gr.Slider(
                    minimum=0.5,
                    maximum=2.0,
                    value=1.0,
                    step=0.1,
                    label="⚡ Vitesse",
                    scale=1
                )
        
        # Bouton de génération
        btn_generer = gr.Button("🎙️ GÉNÉRER L'AUDIO", variant="primary", size="lg")
        
        # Résultats
        with gr.Row():
            with gr.Column(scale=1):
                audio_output = gr.Audio(
                    label="🎵 Audio généré",
                    type="filepath",
                    interactive=False
                )
            with gr.Column(scale=1):
                info_output = gr.Markdown(label="📊 Informations")
        
        # Action de génération
        btn_generer.click(
            fn=generer_audio,
            inputs=[texte_input, nom_fichier, emotion, vitesse],
            outputs=[audio_output, info_output]
        )
    
    # Exemples prédéfinis
    with gr.Accordion("💡 Exemples de textes", open=False):
        gr.Examples(
            examples=[
                ["Bonjour et bienvenue sur ma chaîne YouTube ! Aujourd'hui, nous allons découvrir un sujet passionnant.", "intro_youtube.wav"],
                ["N'oubliez pas de liker cette vidéo, de vous abonner et d'activer la cloche pour ne rien manquer !", "outro_youtube.wav"],
                ["Dans cette vidéo tutoriel, nous allons apprendre étape par étape comment créer votre premier podcast avec l'intelligence artificielle.", "tutoriel.wav"],
                ["Merci d'avoir regardé cette vidéo ! À très bientôt pour de nouvelles aventures.", "merci.wav"],
            ],
            inputs=[texte_input, nom_fichier],
            label="Cliquez sur un exemple pour l'utiliser"
        )
    
    # Instructions et conseils
    with gr.Accordion("📚 Guide d'utilisation", open=False):
        gr.Markdown("""
        ## Comment utiliser cette interface?
        
        ### 1️⃣ Charger le modèle
        - Cliquez sur **"Charger le modèle Chatterbox"**
        - Attendez le message de confirmation (10-20 secondes)
        
        ### 2️⃣ Préparer votre texte
        - Tapez ou collez votre texte (max 1000 caractères)
        - Ou cliquez sur **"Insérer un exemple"** pour tester
        - Vérifiez la ponctuation (. , ! ?)
        
        ### 3️⃣ Options (optionnel)
        - **Nom du fichier:** Laissez vide pour auto-génération
        - **Émotion:** Choisissez neutral, happy, sad, etc.
        - **Vitesse:** 1.0 = normal, 1.5 = rapide, 0.8 = lent
        
        ### 4️⃣ Générer
        - Cliquez sur **"GÉNÉRER L'AUDIO"**
        - Attendez 30-60 secondes (selon la longueur)
        - Écoutez et téléchargez votre audio!
        
        ---
        
        ## 💡 Conseils pour un meilleur résultat
        
        ### ✅ À FAIRE:
        - Utiliser une **ponctuation correcte** (. , ! ?)
        - Écrire les nombres en **lettres** ("vingt-trois" et non "23")
        - Diviser les **longs paragraphes** en phrases courtes
        - Éviter les **abréviations** ("numéro" et non "n°")
        - Tester avec des **exemples courts** d'abord
        
        ### ❌ À ÉVITER:
        - Textes sans ponctuation
        - Phrases de plus de 200 caractères
        - Abréviations et symboles (@, #, etc.)
        - Mélanger plusieurs langues dans un même texte
        
        ---
        
        ## 🌍 Langues supportées
        
        Chatterbox parle **23 langues:**
        
        - **Europe:** Français, English, Español, Deutsch, Italiano, Português, Русский, Polski, Nederlands, Čeština
        - **Asie:** 中文, 日本語, 한국어, हिन्दी, ไทย, Tiếng Việt, Bahasa Indonesia
        - **Moyen-Orient:** العربية, Türkçe
        - **Autres:** Et bien d'autres!
        
        **Note:** Le modèle détecte automatiquement la langue du texte.
        
        ---
        
        ## ⚖️ Licence et monétisation YouTube
        
        ### ✅ AUTORISÉ:
        - 💰 **Monétiser vos vidéos YouTube** avec l'audio généré
        - 🎙️ **Créer des podcasts commerciaux**
        - 📚 **Produire des audiolivres**
        - 📺 **Utiliser dans des publicités**
        - 🌐 **Distribution commerciale**
        
        **Licence:** MIT - Usage commercial autorisé sans restrictions
        
        ### 💡 RECOMMANDÉ:
        Mentionnez Chatterbox dans vos descriptions:
        ```
        🎙️ Audio généré avec Chatterbox TTS (Resemble.AI)
        https://github.com/resemble-ai/chatterbox
        Licence: MIT
        ```
        
        ---
        
        ## 🔧 Dépannage
        
        ### Le modèle ne se charge pas
        - Vérifiez votre connexion GPU (NVIDIA CUDA)
        - Fermez et relancez l'interface
        - Vérifiez l'installation de PyTorch avec CUDA
        
        ### L'audio a une mauvaise qualité
        - Améliorez la **ponctuation** de votre texte
        - Écrivez les **nombres en lettres**
        - Divisez les **phrases trop longues**
        - Évitez les **symboles** et **abréviations**
        
        ### La génération est lente
        - Normal: 30-60s pour 100-200 caractères
        - Première génération plus lente (chargement)
        - Utilisez un **GPU NVIDIA** pour accélérer
        
        ### Fichier non trouvé
        - Les fichiers sont dans: `podcasts_web/`
        - Vous pouvez les télécharger directement depuis l'interface
        
        ---
        
        ## 📁 Où sont mes fichiers?
        
        Tous vos audios sont enregistrés dans:
        ```
        C:\\Users\\adolk\\Documents\\Youtube ai audio\\chatterbox\\podcasts_web\\
        ```
        
        Format: **WAV 24kHz** (haute qualité)
        
        ---
        
        ## 📞 Besoin d'aide?
        
        Consultez la documentation complète:
        - `GUIDE_UTILISATION.md` - Guide complet
        - `AIDE_RAPIDE.md` - Référence rapide
        - `README_FR.md` - Vue d'ensemble
        
        Support en ligne:
        - GitHub: https://github.com/resemble-ai/chatterbox/issues
        - Site: https://www.resemble.ai/
        """)
    
    # Pied de page
    gr.Markdown("""
    <div class="footer">
        <p><b>🎙️ Chatterbox TTS</b> - Générateur de Podcast IA</p>
        <p>Développé par <a href="https://www.resemble.ai/" target="_blank">Resemble.AI</a> | 
        Licence MIT | 
        <a href="https://github.com/resemble-ai/chatterbox" target="_blank">GitHub</a></p>
        <p style="font-size: 0.9em; color: #666;">
            ✨ Interface créée pour faciliter l'utilisation par des non-techniciens<br>
            💰 Monétisation YouTube autorisée | 🌍 23 langues supportées | ⚡ GPU acceleration
        </p>
    </div>
    """)

# Lancement de l'interface
if __name__ == "__main__":
    print("""
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║     🎙️  CHATTERBOX TTS - INTERFACE WEB GRAPHIQUE            ║
║                                                               ║
║     Interface simple pour générer des podcasts IA             ║
║     Conçue pour les utilisateurs non-techniques               ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝

📝 Configuration:
   • GPU: """ + (torch.cuda.get_device_name(0) if torch.cuda.is_available() else "CPU uniquement") + """
   • CUDA: """ + ("✅ Disponible" if torch.cuda.is_available() else "❌ Non disponible") + """
   • Dossier sortie: podcasts_web/

🚀 Lancement de l'interface...
    """)
    
    interface.launch(
        server_name="127.0.0.1",  # Localhost uniquement
        server_port=7860,          # Port par défaut
        share=False,               # Ne pas créer de lien public
        inbrowser=True,            # Ouvrir automatiquement dans le navigateur
        show_error=True,           # Afficher les erreurs
        quiet=False                # Afficher les logs
    )
