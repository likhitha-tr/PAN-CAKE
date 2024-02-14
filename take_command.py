import speech_recognition as sr

def take_command() -> str:
    try:
        with sr.Microphone() as data_taker:
            print("Say Something")
            voice = listener.listen(data_taker)
            instruction = listener.recognize_google(voice)
            instruction = instruction.lower()
            return instruction
    except Exception as e:
        print(f"Error occurred: {e}")
        return None