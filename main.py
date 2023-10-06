import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime
import openai
from namesofsites import sites_or_apps, songs

zira_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
openai.api_key = 'Your_api_key_here'

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
        # r.pause_threshold = 1
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-IN")
            print(f"user said: {query}")
            return query
        except Exception as e:
            return "Some error occured! Please try again."
        
def open_web_or_apps(sitename_or_appname, site_url_or_app_address):
    say(f"Opening {sitename_or_appname}", zira_id)
    webbrowser.open(site_url_or_app_address)
    os.system(f"open {site_url_or_app_address}")
        

def play_song(songname, song_address):
    say(f"Playing {songname}", zira_id)
    os.startfile(song_address)

def start_up():
    for site_or_app in sites_or_apps:
        ini_command = "open "
        sitename_or_appname = f"{site_or_app[0]}"
        user_command = ini_command + sitename_or_appname.lower()
        if user_command.lower() in query.lower():
            open_web_or_apps(site_or_app[0], site_or_app[1])
            


    user_command = "play songs".lower()
    if user_command in query.lower():
        filepath = "C:\\Users\\omkar\\OneDrive\\Desktop\\NCS_Songs"
        try:
            say("Opening songs folder that I found", zira_id)
            os.startfile(filepath)
        except Exception as ex:
            say(f"No folder found for playing songs!", zira_id)
        
     
    for song in songs:
        user_command = f"play song {song[0].lower()}"
        if user_command in query.lower():
                play_song(song[0], song[1])


    if "the time".lower() in query.lower():
        strf_time = datetime.datetime.now().strftime("%H:%M:%S")
        say(f"The current time is {strf_time}", zira_id)

    if "using AI".lower() in query.lower():
        try:
            query_seperation = query.split("using AI", 1)
            prompt = query_seperation[1].strip()
            if prompt:
                response = openai.Completion.create(
                    engine = "text-davinci-002",
                    prompt = prompt,
                    max_tokens = 500
                )
                say(response, zira_id)
            else:
                say("Please provide a valid prompt!", zira_id)
        except Exception as e:
            say(f"Error resolving query. You might have ended your free tokens limit", zira_id)

    if  "tell me a joke".lower() in query.lower():
        say("What is a better joke than your life? HaHaHaHaHa", zira_id)        # :)
        exit()
    

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
    

    say("Hello, I am Violet", zira_id)

    query = take()
    # say(query, zira_id)
    start_up();

    say("Do you want any other help?", zira_id)
    query = take()
    # say(query, zira_id)
    if query.lower() == "no" or query.lower() == "naah":
        say("Okay. For any help, I am just a click away! Good day!", zira_id)
    else:
        start_up();
    
    