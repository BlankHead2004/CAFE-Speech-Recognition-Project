import speech_recognition as sr
import pyautogui
import time
from speak_listen import speak
from speak_listen import TakeCommand

def write_to_editor(text):
    # Simulate typing the text
    pyautogui.typewrite(text)

def main():
    # Initialize the speech recognizer
    speak("Typing started....")

    while True:
        query = TakeCommand().lower()

        if "stop typing" in query.lower():
            print("Stopping typing...")
            speak("Stopping typing...")
            break  # Exit the loop and stop the function
        
        # Write the recognized text to the word editor
        write_to_editor(query+ " ")
        time.sleep(2)

