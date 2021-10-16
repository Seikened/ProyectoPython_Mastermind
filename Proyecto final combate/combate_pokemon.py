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
        "combats":0,
        "pokeballs": 0,
        "heat_potion": 0,
    }                                                                               

                                                                                    
def any_player_pokemon_lives(player_profile):
    return (sum( [pokemon["current_health"] for pokemon in player_profile["pokemon_inventory"]] ) > 0) # Si la suma de todas las vidas de los pokemon es mayor a 0 devolvera un True si no un False



def choose_pokemon(player_profile):
    chosen = None
    while not chosen:
        print("Elije tu pokemon con el que lucharas: ")
        for index in range(len(player_profile["pokemon_inventory"])):
            print("{} - {}".format(index,get_pokemon_info(player_profile["pokemon_inventory"][index])))
        try:
            return player_profile["pokemon_inventory"][int(input("¿Cual elijes? "))]
        except (ValueError, IndexError):
            print("Obción invalida")
        
    

def get_pokemon_info(pokemon):
    return "{} | Level {} | HEALTH POINS {}/{}".format(pokemon["name"].upper(), 
                                                       pokemon["level"],
                                                       pokemon["current_health"],
                                                       pokemon["base_health"])

def  get_attack_info(attack):
    return "{} | DAMAGE {} | MIN LEVEL {}".format(attack["name"].upper(),
                                                  attack["damage"],
                                                  attack["min_livel"],
                                                            )

def player_attack(player_pokemon):
    pass

def enemy_attack(enemy_pokemon,player_pokemon):
    #RANDOM EMENY ATTACK
    random_attack = random.choice(enemy_pokemon["attacks"])
    damage = int(random_attack["damage"])
    print("Daño de ataque {}".format(damage),get_attack_info(random_attack))
    player_pokemon["current_health"] -= damage
    print("Vida restante del pokemon seleccionado {}".format(player_pokemon["current_health"]))
    input("ENTER")

    



def fight(player_profile,enemy_pokemon):
    print("---NUEVO COMBATE---")
    player_pokemon = choose_pokemon(player_profile)
    
    print("Contrincantes: \n{} \n{}VS \n{}".format(get_pokemon_info(player_pokemon),
                                                 " "* 17,
                                                 get_pokemon_info(enemy_pokemon)))

    while any_player_pokemon_lives(player_profile) and enemy_pokemon["current_health"] > 0:

        player_attack(player_pokemon,enemy_pokemon)
        enemy_attack(enemy_pokemon,player_pokemon)
    
    

    print("---FIN DEL COMBATE---")
    input("Presiona ENTER para continuar...")











def main():
    pokemon_list = get_all_pokemons()
    player_profile = get_player_profile(pokemon_list)
    #pprint(player_profile)

    while any_player_pokemon_lives(player_profile):
        enemy_pokemon = random.choice(pokemon_list)
        fight(player_profile,enemy_pokemon)
        
    print("Has perdido en el combate numero {}".format(player_profile["combats"]))

if __name__ == "__main__":
    main()




