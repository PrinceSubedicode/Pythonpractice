import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import datetime
import wikipedia
import os
import json     
import threading
import time
from enum import Enum
import logging
from typing import Optional, Callable, Dict, List
import re

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class CommandType(Enum):
    TIME = "time"
    DATE = "date"
    OPEN_YOUTUBE = "open_youtube"
    OPEN_GOOGLE = "open_google"
    SEARCH = "search"
    WIKIPEDIA = "wikipedia"
    WEATHER = "weather"
    SYSTEM = "system"
    STOP = "stop"
    UNKNOWN = "unknown"

class JarvisAssistant:
    def __init__(self):
        # Initialize recognizer and TTS engine
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        
        # Set up voice properties
        voices = self.engine.getProperty('voices')
        if voices:
            self.engine.setProperty('voice', voices[0].id)  # Male voice
        
        self.engine.setProperty('rate', 180)
        self.engine.setProperty('volume', 0.9)
        
        # Command patterns with regex for better matching
        self.command_patterns = {
            CommandType.TIME: re.compile(r'.*(time|clock).*'),
            CommandType.DATE: re.compile(r'.*(date|day|today).*'),
            CommandType.OPEN_YOUTUBE: re.compile(r'.*(open|start).*youtube.*'),
            CommandType.OPEN_GOOGLE: re.compile(r'.*(open|start).*google.*'),
            CommandType.SEARCH: re.compile(r'.*search (for)? (.+)'),
            CommandType.WIKIPEDIA: re.compile(r'.*(who is|what is|tell me about|wikipedia) (.+)'),
            CommandType.WEATHER: re.compile(r'.*(weather|temperature) (in|for|at)? (.+)'),
            CommandType.SYSTEM: re.compile(r'.*(shutdown|restart|sleep) (computer|pc).*'),
            CommandType.STOP: re.compile(r'.*(stop|exit|quit|goodbye).*')
        }
        
        self.weather_api_key = os.getenv('WEATHER_API_KEY', 'your_api_key_here')
        self.is_listening = False
        
        logger.info("Jarvis initialized")

    def speak(self, text: str, priority: bool = False) -> None:
        """Convert text to speech"""
        print(f"Jarvis: {text}")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self, timeout: int = 5, phrase_time_limit: int = 8) -> Optional[str]:
        """Listen for audio input and convert to text"""
        with sr.Microphone() as source:
            try:
                print("Listening...")
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
                
                command = self.recognizer.recognize_google(audio).lower()
                print(f"You said: {command}")
                return command
                
            except sr.WaitTimeoutError:
                return None
            except sr.UnknownValueError:
                return None
            except sr.RequestError as e:
                logger.error(f"Speech recognition error: {e}")
                return None

    def classify_command(self, command: str) -> (CommandType, Dict):
        """Classify the command using regex patterns"""
        if not command:
            return CommandType.UNKNOWN, {}
            
        for cmd_type, pattern in self.command_patterns.items():
            match = pattern.match(command)
            if match:
                if cmd_type == CommandType.SEARCH:
                    return cmd_type, {'query': match.group(2)}
                elif cmd_type == CommandType.WIKIPEDIA:
                    return cmd_type, {'query': match.group(2)}
                elif cmd_type == CommandType.WEATHER:
                    return cmd_type, {'location': match.group(3)}
                else:
                    return cmd_type, {}
                    
        return CommandType.UNKNOWN, {}

    def search_wikipedia(self, query: str, sentences: int = 2) -> str:
        """Search Wikipedia for information"""
        try:
            wikipedia.set_lang("en")
            results = wikipedia.summary(query, sentences=sentences)
            return results
        except wikipedia.DisambiguationError as e:
            return f"Multiple results found. Please be more specific. Options include: {', '.join(e.options[:3])}"
        except wikipedia.PageError:
            return "Sorry, I couldn't find any results for that query."
        except Exception as e:
            logger.error(f"Wikipedia search error: {e}")
            return "Sorry, I encountered an error while searching Wikipedia."

    def get_weather(self, location: str) -> str:
        """Get weather information for a location"""
        if self.weather_api_key == 'your_api_key_here':
            return "Please set up a weather API key to use this feature."
            
        try:
            base_url = "http://api.openweathermap.org/data/2.5/weather"
            params = {
                'q': location,
                'appid': self.weather_api_key,
                'units': 'metric'
            }
            
            response = requests.get(base_url, params=params)
            data = response.json()
            
            if response.status_code == 200:
                weather_desc = data['weather'][0]['description']
                temp = data['main']['temp']
                city = data['name']
                return f"The weather in {city} is {weather_desc} with a temperature of {temp} degrees Celsius."
            else:
                return f"Sorry, I couldn't get weather information for {location}."
                
        except Exception as e:
            logger.error(f"Weather API error: {e}")
            return "Sorry, I encountered an error while fetching weather information."

    def get_time(self) -> str:
        """Get current time"""
        now = datetime.datetime.now()
        return now.strftime("%I:%M %p")

    def get_date(self) -> str:
        """Get current date"""
        now = datetime.datetime.now()
        return now.strftime("%A, %B %d, %Y")

    def system_command(self, command: str) -> str:
        """Execute system commands"""
        if 'shutdown' in command:
            return "Shutdown command disabled for safety."
        elif 'restart' in command:
            return "Restart command disabled for safety."
        elif 'sleep' in command:
            return "Sleep command disabled for safety."
        return "Unknown system command."

    def process_command(self, command: str) -> bool:
        """Process the given command and execute appropriate action"""
        cmd_type, params = self.classify_command(command)
        
        if cmd_type == CommandType.TIME:
            self.speak(f"The time is {self.get_time()}")
            
        elif cmd_type == CommandType.DATE:
            self.speak(f"Today is {self.get_date()}")
            
        elif cmd_type == CommandType.OPEN_YOUTUBE:
            self.speak("Opening YouTube")
            webbrowser.open("https://youtube.com")
            
        elif cmd_type == CommandType.OPEN_GOOGLE:
            self.speak("Opening Google")
            webbrowser.open("https://google.com")
            
        elif cmd_type == CommandType.SEARCH:
            query = params.get('query', '')
            if query:
                self.speak(f"Searching for {query}")
                webbrowser.open(f"https://www.google.com/search?q={query}")
            else:
                self.speak("What would you like me to search for?")
                
        elif cmd_type == CommandType.WIKIPEDIA:
            query = params.get('query', '')
            if query:
                self.speak("Let me check Wikipedia for you")
                summary = self.search_wikipedia(query)
                self.speak(summary)
            else:
                self.speak("What would you like me to look up on Wikipedia?")
                
        elif cmd_type == CommandType.WEATHER:
            location = params.get('location', '')
            if location:
                weather_info = self.get_weather(location)
                self.speak(weather_info)
            else:
                self.speak("For which location would you like weather information?")
                
        elif cmd_type == CommandType.SYSTEM:
            response = self.system_command(command)
            self.speak(response)
            
        elif cmd_type == CommandType.STOP:
            self.speak("Goodbye!")
            return False
            
        elif cmd_type == CommandType.UNKNOWN:
            self.speak("I'm sorry, I didn't understand that command. Please try again.")
            
        return True

    def listen_continuously(self):
        """Continuously listen for commands"""
        self.is_listening = True
        
        # Initialize microphone once outside the loop
        with sr.Microphone() as source:
            # Adjust for ambient noise only once at startup
            logger.info("Adjusting for ambient noise... Please wait...")
            self.recognizer.adjust_for_ambient_noise(source, duration=2)
            print("Ready! You can ask me anything now.")
            self.speak("Ready! You can ask me anything now.")
            
            while self.is_listening:
                try:
                    print("Listening...")
                    audio = self.recognizer.listen(source, timeout=3, phrase_time_limit=8)
                    
                    try:
                        command = self.recognizer.recognize_google(audio).lower()
                        print(f"You said: {command}")
                        
                        if command:
                            if not self.process_command(command):
                                self.is_listening = False
                                
                    except sr.UnknownValueError:
                        # No understandable speech detected, continue listening
                        pass
                    except sr.RequestError as e:
                        logger.error(f"Speech recognition error: {e}")
                        
                except sr.WaitTimeoutError:
                    # Timeout is normal, just continue listening
                    pass
                except Exception as e:
                    logger.error(f"Unexpected error in listening: {e}")

    def start(self):
        """Start the assistant"""
        self.speak("Initializing Jarvis. How can I assist you today?")
        self.listen_continuously()

if __name__ == "__main__":
    try:
        jarvis = JarvisAssistant()
        jarvis.start()
            
    except KeyboardInterrupt:
        print("\nShutting down Jarvis...")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        print("An error occurred. Please check the logs for details.")
        
        

.
        