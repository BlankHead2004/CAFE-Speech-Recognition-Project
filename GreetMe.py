import pyttsx3
import datetime
from speak_listen import speak
from speak_listen import TakeCommand
    
def GreetMe() :
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12 :
        speak("Good Morning, Sir ")
    
    elif hour>=12 and hour<16 :
        speak("Good Afternoon, Sir")
        
    else :
        speak("Good Evening, sir")
    
    speak("Please tell me how can i help you ?")