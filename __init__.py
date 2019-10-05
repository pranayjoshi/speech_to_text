import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
engine.say("hi user")
engine.runAndWait()
def speak(text):

    engine.say(text)
    engine.runAndWait()
def myCommand():
    "listens for commands"

    r = sr.Recognizer()

    with sr.Microphone() as source:

        speak('i am ready for your command')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio).lower()
        speak('you said:' + command +'\n')

    #loop back to continue to listen for commands if unrecognizable speech is received
    except sr.UnknownValueError:
        speak("Your last command couldn\'t be heard")
        command = myCommand();

    return command
def result(command):
    mfopener = open("results.txt", "a+")
    mfopener.write(command)
    mfopener.close()
if __name__ == "__main__":
    result(myCommand())