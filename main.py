import pyttsx3

def say(text, voice_id=None):
    engine = pyttsx3.init()
    
    # Optional: Set the voice (accent)
    if voice_id:
        engine.setProperty('voice', voice_id)
    
    engine.say(text)
    engine.runAndWait()

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
    
    zira_id = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'

    print("pycharm")
    say("Hello, I am your assistant", zira_id)
