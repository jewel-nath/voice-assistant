# ROOT_PATH and the custom-conversation file follow GassistPi by Shivasiddharth (https://github.com/shivasiddharth/GassistPi),
# MIT licence, Copyright (c) 2020 Shivasiddharth.
import pyttsx3
import os
import os.path
import yaml

ROOT_PATH = os.path.realpath(os.path.join(__file__, '..', '..'))
USER_PATH = os.path.realpath(os.path.join(__file__, '..', '..','..'))

with open('{}/config/conversation.yaml'.format(ROOT_PATH),'r', encoding='utf8') as conf:
    custom_conversation = yaml.load(conf, Loader=yaml.FullLoader)

engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
#engine.setProperty('voice', voices[1].id) #For Windows
engine.setProperty("voice", 'english+f4') #For Linux 


def speak(text):
    engine.say(text)
    engine.runAndWait()
