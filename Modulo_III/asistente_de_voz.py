import re
from speak_and_listen import speak,listen





def identify_name(text):
    name = None
    patterns = ["me llamo ([A-Za-z]+)", "yo soy ([A-Za-z]+)", "^([A-Za-z]+)$"]
    #for pattern in patterns: 
    for pattern in patterns:
        try:
            name = re.findall(pattern, text)[0]
            print(name)
        except IndexError:
            pass   
    return name




def main():
    speak("Hola, ¿Cómo te llamas? ")
    text = listen()
    name = identify_name(text)
    if name:
        speak("Encantado de conocerte, {}".format(name))
    else:
        speak("Pues mira, la verdad no te he entenido")
    



    





if __name__ == "__main__":
    main()