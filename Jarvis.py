from Recognize_voice import Recognize_voice
from Text_to_speech import Text_to_speech

class Jarvis():
    def __init__(self, locale):
        self.locale = locale

    def escuta(self):
        rv = Recognize_voice()
        return rv.get_audio_google_recognition(self.locale)

    def fala(self, text):
        ts = Text_to_speech()
        ts.speak(text, self.locale)

    def change_locale(self, locale):
        if (len(str(locale).lower()) > 0):
            self.locale = str(locale)

    def get_locale(self):
        return self.locale