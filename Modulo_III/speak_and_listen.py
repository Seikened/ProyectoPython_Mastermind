import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init()
engine.setProperty("rate",160)
engine.setProperty("voice", "spanish")

r = sr.Recognizer()#Este es nuestro reconocerdor

def speak(text):
    engine.say(text)
    engine.runAndWait()



def listen():
    with sr.Microphone() as source:   #Aqui se abre y empieza a tener el microfono como un recurso y empieza a almacenar el texto
        print("Escuchando... ")
        audio = r.listen(source)   #Aquí se deja todo el recurso de lo de arriba

        try:
            text = r.recognize_google(audio, language="es=ES")
            print("he entendido: {}".format(text))
            return text
        except sr.UnknownValueError:
            print("Lo siento pero no te he entendido")
            

if __name__ == "__main__":
    speak("Probando todo bien")
    print(listen())


