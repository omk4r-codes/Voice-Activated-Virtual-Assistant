import speech_recognition as sr
import pyttsx3
import webbrowser
from namesofsites import sites

zira_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

def say(text, voice_id=None):
    engine = pyttsx3.init()
    
    # Optional: Set the voice (accent)
    if voice_id:
        engine.setProperty('voice', voice_id)
    
    engine.say(text)
    engine.runAndWait()

def take():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-IN")
            print(f"user said: {query}")
            return query
        except Exception as e:
            return "Some error occured! Please try again."
        
def open_web(sitename, site_url):
    say(f"Opening {sitename}", zira_id)
    webbrowser.open(site_url)  


if __name__ == '__main__':
    '''
    to set different voice: 
    # List available voices
    voices = pyttsx3.init().getProperty('voices')
    
    # Print available voices and their IDs
    for voice in voices:
        print(f"Voice ID: {voice.id}, Name: {voice.name}")
    
    # Change the voice using the voice ID (replace 'voice_id_here' with the desired ID)
    
    '''
    


    print("pycharm")
    say("Hello, I am Violet", zira_id)

    query = take()
    say(query, zira_id)

    for site in sites:
        if site[0].lower() in query.lower():
            open_web(site[0], site[1])
