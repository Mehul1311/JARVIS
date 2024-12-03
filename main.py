import speech_recognition as sr
import pyttsx3
import wikipedia
import webbrowser
import datetime
import os


def speak(audio):
    engine = pyttsx3.init()  # Initialize text-to-speech engine
    voices = engine.getProperty('voices')  # Get available voices
    engine.setProperty('voice', voices[0].id)  # Choose the first voice (you can change it)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Use Google's speech recognition
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def assistant_main():
    speak("Hello sir, i am jarvis ! how can I help you today?")
    
    while True:
        query = take_command().lower()
        
        # Basic tasks that the assistant can handle:
        
        # 1. Open websites
        if 'open youtube' in query:
            webbrowser.open("youtube.com")
            speak("Opening YouTube")
            
        elif 'open google ' in query:
            webbrowser.open("google.com")
            speak("Opening Google")
        
        # 2. Tell the current time
        elif 'time' in query:
            str_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {str_time}")
        
        # 3. Search Wikipedia
        elif 'wikipedia , wanna search something' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("can't find wikipedia")
            speak(results)
        
        # 4. Play music (assuming you have a music folder)
        elif 'play music' in query:
            music_dir = 'C:\\Users\\Mehul\\Music'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))  # Plays the first song
            speak("playing")
        
        # 5. Exit the assistant
        elif 'stop' in query:
            speak("Okay sir!")
            break


if __name__ == "__main__":
    assistant_main()
