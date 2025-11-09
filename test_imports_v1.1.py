import gradio
from chatterbox.mtl_tts import ChatterboxMultilingualTTS, SUPPORTED_LANGUAGES
import os

print('✅ Tous les imports OK')
print(f'Gradio version: {gradio.__version__}')
print(f'Langues supportées: {len(SUPPORTED_LANGUAGES)}')
print(f'Exemples de langues: {list(SUPPORTED_LANGUAGES.items())[:5]}')
print(f'Dossier voix existe: {os.path.exists("voix_sauvegardees")}')
print('\n🎉 Application prête à être lancée!')
