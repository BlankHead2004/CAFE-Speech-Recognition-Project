import pyttsx3
import speech_recognition

engine = pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
engine.setProperty('volume' ,0.8 )
engine.setProperty('voice' , voices[0].id)
engine.setProperty('rate' , 170)

def speak(audio) :
    engine.say(audio)
    engine.runAndWait()
    
def TakeCommand() :
    r = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 0.5
        r.energy_threshold = 300
        audio = r.listen(source , 0, 4)
    try:
        print("Understanding...")
        query= r.recognize_google(audio , language= 'en-in')
        print(f"You Said: {query}\n")
    except Exception as e: 
        print("Say that again.")
        return ""
    return query