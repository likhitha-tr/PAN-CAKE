import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Initialize the engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am your assistant. Please tell me how may I assist you?")

def takeCommand():
    # It will record the audio
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)

        try:
            # Using google speech recognition
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"User said: {query}\n")
        except Exception as e:
            # If not understood, prompt again
            print("Say that again please...")
            return "None"
        return query

def assistant(query):
    if 'wikipedia' in query.lower():
        # Search wikipedia
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'play' in query.lower():
        # Play a song
        song = query.replace("play", "")
        speak("Playing " + song)
        pywhatkit.playonyt(song)

    elif 'time' in query.lower():
        # Get time
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"The time is {strTime}")

    elif 'who is' in query.lower():
        # Search wikipedia
        speak('Searching Wikipedia...')
        query = query.replace("who is", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'is love' in query.lower():
        speak("It is 100% sure that I love you")

    elif "will you be my girlfriend" in query.lower():
        speak("I'm just a computer program, I can't have a girlfriend")

    elif 'how are you' in query.lower():
        speak("I am fine, thank you. How about you?")

    elif 'i am fine' in query.lower():
        speak("That's good to hear")

    elif "bye" in query.lower():
        speak("Goodbye! Have a great day")
        exit()

    else:
        speak("Sorry, I did not understand that")

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        assistant(query)