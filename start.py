import datetime

def start():
    hour = int(datetime.datetime.now().hour)
    wish = "Good Morning!" if hour >= 0 and hour < 12 else "Good Afternoon!" if hour >= 12 and hour < 18 else "Good Evening!"
    speak(f'Hello Sir, {wish} I am your voice assistant. Please tell me how may I help you')