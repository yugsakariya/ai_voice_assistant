from dotenv import load_dotenv
load_dotenv()
import speech_recognition as sr
import webbrowser
import os
import musicLibrary
from gtts import gTTS
from groq import Groq

# pip install pocketsphinx 

recognizer = sr.Recognizer() 

client = Groq(api_key=os.getenv("groq_api_key"))

def aiProcess(command):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": command + " Answer in 3-5 sentences only, keep it short and simple."}]
    )
    return response.choices[0].message.content


def speak(text):
    os.system(f'say "{text}"')


def processCommand(c):
    if "open google" in c.lower():
        webbrowser. open("https://google.com")

    elif "open facebook" in c.lower():
        webbrowser. open("https://facebook.com")

    elif "open youtube" in c.lower():
        webbrowser. open("https://youtube.com")

    elif "open instagram" in c.lower():
        webbrowser. open("https://instagram.com")

    elif c.lower().startswith("play"):
        song = " ".join(c.lower().split(" ")[1:])
        if song in musicLibrary.music:
            link = musicLibrary.music[song]
            webbrowser.open(link)
        else:
            speak("Sorry,this song is not in my library. Please try another song.")


    else:
        output = aiProcess(c)
        speak(output)


if __name__ == "__main__":
    speak("Initializing Jarvis.... ")

    while True:
# Listen for the wake word "Jarvis"
# obtain audio from the microphone

        r = sr.Recognizer ()
        with sr.Microphone() as source:
            print ("Listening....")
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
        
        print("recognizing...")
        try:
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("yes sir")
                # listen for command 
                with sr.Microphone() as source:
                    print ("Jarvis active....")
                    audio = r.listen(source) 
                    command  = r.recognize_google(audio)

                    processCommand(command)


        except Exception as e:
            print ("Error; {0}". format (e))
            



