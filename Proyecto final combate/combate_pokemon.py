from poketload import get_all_pokemons
from pprint import pprint
import random






#/2 profile =

#/2 Esto va a genrar una lista en la cual nos genera 3 iteraciones y a cada iretaración se va a ejecutar este codigo "random.randing(len(pokemon_list))"  y esto sera el contenido de la lista final
                                                                                    #/2 Aqui nos hemos ahoprrado esta linea de codigo                                                                                 
                                                                                    #/2  for a in range(3):
                                                                                    #/2      profile["pokemon_inventory"].append(random.randing(len(pokemon_list)))
        

def get_player_profile(pokemon_list):
    
    return  { 
        "player_name": input("¿Cual es tu nombre? "),
        "pokemon_inventory": [random.choice(pokemon_list) for a in range(3)], 
        "pokeballs": 0,
        "heat_potion": 0,
        "combats":0
    }                                                                               

                                                                                    



def main():
    pokemon_list = get_all_pokemons()
    player_profile = get_player_profile(pokemon_list)
    pprint(player_profile)

if __name__ == "__main__":
    main()




