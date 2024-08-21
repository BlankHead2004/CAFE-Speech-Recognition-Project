import wikipedia
from speak_listen import speak
from speak_listen import TakeCommand
import pyautogui
import os

if __name__  == "__main__" :
    
    file_path = "a.ahk"
    os.startfile(file_path)
    while True:
        
        query = TakeCommand().lower()
        if "wake up" in query:
            from GreetMe import GreetMe  
            GreetMe()
        
            while True:
                query = TakeCommand().lower()
                if "go to sleep" in query:
                    speak("Ok sir , You can call me anytime")
                    break
                
                elif "start typing" in query :
                    import write_save
                    write_save.main()
                
                elif "open" in query:
                    from apps import open_system_app
                    open_system_app(query)
                    
                elif "close" in query:
                    from apps import close_system_app
                    close_system_app(query)
                    
                elif "google" in query :
                    from searches import search_google
                    search_google(query)
                    
                elif "youtube" in query :
                    from searches import search_youtube
                    search_youtube(query)
                
            
                elif "wikipedia" in query :
                    from searches import search_wikipedia
                    search_wikipedia(query)
                    
                elif "abuse me" in query:
                    from abuse import abuseMe
                    abuseMe(query)
                    
                elif "pause" in query:
                    pyautogui.press("k")
                    speak("video paused")
                    
                elif "play" in query:
                    pyautogui.press("k")
                    speak("video played")
                    
                elif "unmute" in query:
                    speak("unmuting video")
                    pyautogui.press("m") 
                    
                elif "mute" in query:
                    pyautogui.press("m")
                    speak("video muted")
                       
                elif "volume up" in query:
                    from keyboard import volumeup
                    speak("Turning volume up")
                    volumeup()
                    
                elif "volume down" in query:
                    from keyboard import volumedown
                    speak("Turning volume down")
                    volumedown()
                
                elif "time" in query:
                    from time_date import speak_current_time
                    speak_current_time()
                
                elif "date" in query:
                    from time_date import speak_current_date
                    speak_current_date()                   
                    

# api key = 'fd4ebf9c-d0c7-4ecd-8273-e105256e862b'

