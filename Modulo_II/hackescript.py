import os
from pathlib import Path
from random import randrange
from time import sleep
import sqlite3

HACKER_FILE_NAME = "Pruebameeee.txt"



def get_user_path():
    return "{}/".format(Path.home())


def delay_action():
    hours_g = randrange(7200,10800)#Generador de segundos
    #-------------------------------------Se convierten de seg a horas para que el usuario pueda ver la correcta conversión
    print("Durmiendo {} horas ".format((hours_g/60)/60.))
    sleep(hours_g) 


def get_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "AppData/Local/Google/Chrome/User Data/Default/History"
            connecting = sqlite3.connect(history_path)
            cursor = connecting.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY  last_visit_time DESC")
            urls = cursor.fetchall()
            print("las urls se han obtenido")
            connecting.close() 
            return urls
        except sqlite3.OperationalError:
            print("Durmiendo 3seg")
            sleep(3)


def create_hacker_file(user_path,chrome_history):
    hacker_file = open(user_path + "OneDrive/Escritorio/" + HACKER_FILE_NAME,"w") 
    hacker_file.write("Top links mas recientes\n\n")
    contador=0
    for urlss in chrome_history:
        contador += 1
        strings_urls = str(urlss)
        hacker_file.write("\n\nTop  #{}".format(contador)+"\n"+strings_urls)
    print("se ha creado el archivo con exito")

    return hacker_file


def main():

    ####delay_action()   
    # Calculamos la rusta del usuario de windows    
    user_path = get_user_path()
    #Recojemos el historial de google chrome
    chrome_history= get_chrome_history(user_path)
    #Creamos un archivo en el escritorio
    hacker_file = create_hacker_file(user_path,chrome_history)  
    

if __name__ == "__main__":
    main()
