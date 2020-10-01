import datetime
import os
import smtplib
import webbrowser

import pyttsx3
import speech_recognition as sr
import wikipedia

#Jarvis_Project

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak('Good Morning!')
    elif 12 <= hour < 18:
        speak('Good Afternoon!')
    else:
        speak('Good Evening!')

    speak("I'm Jarvis Sir , Please tell me how may i help you?")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source, phrase_time_limit=5)

    try:
        print('Recognizing...')
        text = r.recognize_google(audio, language='en-in')
        print(f'User said : {text}\n')
    except Exception as recognition_exception:
        print(recognition_exception)
        print('Say that again please...')
        return 'None'

    return text


def send_email(receiver, body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('mohdsameer7408@gmail.com', 'B8a8b8e7s7@$')
    server.sendmail('mohdsameer7408@gmail.com', receiver, body)
    server.close()


if __name__ == '__main__':
    wish_me()
    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace('wikipedia', '')
            results = wikipedia.summary(query, sentences=2)
            speak(f'According to wikipedia...\n {results}')
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
        elif 'play music' in query:
            music_dir = 'E:\\Html_codes\\blank-profile-picture-973460_1280.png'
            os.startfile(music_dir)
        elif 'time' in query:
            time = datetime.datetime.now().strftime('%H:%M:%S')
            speak(f'It is {time} at present')
        elif 'open code' in query:
            code_dir = 'C:\\Users\\Sameer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe'
            os.startfile(code_dir)
        elif 'email to harry' in query:
            try:
                speak('What should i say?')
                content = take_command()
                to = 'mohdsameer7408@gmail.com'
                send_email(to, content)
                speak('Email has been sent!')
            except Exception as e:
                print(e)
                speak('An error occurred while sending the mail...')
        elif 'exit' in query:
            speak('Signing off!, Have a good day.')
            exit()
