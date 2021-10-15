from requests_html import HTMLSession
import pickle

pokemon_base = {
    "url_photo":"",
    "name": "",
    "current_health": 100,
    "base_health": 100,
    "level": 1,
    "type": None,
    "current_exp": 0

}
MAIN_URL = "https://www.pokexperto.net/"
URL_BASE = "{}index2.php?seccion=nds/nationaldex/movimientos_nivel&pk=".format(MAIN_URL)



"""Este archivo tiene una  funcion muy importante
-Conseguir los pokemons ya sea de internet o de el arvhivo que se ha generado previamente al descargarlos
-Y con esto tener los 150 pokemons que existen
"""


def get_pokemon(index):
    session = HTMLSession()
    url = "{}{}".format(URL_BASE, index)
    url_img_pokemon = "https://www.pokexperto.net/nds/artwork/{}.jpg".format(index)

    
    new_pokemon = pokemon_base.copy()
    pokemon_page = session.get(url)
    # pokemon_type_search= pokemon_page.html.find(".bordeambos", first=True).html


    ### Stats of the new pokemon
    new_pokemon["url_photo"] = url_img_pokemon
    new_pokemon["name"] = pokemon_page.html.find(".mini", first=True).text
    #current_health
    #base_heatl
    #level
    new_pokemon["type"] = [] ###############################################################  """new_pokemon["type"]= re.findall("3ds/sprites/tipos/([A-Za-z]+).png",pokemon_type_search)"""
    for img in pokemon_page.html.find(".pkmain", first=True).find(".bordeambos", first=True).find("img"):
        new_pokemon["type"].append(img.attrs["alt"])
    #current_exp
    ### 
    new_pokemon["attacks"] = []
    for attack_item in pokemon_page.html.find(".pkmain",)[-1].find("tr .check3"): #El -1 en una lista es: "El indice del último"
        attack={
            "name":attack_item.find("td",first=True).find("a",first=True).text, 
            "type": attack_item.find("td")[1].find("img",first=True).attrs["alt"],
            "min_livel": attack_item.find("th",first=True).text, 
            "damage":  int(attack_item.find("td")[3].text.replace("--","0"))
        }
        new_pokemon["attacks"].append(attack)




    return new_pokemon

def get_all_pokemons():
    try:
        print("Cargando el archivo de pokemons...")
        with open("pokefile.pkl", "rb") as pokefile: 
            all_pokemons = pickle.load(pokefile)#Esto carga el archivo de pokefile

    except FileNotFoundError:
    ####### Esto se genera cuando no tenemos un archivo con los pokemons
        print("pokefile no encontrado. Descangando los pokemons de internet...")
        all_pokemons = []
        for index in range(151):
            all_pokemons.append(get_pokemon(index+1))
            print("*", end="")
            

        with open("pokefile.pkl", "wb") as pokefile:
            pickle.dump(all_pokemons, pokefile)
            print("\n¡Todos los pokemons han sido descargados!")

        print("¡Lista de pokemons cargada!")
        return all_pokemons


get_all_pokemons()
