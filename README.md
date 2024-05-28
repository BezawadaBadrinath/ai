AI
this the ai project by using the python programing

Imports
python

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia as wiki 
import pyautogui as pag
import pyscreeze
import json
import requests
import openai
import pywhatkit as pwh
import smtplib
import sample
import os
These are the libraries being imported:

pyttsx3: Text-to-speech conversion library.
datetime: Library for manipulating dates and times.
speech_recognition: Library for recognizing speech.
wikipedia: Library for interacting with Wikipedia.
pyautogui: Library for GUI automation.
pyscreeze: Library for taking screenshots.
json: Library for working with JSON data.
requests: Library for making HTTP requests.
openai: Library for interacting with OpenAI API.
pywhatkit: Library for sending WhatsApp messages and other web-related tasks.
smtplib: Library for sending emails.
sample: Custom module for playing and controlling music.
os: Library for interacting with the operating system.
Initialization
python

x = pyttsx3.init()
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiOTg1ODFkMjQtYmJhOC00MDZiLTgyNjYtMjMwZmNkNjM4YTBkIiwidHlwZSI6ImFwaV90b2tlbiJ9.nQT0Pbpc8zm5HfFV8bHPqDWW8keO2XBpaMPhHqYb3XA"}
Initializes the text-to-speech engine (pyttsx3).
Sets up headers for authentication with an API.
Talk to AI Function
python

def talktoai(query):
    payload["text"] = query
    response = requests.post(url, json=payload, headers=headers)
    result = json.loads(response.text)
    speak(result['openai']['generated_text'])
Sends a query to the AI API and receives a response.
Extracts the generated text from the response and uses the speak function to vocalize it.
Speak Function
python

def speak(audio):
    x.say(audio)
    x.runAndWait()
Converts text to speech and speaks it out loud.
Time Function
python

def time():
    t = datetime.datetime.now().strftime("%H:%M:%S")
    speak(t)
Gets the current time and speaks it.
Date Function
python

def date():
    y = str(datetime.datetime.now().year)
    m = str(datetime.datetime.now().month)
    d = str(datetime.datetime.now().day)
    speak(d)
    speak(m)
    speak(y)
Gets the current date and speaks it in day, month, year format.
Wish Function
python

def wish():
    h = datetime.datetime.now().hour
    if h < 12:
        speak("Good Morning ")
    elif h >= 12 and h <= 18:
        speak("Good Afternoon ")
    elif h > 18 and h <= 21:
        speak("Good Evening")
    else:
        speak("Good Night ")
    speak("How can I help you today")
Determines the current time of day and gives an appropriate greeting.
Input Function
python

def inp():
    x1 = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        x1.pause_threshold = 1
        audio = x1.listen(source)
        try:
            print("Recognizing...")
            query = x1.recognize_google(audio, language='en-in')
            print(query)
        except Exception as e:
            print(e)
            speak("Can you repeat again")
            inp()
            return "None"
        return query
Listens to the user's speech, recognizes it, and returns it as text.
Screenshot Function
python

def screenshot():
    im1 = pyscreeze.screenshot()
    im2 = pyscreeze.screenshot('myim.png')
Takes a screenshot and saves it as 'myim.png'.
YouTube Function
python

def youtube(elem):
    pwh.playonyt(elem)
Plays a YouTube video based on the input element.
Browse Function
python

def browse(ques):
    pwh.search(ques)
Searches the web for the input query.
WhatsApp Function
python

def whatsapp(t, msg):
    pwh.sendwhatmsg_instantly(t, msg)
Sends an instant WhatsApp message to the specified number.
Send Email Function
python

def sendemail(to, msg):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('badrinathbezawada@gmail.com', 'qihy gitr eoro xubn')
    server.sendmail('narendrakumar1972@gmail.com', to, msg)
    server.close()
Sends an email using SMTP.
Main Program Logic
python

if __name__ == "__main__":
    wish()
    while True:
        query = inp().lower()
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "wikipedia" in query:
            print("I'm searching...")
            query = query.replace("wikipedia", "")
            search = wiki.summary(query, sentences=5)
            print(search)
            speak(search)
        elif "screenshot" in query:
            speak("I'm taking screenshot...")
            screenshot()
        elif "open youtube" in query:
            speak("what you want to browse ?")
            elem = inp()
            speak("opening youtube....")
            youtube(elem)
        elif "open chrome" in query:
            speak("what you want to search ?")
            ques = inp()
            speak("Browsing..")
            browse(ques)
        elif "send whatsapp" in query:
            speak("input recepient as text")
            t = input()
            speak("say what i send")
            msg = inp()
            whatsapp(t, msg)
        elif "remember" in query:
            speak("what to be remembered?")
            data = inp()
            speak("your input is" + data)
            remember = open('data.txt', 'w')
            remember.write(data)
            remember.close()
        elif "speak data" in query:
            remember = open('data.txt', 'r')
            speak("the data is stored" + remember.read())
        elif "send email" in query:
            try:
                speak("what you want to send")
                msg = input()
                speak("enter recipient email")
                to = input()
                sendemail(to, msg)
                speak("it is success")
            except Exception as e:
                print(e)
                speak("failed to send")
        elif "play a song" in query:
            song_path = input("enter the song path")
            sample.play_song(song_path)
        elif "pause the song" in query:
            sample.control("pause")
        elif "unpause" in query:
            sample.control("unpause")
        elif "play" in query:
            try:
                sample.play_song("play")
            except:
                print("please say play a song")
        elif "stop" in query:
            sample.control("stop")
        elif "exit" in query:
            speak("Exiting")
            exit()
        elif "shutdown my pc" in query:
            os.system("shutdown /s /t 1")
        elif "restart my pc" in query:
            os.system("shutdown /r /t 1")
        else:
            talktoai(query)
The main logic of the program that listens for voice commands and performs actions based on the command.
It checks for keywords in the input query and calls the corresponding function.
If no predefined command is recognized, it sends the query to the AI API and speaks out the response.
