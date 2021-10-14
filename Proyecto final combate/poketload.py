from requests_html import HTMLSession
import re


pokemon_base = {
    "name": "",
    "current_health": 100,
    "base_health": 100,
    "level": 1,
    "current_exp": 0

}

URL_BASE = "https://www.pokexperto.net/index2.php?seccion=nds/nationaldex/movimientos_nivel&pk="

"""for items in chrome_history:
        results = re.findall("https://www.instagram.com/([A-Za-z0-9_.-]+)/+$", items[2])
        if results and results[0] not in ["fer_leonfranco"]:  # FILTRO
            profiles_visited.append(results[0])"""


def get_pokemon(index):
    session = HTMLSession()
    url = "{}{}".format(URL_BASE, index)
    url_img_pokemon = "https://www.pokexperto.net/nds/artwork/{}.jpg".format(index)

    
   
    pokemon_page = session.get(url)
    pokemon_name = pokemon_page.html.find(".mini", first=True).text
    pokemon_type_url_image = pokemon_page.html.find(".bordeambos", first=True)
    pokemon_type = str(re.findall("https://www.pokexperto.net/3ds/sprites/tipos/([A-Za-z]+).png",pokemon_type_url_image)).title()
    
    
    print(pokemon_type)
    print(pokemon_name)




get_pokemon(1)