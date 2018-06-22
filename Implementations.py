import speech_recognition as sr
import os
import time
import subprocess
 
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

    def speak(self, text, lang="pt-br"):
        try:
            
            text = str(text).split(" ")

            for word in text:
                self.__say_with_espeak(word, lang)
        except:
            print("ERROR... class Text_to_speech.speak [ PRESS ENTER ]")

class Recognize_voice():
    def get_audio_google_recognition(self, lang="pt-br"):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)

        # recognize speech using Google Speech Recognition
        try:
            return r.recognize_google(audio, language = lang, show_all=False)

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        return None    
        


class Jarvis():
    def __init__(self):
        self.texto = ""

    def escuta(self, lang):
        rv = Recognize_voice()
        return rv.get_audio_google_recognition(lang)   

    def fala(self, text, lang):
        ts = Text_to_speech()
        ts.speak(text, lang)   
    
    def get_txt(self):
        return self.texto

    def set_txt(self, txt):
        if(len(txt) > 0):
            self.texto = txt    

