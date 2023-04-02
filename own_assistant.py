import speech_recognition as sr
import pyttsx3
import pywhatkit 
import datetime
import wikipedia
import pyjokes
# import Py_Weather
# import google 
# from googlesearch import search



listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('\n LISTENING ...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                # print(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    # print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who the heck is' and 'what is ' in command:
        person = command.replace('who the heck is', '')
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    
    
    # elif 'what is ' in command:
    #     query = command.replace('what is', '')
    #     what = search(query, tld='co.in', lang='en', num=10, start=0, stop=None, pause=2)
    #     print(what)
    #     talk(what)
    
    
    
        
    
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'are you there' in command:
        talk('yes i am here for you')   
    elif 'eating' and 'eat' in command:
        talk('i only need power') 
    elif 'hello' in command:
        talk('hello how can i help you')
    elif 'bye' in command:
        talk('bye but i always available for you') 
    elif 'how are you' in command:
        talk('i am absolutely fine')
    elif 'what are you doing' in command:
        talk('Nothing just want to talk with you')
    
    
        
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Sorry i cannt understand')


while True:
    run_alexa()