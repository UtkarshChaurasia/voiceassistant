import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import wolframalpha # to calculate strings into formula, its a website which provides api, 100 times per day
import smtplib
from selenium import webdriver  # to control browser operations
from selenium.webdriver.common.keys import Keys
from io import BytesIO
from io import StringIO

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
newVoiceRate = 135
engine.setProperty('rate', newVoiceRate)
engine.runAndWait()


#wolframalpha id declaration
app_id= "E46YXW-T5LG6RT7K7"
client = wolframalpha.Client(app_id)




def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("Hello Utkarsh. Please tell me how may I help you") 




def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")
        speak("Say that again please...") 
        return "None"
    return query




def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('msdianuc07@gmail.com', 'ABHiNAWgv94@')
    server.sendmail('msdianuc07@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()




        # Logic for executing tasks based on query
        
            # Logic for searches
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)


        elif 'google' in query:
            indx = query.split().index('google')
            query = query.split()[indx+1:]
            speak("Searching google")
            webbrowser.open("https://www.google.com/search?q=" + '+'.join(query))

        elif 'youtube' in query:
            indx = query.split().index('youtube')
            query = query.split()[indx+1:]
            webbrowser.open("https://www.youtube.com/results?search_query=" + '+'.join(query))
        

        #Logic for calculation
        elif "calculate" in query:
            res = client.query(query)
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)



        #weather forecast
        elif "weather" in query:
            res = client.query(query)
            answer = next(res.results).text
            print(query + answer)
            speak(query +" "+ answer)


        #information
        elif "what is" in query:
            res = client.query(query)
            answer = next(res.results).text
            print("The answer is " + answer)
            speak("The answer is " + answer)





        elif "who are you" in query or "define yourself" in query:
            print('''Hello, I am Zen. Your personal Assistant.
            I am here to make your life easier. 
            You can command me to perform various tasks such as calculating sums or opening applications etcetra''')
            speak('''Hello, I am Zen. Your personal Assistant.
            I am here to make your life easier. 
            You can command me to perform various tasks such as calculating sums or opening applications etcetra''')


        elif "who made you" in query or "created you" in query:
            print("I have been created by Utkarsh Chaurasia.")
            speak("I have been created by Utkarsh Chaurasia.")
            

        elif 'tell me a joke' in query or 'zen tell me a joke' in query:
            print("Virat Kohli is the best captain")
            speak("Virat Kohli is the best captain")


        elif 'tell me another joke' in query or 'zen tell me another joke' in query:
            print("Mani is intelligent")
            speak("Mani is intelligent")


        elif 'open youtube' in query:
            webbrowser.open("youtube.com")


        elif 'open academia' in query:
            webbrowser.open("http://academia.srmist.edu.in/")


        elif 'open linkedin' in query:
            webbrowser.open("https://www.linkedin.com/in/utkarsh-chaurasia-a4b76a17b/")


        elif "open word" in query or "open Microsoft Word" in query:
            speak("Opening Microsoft Word")
            os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\Word 2013.exe')



        elif "open visual studio code" in query or "open visual studio" in query or "open studio code" in query:
            speak("Opening visual studio code")
            os.startfile('C:\\Users\\91873\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')  


        elif "open chrome" in query or "open google chrome" in query:
            speak("opening Google Chrome")
            os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')  


        elif 'play music' in query or 'play song' in query or 'sing me a song' in query:
            print("Which song you want to listen")
            speak("Which song you want to listen")
            print("Playing song")
            speak("Playing song")
            music_dir = 'C:\\Users\\91873\\Desktop\\Songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))


        elif 'time' in query or 'tell the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")


        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                speak("whom shoul I send")
                to = takeCommand()    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email") 


        elif "exit" in query or "bye" in query or "go " in query or "sleep" in query:
            print("Ok bye Utkarsh. Have a nice day ahead.")
            speak("Ok bye Utkarsh. Have a nice day ahead.")
            break   
            
            
            
            
