import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    speak("Intializing Jarvis....")

while True:
    #listen for the wake word jarvis
    #obtain audio from the microphone

    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        audio=r.listen(source,timeout=2,phrase_time_limit=1)

    print("recognizing..")
    try:
        command= r.recognize_google(audio)
        print(command)

    except Exception as e:
        print("error; {0}".format(e))    
