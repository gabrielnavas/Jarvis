from Implementations import Jarvis

class MyJarvis(Jarvis):
    def __init__(self):
        self.my_name = ''

    def change_name(self, name):
        if(len(name) > 0):
            self.my_name = name

    def say_hello_user(self):
        self.fala("Ola" + self.my_name, "pt-br")

    def escutar_musica(self, app, endereco):
        self.fala("Um momento.", "pt-br")
        
        
    def start(self):
        
        if(self.my_name is not ''):
            self.say_hello_user()

        while(True):
            
            print("\n\nesperando voz: ")
            texto = self.escuta("pt-br")
            print(texto)

            texto = str(texto).lower()
            if('sair ' in texto):
                exit()
            
            elif(texto == 'escutar música'):
                continue
                


if __name__ == '__main__':
    jarvis = MyJarvis()
    jarvis.start()