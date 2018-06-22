from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

class Bot():
    def __init__(self, name):      
        self.bot = ChatBot(name)
        self.bot.set_trainer(ListTrainer)

    def get_response(self, quest):
        response = self.bot.get_response(quest)
        
        if(float(response.confidence) > 0.3):
            return response
        else:
            return None    

    def load_for_trainer(self):
        arqs_list = os.listdir("Bot/learning_list/")

        for txt in arqs_list:
            print("LOADING " + txt)
            with open("Bot/learning_list/" + txt, 'r') as arq:
                list_question = []
                for question in arq:
                    list_question.append(question)
            self.bot.train(list_question)        

"""
def main():
    jarvis = Bot('Jarvis')
    jarvis.load_for_trainer()

    while(True):
        resp = str(jarvis.get_response(str(input("MY: "))))
        if(resp == 'None'):
            print('BOT: Não entendi.')
        else:
            print('BOT: '+resp)  
            
              

if __name__ == '__main__':
    main()        
"""    