#........AI DESKTOP VOICE ASSISTANT........

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import pyautogui 
import pywhatkit as kit
import subprocess as sp 


engine = pyttsx3.init('sapi5')

engine.setProperty('volume', 1.0)
engine.setProperty('rate', 180)
voices= engine.getProperty('voices') #getting details of current voice
engine.setProperty('voice',voices[0].id)


def speak(audio):
   engine.say(audio) 
   engine.runAndWait() #Without this command, speech will not be audible to us.


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Tejas Sir. Please tell me how may I help you")  

  
def takeCommand():
    #It takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        r.energy_threshold = 200
        r.adjust_for_ambient_noise(source, duration=5)
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        speak("Say that again please...")
        return "None" #None string will be returned
    return query

def search_on_google(query):
    kit.search(query)


def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


if __name__=="__main__" :
   wishme()
   while True:
   #if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        

        elif 'open google' in query:
            speak('What do you want to search on Google, sir?')
            query = takeCommand().lower()
            speak('')
            search_on_google(query)


        elif 'play music' in query:
            music_dir = 'C:\\Users\\sharv\\Dropbox\\PC\\Music\\gana'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))


        elif 'open code' in query:
            codePath = "C:\\Users\\sharv\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        

        elif 'notepad' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad"
            os.startfile(codePath)


        elif 'screenshot' in query:
            image = pyautogui.screenshot()
            image.save('C:\\Users\\sharv\\Dropbox\\PC\\Pictures\\Saved Pictures\\screenshot.png')
            speak('Screenshot taken.')


        elif 'camera' in query:
            open_camera()


        elif "send whatsapp message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = takeCommand().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")


        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")


        elif 'stop' in query:
            speak("okay sir !")
            speak(" Good Byeee !")
            exit()