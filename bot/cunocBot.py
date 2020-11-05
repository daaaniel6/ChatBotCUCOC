from chatterbot import  ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import pyttsx3

import logging
logging.basicConfig(filename='archivarlog.log',level=logging.DEBUG)

#VOZ
engine = pyttsx3.init()
voices = engine.getProperty('voices') #a voices se le carga un vector con la información de todas las voces
#getPropierty es para obtener información de algo, ya sea el volumen o la velocidad con que habla
engine.setProperty('voice', voices[0].id) #setProperty es para cambiar una propiedad, ya sea voz o volumen
volume = engine.getProperty('volume') #para obtener el volumen actual
engine.setProperty('volume', volume+1.0)#cambiar el volumen
rate = engine.getProperty('rate')#para obtener la velocidad actual
engine.setProperty('rate', rate-80)#cambiar la velocidad con que habla

chatbot = ChatBot('cunoc')

#chatbot.storage.drop() //borrar memoria

entrenador = ChatterBotCorpusTrainer(chatbot)
entrenador.train('chatterbot.corpus.spanish')
#C:\Users\danie\AppData\Local\Programs\Python\Python37\Lib\site-packages\chatterbot_corpus\data\spanish

while True:
    solicitud = input('Yo: ')
    respuesta = chatbot.get_response(solicitud)
    print('Bot: ', respuesta)
    engine.say(respuesta)
    engine.runAndWait()



