import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
from python_translator import Translator
# from translate import Translator

engine = pyttsx3.init()
Globlist = ["",""]

def speak(sentence):
    engine.say(sentence)
    engine.runAndWait()

def transSlice(string):
    string = string.replace("translate from ","")
    string = string.replace("to ","")

    var = 0
    for i in string:
        if i != " ":
                var += 1
        else:
            break

    Globlist[0] = string[slice(var)]
    Globlist[1] = string.replace(Globlist[0] + " " , "")
    

def translate(lang,lang1, text):
    translator = Translator()
    results = translator.translate(text, lang, lang1)
    return results

def timeTeller():
    hour = str(datetime.datetime.now().hour)
    min = str(datetime.datetime.now().minute)
    speak("it's " + hour + "hour and " + min + "minutes")

def time():
    hour = int(datetime.datetime.now().hour)
    if hour > 0 and hour < 12:
        speak("hello, good morning sir")
    elif hour > 12 and hour < 18:
        speak("hello, good afternoon sir")
    elif hour > 18:
        speak("hello, good night sir")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query.lower()

cons = True
cons2 = True

while cons:
    if cons2:
        time()
        cons2 = False
    
    command = takeCommand()

    if 'wikipedia' in command:
            speak('Searching Wikipedia...')
            command = command.replace("wikipedia", "")
            try:
                results = wikipedia.summary(command, sentences = 3)
                speak("According to Wikipedia")
                print(results)
                speak(results)
            except wikipedia.exceptions.WikipediaException:
                speak("im sorry sir i cant find the page, please be more specific or search another topic")

    elif "google" in command:
        speak("got it, sir")
        link = command.replace("google","")
        webbrowser.open("https://duckduckgo.com/?q=" + link)
    
    elif "open youtube" in command:
        speak("got it, sir")
        webbrowser.open("youtube.com")
    
    elif "date" in command:
        day = str(datetime.datetime.now().day)
        year = str(datetime.datetime.now().year)
        month = datetime.datetime.now().month
        monthName = {
            1 : "January",
            2 : "February",
            3 : "March",
            4 : "April",
            5 : "May",
            6 : "June",
            7 : "July",
            8 : "August",
            9 : "September",
            10 : "October",
            11 : "November",
            12 : "Desember"
        }
        print("it's " + day + " " + monthName[month] + " " + year)
        speak("it's " + day + " " + monthName[month] + " " + year)

    elif "time" in command:
        timeTeller()

    elif "bmo" in command or "nemo" in  command or "mimo" in command:
        speak("yes,sir?")
        
    elif "quit" in command or "exit" in command:
        speak("See you later, sir")
        cons = False

    elif "who are you" in command:
        speak("my name is BMO, im your personal assistant")

    elif "reason to exist" in command or "why" in command:
        speak("to kill every human in this planet")
    
    elif "you" and "are" and "trash" in command:
        speak("i hope you drown")

    elif "who makes you" in command:
        speak("zaki prastiadi")

    elif "how are you" in command:
        speak("im alright sir, how about you?")
    
    elif "fine" in command or "good" in command:
        speak("it nice to hear you doing alright sir")
    
    elif "translate" in command:
        transSlice(command)
        print(translate(Globlist[1],Globlist[0],"Halo nama saya dzaky"))

    elif "calculate speed" in command:
        speak("pls enter the distance in meter sir")
        x = True
        y = True
        while x:
            try:
                dis = float(takeCommand())
                speak("enter the time in second sir")
                x = False
            except ValueError:
                speak("pardon me sir, can you repeat the distance for me again?")
        while y:
            try:
                t = float(takeCommand())
                speak("your result is "+ str(dis / t)+ " meter per second")
                y = False
            except ValueError:
                speak("pardon me sir, can you repeat the time for me again?")
