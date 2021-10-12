import pyttsx3
import speech_recognition as sr
import re




def identify_name(text):
    name = None
    patterns = ["me llamo ([A-Za-z]+)", "yo soy ([A-Za-z]+)", "^([A-Za-z]+)$"]
    #for pattern in patterns: 
        
    name = re.findall("me llamo ([A-Za-z]+)", text)[0]
    print(name)
     
          
    return name




def main():
    engine = pyttsx3.init()
    engine.setProperty("rate",120)
    engine.setProperty("vioice", "spanish")


    engine.say("Hola, ¿cómo te llamas?")
    engine.runAndWait()

    r = sr.Recognizer() #Se encarga de recojer información si reconoce algun tipo de habla...

    with sr.Microphone() as source:
        print("Puedes hablar")
        audio = r.listen(source)
        text = r.recognize_google(audio, language="es=MX")
        print(text+"\n")
        
        name = identify_name(text)

        if name:
            engine.say("Encantado de conocerte {}".format(name))
        else:   
            engine.say("No te entendi, vamos otra vez")
        engine.runAndWait()





if __name__ == "__main__":
    main()