import webbrowser
import pyttsx3
import speech_recognition as sr

recognizer = sr.Recognizer()
ttsx = pyttsx3.init()

def speak():
    ttsx.say("hi sounava")
    ttsx.runAndWait()
if __name__=="__main__":
    speak()
    while True:
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("listening.....")
            audio=r.listen(source,timeout=2,phrase_time_limit=1)

        try:
            recog=r.recognize_google(audio)
            print("wait......")
            print(recog)
            ttsx.say(recog)
        except sr.UnknownValueError() as e:
            print("could not understand your audio")
        except sr.RequestError as e:
            print("error {0}".format(e))

