import tkinter as tk
import datetime
import webbrowser
import speech_recognition as sr
import pyttsx3

def take_command():
    # code for taking command from user
    pass

def speak(text):
    # code for speaking the text
    pass

def run_command():
    instruction = take_command().lower()
    print(instruction)

    if 'who are you' in instruction:
        speak('I am your personal voice Assistant')

    elif 'what can you do for me' in instruction:
        speak('I can play songs, tell time, and help you go with wikipedia')

    elif 'current time' in instruction:
        time = datetime.datetime.now().strftime('%I: %M')
        speak(f'current time is {time}')

    elif 'open google' in instruction:
        speak('Opening Google')
        webbrowser.open('google.com')

    elif 'open youtube' in instruction:
        speak('Opening Youtube')
        webbrowser.open('youtube.com')

    elif 'open facebook' in instruction:
        speak('Opening Facebook')
        webbrowser.open('facebook.com')

    elif 'open PythonGeeks' in instruction:
        speak('Opening PythonGeeks')
        webbrowser.open('pythongeeks.org')

    elif 'open linkedin' in instruction:
        speak('Opening Linkedin')
        webbrowser.open('linkedin.com')

    elif 'open gmail' in instruction:
        speak('Opening Gmail')
        webbrowser.open('gmail.com')

    elif 'open stack overflow' in instruction:
        speak('Opening Stack Overflow')
        webbrowser.open('stackoverflow.com')

    elif 'shutdown' in instruction:
        speak('I am shutting down')
        return False

    else:
        speak('I did not understand, can you repeat again')

    return True

def start():
    while True:
        if run_command():
            continue
        else:
            break

# Initialize the recognizer and the text-to-speech engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Start the main loop
start()
