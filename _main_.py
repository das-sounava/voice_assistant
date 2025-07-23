import webbrowser
import pyttsx3
import speech_recognition as sr
import pyaudio
recognizer = sr.Recognizer()
ttsx = pyttsx3.init()
ttsx_1=ttsx.getProperty('voices')
ttsx.setProperty('voice',ttsx_1[1].id)
def speak():
    ttsx.say("initializing ana")
    ttsx.runAndWait()
def google():
    webbrowser.open("https://www.google.com")
def youtube():
    webbrowser.open("https://www.youtube.com")
if __name__=="__main__":
    speak()
    while True:
        r=sr.Recognizer()
        try:
            with sr.Microphone() as source:
                ttsx.say("listening.....")
                audio=r.listen(source,phrase_time_limit=3,timeout=2)
                recog=r.recognize_google(audio, language='eng-in')
                if(recog.lower()=="hello"):
                    ttsx.say("ana is awake")
                    command=r.listen(source,phrase_time_limit=3,timeout=2)
                    ttsx.say("recognizing")
                    com=r.recognize_google(command, language='eng-in')
                    print(com)
                    ttsx.say(com)
                    if(com.lower()=="open google"):
                        google()
                        ttsx.say("google opened")
                    elif(com.lower()=="open youtube"):
                        youtube()
                        ttsx.say("youtube opened")


        except Exception as e:
            print("error; {0}".format(e))
             

