from requests_html import HTMLSession
import re, random


pokemon_base = {
    "url_photo":"",
    "name": "",
    "current_health": 100,
    "base_health": 100,
    "level": 1,
    "type": [],
    "current_exp": 0

}
MAIN_URL = "https://www.pokexperto.net/"
URL_BASE = "{}index2.php?seccion=nds/nationaldex/movimientos_nivel&pk=".format(MAIN_URL)
index = random.randrange(1,150)


def get_pokemon(index):
    session = HTMLSession()
    url = "{}{}".format(URL_BASE, index)
    url_img_pokemon = "https://www.pokexperto.net/nds/artwork/{}.jpg".format(index)

    
    new_pokemon = pokemon_base.copy()
    pokemon_page = session.get(url)
    pokemon_type_search= pokemon_page.html.find(".bordeambos", first=True).html

    new_pokemon["url_photo"] = url_img_pokemon
    new_pokemon["name"] = pokemon_page.html.find(".mini", first=True).text
    #current_health
    #base_heatl
    #level
    new_pokemon["type"]= re.findall("3ds/sprites/tipos/([A-Za-z]+).png",pokemon_type_search)
    #current_exp

    print("\n\nNumero de Pokemon #{}".format(index))
    print(new_pokemon["url_photo"])
    print("\n",url)
    print((" ".join(new_pokemon["type"]).title()))
    print(new_pokemon["name"],"\n")




get_pokemon(index)