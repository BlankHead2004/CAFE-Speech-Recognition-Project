# search.py
import pywhatkit
import wikipedia
from speak_listen import speak
from speak_listen import TakeCommand

def search_youtube(query):
    query = query.replace("youtube" , "")
    if query == "" :
        speak("Please say that again, Sir")
        return
    speak("Searching YouTube for " + query)
    pywhatkit.playonyt(query)

def search_google(query):
    query = query.replace("google" , "")
    if query == "" :
        speak("Please say that again, Sir")
        return
    speak("Searching Google for " + query)
    pywhatkit.search(query)

def search_wikipedia(query):
    query = query.replace("wikipedia" , "")
    if query == "" :
        speak("Please say that again, Sir")
        return
    speak("Searching Wikipedia for " + query)
    result = wikipedia.summary(query, sentences=2)
    print(result)
    speak(result)


# Example Usage:
# perform_search("Python programming", "google")
# perform_search("OpenAI", "wikipedia")
# perform_search("Python tutorial", "youtube")
