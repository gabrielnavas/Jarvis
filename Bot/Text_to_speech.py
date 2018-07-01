import subprocess
from gtts import gTTS

class Text_to_speech():
    """ # TUTORIAL
    https://www.smallsurething.com/text-to-speech-with-python-3-on-linux-and-osx/
    python-espeak

    Then use it like so:
    Python
    from espeak import espeak
    espeak.synth('Hello, world!')

    from espeak import espeak
    espeak.synth('Hello, world!')

    espeak  supports multiple languages, so if you are not dealing with English text, you need to pass in the language code. Unfortunately, it looks like the Python bindings don’t support that yet, but we can still use subprocess  like we did on linux.
    Python
    import subprocess

    def say_with_espeak(text, lang="en"):
        subprocess.call("espeak -v {0} {1}".format(lang, text), shell=True)

    import subprocess

    def say_with_espeak(text, lang="en"):
        subprocess.call("espeak -v {0} {1}".format(lang, text), shell=True)"""

    def __say_with_espeak(self, text, lang):
        subprocess.call("espeak -v {0} {1}".format(lang, text), shell=True)

    def __old_speak(self, text, lang="pt-br"):
        try:

            text = str(text).split(" ")

            for word in text:
                self.__say_with_espeak(word, lang)
        except:
            print("ERROR... class Text_to_speech.speak [ PRESS ENTER ]")

    def speak(self, text, lang):
        voice = gTTS(text, lang=lang)
        voice.save("voz.mp3")
        subprocess.call(['mplayer', 'voz.mp3'])

