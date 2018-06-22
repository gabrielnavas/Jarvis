from Implementations import Jarvis
import time
from Bot.Bot import *

class Instructions():
    pass
    

class MyJarvis(Jarvis):
    def __init__(self):
        self.my_name = ''
        self.jarvis = Bot('Jarvis')
        self.jarvis.load_for_trainer()

    def change_name(self, name):
        if(len(name) > 0):
            self.my_name = name

    def say_hello_user(self):
        time.sleep(2)
        self.fala("Ola" + self.my_name, "pt-br")
       
    def start(self):
 
        #self.fala("CARREGANDO SISTEMA", "pt-br")  
        #time.sleep(3)

        if(self.my_name is not ''):
            self.say_hello_user()

        #self.fala("SISTEMA CARREGADO", "pt-br")
        time.sleep(5)


        while(True):
            
            print("\n\n\n\n\nDIGA ALGO....\n\n\n\n")
            texto = self.escuta("pt-br")
            
            if(texto is not None):
                print("\n\n\n\nVOCE: " + texto + "\n\n\n")

                texto = str(texto)
                if('sair' in texto.lower()):
                    self.fala("Até mais Mister" + self.my_name, "pt-br")   
                    exit()
                
                if('navegador' in texto.lower()):
                    self.fala("Abrindo navegador Mr" + self.my_name, "pt-br")
                    #fazer class

                else:
                    resp_jarvis_bot = str(self.jarvis.get_response(texto))
                    self.fala(resp_jarvis_bot, "pt-br")    


def main():
    jarvis = MyJarvis()
    jarvis.change_name("Gabriel Miguel Navas")
    jarvis.start()

if __name__ == '__main__':
    main()