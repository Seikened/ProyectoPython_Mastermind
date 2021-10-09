import os
from random import randrange
from time import sleep


time_sleep = random.randint(1,4)


def main():
    sleep(randrange(1,4) * 60 * 60) #Me quede aqui H4X0RRSCRIPT - Espiando el historial de Google Chrome 3:03min

    desktop_path ="C:\\Users\\ferna\\OneDrive\\Escritorio\\" # "C:\\Users\\" + os.getlogin() + "\\Desktop\\" es para obtener una ruta de un usuario
   
    a =  open(desktop_path + "PARA TI.txt","w")
    a.write("Soy tu pesadilla")
    a.close()
    



if __name__ == "__main__":
    main()
