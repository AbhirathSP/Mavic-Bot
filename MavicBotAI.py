from click import command
import speech_recognition as sr
import pyttsx3
import pywhatkit
import pyjokes
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[6].id)

def talk(text):
  engine.say('Mavic Here')
  engine.say(text)
  engine.runAndWait()

def take_command():
 try:
     with sr.Microphone() as source:
        print('listening you.....')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'mavic' in command:
            command = command.replace('mavic', '')
            print(command)

 except:
    pass
 
 return command

def run_mavic():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        print('playing' + song)
        pywhatkit.playonyt(song)
    
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('The Time Now is' + time)

    elif 'wikipedia' in command:
        person = command.replace('wikipedia', '')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())

    else:
        talk('Come Again')

while True:
   run_mavic()