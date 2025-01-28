import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
import os
import logging


#Logging
DIR_NAME = "logs"
FILE_NAME = "application.log"
log_path = os.path.join(DIR_NAME, FILE_NAME)

os.makedirs(DIR_NAME)

logging.basicConfig(
    filename=log_path,
    format = "[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level= logging.INFO
)


engine = pyttsx3.init()


def say(words):
    engine.say(words)
    engine.runAndWait()
    engine.stop()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone(device_index=0) as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        query = r.recognize_google(audio, language="en-in")
        print(f"User said {query}")

    except Exception as e:
        print("Say that again")
        return None
    
    return query


def wishMe():
    hour = datetime.datetime.now().hour
    if hour >= 5 and hour < 12:
        say("Good Morning Sir")
    elif hour >= 12 and hour < 18:
        say("Good afternoon Sir")
    else:
        say("Good evening Sir")




wishMe()

while(True):
    query = takeCommand()
    if(query is None):
        continue
    query = query.lower()
    print(query)

    if("time" in query):
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        say(f"Current time is {strTime}")

    elif("exit" in query):
        say("Bye Sir")
        break

    elif("open youtube" in query):
        say("Opening youtube")
        webbrowser.open("youtube.com")

    elif("open google" in query):
        say("Opening google")
        webbrowser.open("google.com")

    elif("wikipedia" in query):
        say("Searching wikipedia")
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        print(result)
        say(f"According to wikipedia, {result}")




