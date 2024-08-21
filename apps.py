import os
from speak_listen import speak
from speak_listen import TakeCommand


def open_system_app(query):
    
    dictapp = {"command prompt":"cmd","commandprompt":"cmd","paint":"mspaint","word":"winword","excel":"excel","chrome":"chrome","vs code":"code","vscode":"code","powerpoint":"powerpnt" , "notepad":"notepad" , "Microsoft Edge":"msedge"}
    keys = list(dictapp.keys())
    try:
        query = query.replace("open","")
        for app in keys:
            if app in query:
                    speak(f"Opening {app}")
                    os.system(f"start {dictapp[app]}")

    except Exception as e:
        speak(f"Failed to open {app}. Error: {str(e)}")

def close_system_app(query):
    
    dictapp = {"command prompt":"cmd","commandprompt":"cmd","paint":"mspaint","word":"winword","excel":"excel","chrome":"chrome","vscode":"code","powerpoint":"powerpnt" , "youtube" :"msedge" , "google" : "msedge" , "notepad":"notepad", "Microsoft edge":"msedge" , "edge":"msedge", "youtube":"msedge"}
    keys = list(dictapp.keys())
    try:
        query = query.replace("close","")
        for app in keys:
            if app in query:
                os.system(f"taskkill /f /im {dictapp[app]}.exe")      #add .exe if error
                speak(f"Closing {app}")
    except Exception as e:
        speak(f"Failed to close {app}. Error: {str(e)}")

# Example usage
# To open Notepad on Windows
# open_system_app("notepad.exe")

# To close Notepad on Windows
# close_system_app("notepad.exe")