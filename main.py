from http import server
import random
import wikipedia
import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<=12):
        speak("Good morning!")
    elif(hour>12 and hour<=16):
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("Hello, I am Jarvis . Please tell me how may I  help you")
    
def takeComand():
    # It takes microphone input from user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening ......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing ......")
        query = r.recognize_google(audio, language= 'eng-in')
        print(f"User said : {query}\n")
    except Exception as e:
        # print(e) # Print error 
        print("Say that again please .....")
        return "None"
    return query

def sendMail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('nitin8824533145@gmail.com', 'Nk@01052020')
    server.sendmail('nitin8824533145@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    # speak("Hii, My name is ZIRA.")
    wishMe()
    # takeComand()

    while(True):
        query = takeComand().lower()
        # Logics for executing tasks based on query
        if 'wikipedia' in query:
            speak("Seaeching Wikipedia .....")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences = 3)
            speak("According to wikipedia")
            print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open brave' in query:
            webbrowser.open("brave.com")

        elif 'music'in query:
            music_dir = 'E:\\Recover\\Music'
            songs = os.listdir(music_dir)
            # print(songs)
            songNumer = random.randint(0, len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[songNumer]))
            print(f"Song {str(songs[songNumer])} is playing ....")
        elif 'next' in query:
            music_dir = 'E:\\Recover\\Music'
            songs = os.listdir(music_dir)
            # print(songs)
            songNumer = random.randint(0, len(songs)-1)
            os.startfile(os.path.join(music_dir, songs[songNumer+1]))
            print(f"Song {str(songs[songNumer+1])} is playing ....")


        
        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H : %M : %S")
            speak(f"Sir, the time is {strTime}")
            print(f"The time is : {strTime}")
        
        elif 'open code' in query:
            codePath = "C:\\Users\\nitin\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email to harry' in query:
            try:
                speak("What should I say ?")
                content = takeComand()
                to = "yourmail@gmail.com"
                sendMail(to, content)
                speak("Email has been sent.")
            except Exception as e:
                print(e)
                print("Sorry sir, I am not able to send this email at the moment")
        elif 'exit' in query:
            speak("Thanks for using me. Have a good day ahead!")
            print("Thanks for using Jarvis")
            exit()
        
