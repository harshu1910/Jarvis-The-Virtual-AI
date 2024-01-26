import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import os 


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[0].id)

def speak(audio):
  engine.say(audio)
  engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
      speak("good morning!")
      speak("i am jarvis sir please tell me how may i help you")
    elif hour>12 and hour<18:
      speak("good afternoon!")
      speak("i am jarvis sir please tell me how may i help you")
    else:
      speak("good evening!")
      speak("i am jarvis sir please tell me how may i help you")
def takeCommand():
    # it takes microphone input from the user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print (e)

        print("say that again please...")
        return "none"
    return query

if __name__ == "__main__":
    speak("")
    wishMe() 
    query = takeCommand().lower()

  #logic for executing tasks based on query
    if 'wikipedia' in query:
        speak('searching wikipedia...')
        query = query.replace("wikipedia", "")
        result = wikipedia.summary(query, sentences=2)
        speak("according to wikipedia")
        print(result)
        speak(result)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")

    elif 'open google' in query:
        webbrowser.open("google.com")    

    elif 'the time' in query:
      strTime = datetime.datetime.now().strftime("%H:%M:%S")
      speak(f"Sir the time is{strTime}")  

    elif 'play music' in query:
      music_dir = 'C:\\users\\harsh sharma\\desktop\\music'
      songs = os.listdir(music_dir)
      print(songs)
      os.startfile(os.path.join(music_dir, songs[3]))

    elif 'open code' in query:
      codePath = "C:\\Users\\Harsh Sharma\\AppData\\Local\\Programs\\Microsoft VS code\\code.exe"
      os.startfile(codePath)
