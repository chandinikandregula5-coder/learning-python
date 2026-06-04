import datetime
import speech_recognition as sr
import pyttsx3

# Voice engine
engine = pyttsx3.init()

user_name=input()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except Exception:
        speak(f"Sorry {user_name}, I didn't catch that.")
        return ""


def check_greeting(command):
    hour = datetime.datetime.now().hour

    if "good morning" in command:
        if hour < 12:
            speak("Good morning {user_name}")
        elif hour < 18:
            speak(f"It is afternoon {user_name}, not morning")
        else:
            speak(f"It is evening {user_name}, not morning")

    elif "good afternoon" in command:
        if 12 <= hour < 18:
            speak(f"Good afternoon {user_name}")
        elif hour < 12:
            speak(f"It is morning {user_name}, not afternoon")
        else:
            speak(f"It is evening {user_name}, not afternoon")
    elif "good evening" in command:
        if 17 <= hour < 12:
            speak("good evening {user_name}")
    elif 5<= hour <12:
       speak("it is morning{user_name},not evening")
    elif 12 <= hour <17:
         speak("it is afternoon {user_name},not evening")
    else:
      speak("it is night{username},not evening")


while True:
    command = take_command()

    check_greeting(command)

    if "exit" in command:
        speak(f"Goodbye {user_name}")
        break
