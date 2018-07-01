from Jarvis import *
from Bot.Bot import *
from os import system

class MyJarvis(Jarvis):
    def __init__(self, locale='pt-br', creatorName='', chatBotName='Jarvis', coeficient_confidence= 0.5):

        self.__init__(locale)
        self.creatorName = creatorName
        self.botName = chatBotName
        self.jarvisBot = Bot(chatBotName)
        self.jarvisBot.load_for_trainer()
        self.coeficient_confidence = float(coeficient_confidence)

    def get_creatorName(self):
        return self.creatorName

    def change_creator_name(self, name):
        if(len(name) > 0):
            self.creatorName = name

    def say_hello_creator(self):
        self.fala("Olá, " + self.creatorName)

    def change_coeficient_confidence(self, coef):
        if(float(coef) > 0.0):
            self.coeficient_confidence = coef
            return True

    def resposta(self, text_enter):
        resp_jarvis = self.jarvisBot.get_response(text_enter)

        if(float(resp_jarvis.confidence) > self.coeficient_confidence):
            print(resp_jarvis)
            self.fala(str(resp_jarvis))
        else:
            self.fala('Não entendi.')

    def byebye(self):
            self.fala('Até mais.')
            system.exit(0)
