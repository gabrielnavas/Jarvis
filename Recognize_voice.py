import speech_recognition as sr


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

