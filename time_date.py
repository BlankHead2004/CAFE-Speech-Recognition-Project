import pyttsx3
import datetime
from speak_listen import speak
from speak_listen import TakeCommand

def speak_current_time():
    # Get the current time
    current_time = datetime.datetime.now().strftime("%H:%M %p")

    # Create a string to speak
    speak_text = f"The current time is {current_time}"
    print(speak_text)
    speak(speak_text)

    
def speak_current_date():
    # Get the current date
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")

    # Create a string to speak
    speak_text = f"Today is {current_date}"
    print(speak_text)
    speak(speak_text)