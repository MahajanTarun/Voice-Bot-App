import speech_recognition as sr
import pyttsx3

engine = pyttsx3.init()
r = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            return r.recognize_google(audio).lower()
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return ""

def ask_question(question):
    speak(question)
    while True:
        response = listen()
        if 'yes' in response:
            return True
        elif 'no' in response:
            return False
        else:
            speak("Please say yes or no.")

# Main flow
speak("Welcome to the Lead Qualifier Bot for home renovation services.")
if not ask_question("Do you own your home?"):
    speak("Thank you for calling. We appreciate your interest. Goodbye.")
elif not ask_question("Is your budget over $10,000?"):
    speak("Thank you for calling. We appreciate your interest. Goodbye.")
elif not ask_question("Are you looking to start within 3 months?"):
    speak("Thank you for calling. We appreciate your interest. Goodbye.")
else:
    speak("You are classified as a hot lead. I will transfer you to a human agent now. Thank you.")