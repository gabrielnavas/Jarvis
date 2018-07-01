from MyJarvis import MyJarvis
from Jarvis import Jarvis
import os

class NavegadorMode():
    def __init__(self, locale='pt-br'):

        self.jarvis = Jarvis(locale)
        self.browser_default = ""
        self.__load_default_browser()

    def init(self):
        #LOOP PARA PEGAR OPCOES DITAS
        while(True):
            self.jarvis.fala('O que deseja fazer?')

            #ESCUTA PARA INICIAR OPCOES
            txt = self.jarvis.escuta()

            if(txt is not None):
                op = str(txt).lower()

                #VOLTA PARA ONDE ELE FOI CHAMADO
                if(op == 'voltar'):
                    return

                #MUDAR NAVEGADOR PADRAO
                elif(op == 'mudar navegador'
                    or op == 'mudar navegador padrão'
                    or ('mudar' in op and 'navegador' in op)):
                        self.interface__change_default_browser()

                #BOT FALA QUAL EH MEU NAVEGADOR PADRAO
                elif(op == 'qual meu navegador padrao?'
                     or ('navegador' in op and 'padrão' in op)):
                    self.falar_navegador_padrao()

                 #ABRIR NAVEGADOR JA COM SITE
                elif(op == 'abrir navegador' or ('abrir' in op and 'site' in op)):
                    self.abrir_navegador()

            #FALA QUE NAO ENTENDEU
            else:
                #self.jarvis.fala('Não entedi o que você disse.')
                pass

    def opcoes(self):
        self.jarvis.fala("""mudar navegador, 
                         'qual navegador padrao, 
                         'abrir um site, e voltar' """)

        self.jarvis.fala('escolha')

    def abrir_navegador(self):
        self.jarvis.fala('Diga o site')

        while(True):
            site = self.jarvis.escuta()

            if(site is not None):
                site = str(site).lower()
                os.system(self.browser_default + ' ' + site)
                self.jarvis.fala('Abrindo ' + site)

            else:
                self.jarvis.fala('Não entendi.')



    def get_browserName(self):
        return self.browser_default

    def falar_navegador_padrao(self):
        self.jarvis.fala('Seu navegador padrão é ' + self.get_browserName())

    def __load_default_browser(self):
        if(os.path.exists('./data/default_browser') is not True):
            os.system('touch ./data/default_browser')

        with open('./data/default_browser') as arq_default_browser:
            b_default = arq_default_browser.readline()

            # AQUI, CASO O ARQUIVO DE NAVEGADOR PADRAO ESTEJA VAZIO
            if(b_default.__len__() == 0):
                self.jarvis.fala("""Você ainda não definiu um navegador padrão.""")
                self.interface__change_default_browser()

    def interface__change_default_browser(self):
        self.jarvis.fala('Diga, qual o nome do novo navegador.')
        while(True):
            navegador = self.jarvis.escuta()

            if(navegador == None):
                self.jarvis.fala('Não entendi muito bem.')
            else:
                op = str(navegador).lower()
                #SE O AUDIO FOR VALIDO
                if(op.__len__() > 0):
                    self.__change_default_browser(op)
                else:
                    self.jarvis.fala('Não entendi muito bem.')

    def __change_default_browser(self, browser_name):
        #AQUI MUDA PARA O NAVEGADOR
        if(str(browser_name).__len__() > 0):
            #PERGUNTA SE REALMENTE QUERO MUDAR
            resp = 'Você deseja realmente mudar para ' + str(browser_name) + '?'
            self.jarvis.fala(resp)
            print(resp)

            while(True):
                op = self.jarvis.escuta()

                if(op is not None):
                    op = str(op).lower()

                    #CASO DIGO SIM
                    if(op == 'sim' or op == 'yes'):

                        self.jarvis.fala('Alterando navegador padrão.')
                        os.remove('./data/default_browser')
                        os.system('touch ./data/default_browser')
                        with open('./data/default_browser') as arq_default_browser:
                            arq_default_browser.write(str(browser_name).lower())
                        self.jarvis.fala('Alterado com sucesso')
                        return True

                    #CASO ELE ENTENDA ERRADO
                    elif( ('errado' in op) or (op == 'você entendeu errado')):
                        self.jarvis.fala('Diga novamente por favor')
                        op = self.jarvis.escuta()
                        op = op.lower()

                    #CASO DIGO NAO
                    elif (op == 'não' or op == 'no'):
                        self.jarvis.fala('Escolheu não.')
                        return False

                #CASO VENHA NONE
                else:
                    self.jarvis.fala('Não entendi.')
        return True

class MyLinuxFunctions:
    pass

class MonitorOS(MyJarvis):
    def __init__(self):
        self.modoConversa = False
        self.change_locale('pt-br')
        self.change_creator_name('Gabriel Navas')

    def init(self):
        self.fala('Ola ' + str(self.get_creatorName()))

        while(True):
            txt = self.escuta()
            print('>>' + txt)

            if(txt is not None):

                op = str(txt).lower()

                if(op == 'opções'):
                    self.options()

                elif(op == 'modo monitor'):
                    self.__modo_monitor()

                elif(op  == 'modo conversa'):
                    self.__modo_conversa_init()

                elif(op == 'sair'):
                    self.byebye()

                else:
                    self.fala('Não entendi muito bem')

            else:
                #self.fala('Não entendi muito bem')
                continue

    def options(self):
        self.fala("""modo monitor, 
                    modo conversa"""
        )

        self.fala('escolha')

    def __modo_monitor(self):
        self.fala('Iniciando modo monitor.')
        print('Iniciando modo monitor')

        while(True):
            txt = str(self.escuta())
            # txt = str(input("Say: "))

            op = str(txt).lower()
            if(op == "ativar modo conversa"):
                self.__modo_conversa()

            elif(op == "ativar modo navegador"):
                self.fala('Iniciando modo navegador.')
                print('Iniciando modo navegador.')

                # ENTRA NA CLASSE JA INICIANDO NUM LOOP PARA OPERACOES
                NavegadorMode().init(self.get_locale())

            elif (op == 'sair'):
                self.byebye()

            else:
                self.fala('Não entendi muito bem você')

    def __modo_conversa(self):
        print('iniciando modo conversa')
        self.fala('Iniciando modo conversa.')

        while (True):
            txt = str(self.escuta())
            #txt = str(input("Say: "))

            if (txt.lower() is not 'desativar modo conversa'):
                self.resposta(txt)
            else:
                self.byebye()




def main():
    MonitorOS().init()


if __name__ == '__main__':
    main()