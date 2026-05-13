# import pyttsx3

# engine = pyttsx3.init()
# engine.say("Hello, I am Jarvis. This is a test.")
# engine.runAndWait()
import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # or voices[1].id
engine.say("hey mobish shut up and study haRD")
engine.runAndWait()
