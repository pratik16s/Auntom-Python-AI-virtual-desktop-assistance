import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice', voices[0].id)

# auntom will wish you according to the time
def wish():
    hour = int(datetime.datetime.now().hour)
    if (hour >= 0 and hour < 12):
        speak("good morning")
    elif (hour >= 12 and hour <= 18):
        speak("good afternoon")
    else:
        speak("good evening")
    speak("how may i help you?")

#speak something
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# takes the voice and returns it's text format
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        # wait for a second to let the recognizer
        # adjust the energy threshold based on
        # the surrounding noise level
        r.energy_threshold = 300
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)  # Using google to recognize audio
        try:
            # listens for the user's input
            audio = r.listen(source)
            query = r.recognize_google(audio, language='en-in')
            # query = query.lower()
            print("Did you just say:", query)
        except Exception as e:
            # print(e)
            print("say that again...please")
            return "none"
        return query
# send email to somebody, you can create a whole directory to send mails to multiple person
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
if __name__ == "__main__":
    speak("This is auntom here... ")
    wish()
    while True:
        # if 1:
        query = takeCommand().lower()  # Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  # if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:                 
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")
        elif 'play music' in query:
            music_dir=str(input("enter your music directory path:(saparated by //)"))
            songs=os.listdir(music_dir)
            print(songs)
            r=random.randint(0,len(songs))
            os.startfile(os.path.join(music_dir,songs[r]))
        elif 'the time' in query:
            time_now=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            speak("current time and date is")
            speak(time_now)
            print(time_now)
        elif 'stack overflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'email to pratik' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "pratikyourEmail@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend. I am not able to send this email")

