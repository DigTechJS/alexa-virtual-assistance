passw="your password here"




import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser as wb
import os
import random
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<17:
        speak("Good AfterNoon!")
    else:
        speak("Good Evening!")
    speak("I am Alexa . Please tell me how may I help you ")


def takeCommand():
        # It takes microphone input from the user and return string output
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening😊....")
            r.pause_threshold=1
            r.energy_threshold=400
            audio=r.listen(source)
        try:
            print("Recognizing🙂...")
            query=r.recognize_google(audio,language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            # print(e)
            print("Say that again please..")
            return "None"
        return query

def sendEmail(to, content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("from@gmail.com",passw)
    server.sendmail("from@gmail.com",to,content)


if __name__ == "__main__":
    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            wb.open('http://www.youtube.com/')
        elif 'open google' in query:
            wb.open('http://www.google.com/')
        elif 'open stackoverflow' in query:
            wb.open('http://www.stackoverflow.com/')
        elif 'play music' in query:
            music_dir="C:\\Users\\hp\\Music"
            songs=os.listdir(music_dir)
            total = 0
            for item in songs:
                total += 1
            # print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randint(0,total)]))
        elif 'time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is: {strTime} ")
            print(f"The time is: {strTime} ")
        elif 'open code' in query:
            codePath="C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'email to sona' in query:
            try:
                speak("What should I say??")
                content=takeCommand()
                to="to@gmail.com"
                sendEmail(to,content)
                print("Mam, Email has been sent successfully")
                speak("Mam, Email has been sent successfully")
            except Exception as e:
                print(e)
                speak("Sorry, Shreya . I am not able to send this email at the moment.")
        elif 'quit' in query:
            print("Mam, I am quitting")
            speak("Mam, I am quitting")
            quit()

