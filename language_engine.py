from googletrans import Translator
from gtts import gTTS

translator = Translator()

def translate_telugu(text):
    translated = translator.translate(text, dest='te')
    return translated.text

def generate_voice(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    filename = "voice.mp3"
    tts.save(filename)
    return filename