from typing import get_type_hints
from poketload import get_all_pokemons
from pprint import pprint
import random,os






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
    os.system("cls")
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

def player_attack(player_pokemon,enemy_pokemon):
    if enemy_pokemon["current_heatl"]:
        chosen = None
        while not chosen:    
            print("Selecciona tu ataque")
            for index in range(len(player_pokemon["attacks"])):
                print("{} - {})".format(index,get_attack_info(player_pokemon["attacks"][index])))
            try:
                item =  player_pokemon["attacks"][int(input("¿Cual elijes? "))]
                damage = int(item["damage"])
                enemy_pokemon["current_health"] -= damage
                print("Vida restante de {} es {}".format(enemy_pokemon["name"],enemy_pokemon["current_health"]))
                chosen = True
                
            except(ValueError, IndexError):
                print("Opción no valida")
        input("Enter")    
        os.system("cls") 
    
def enemy_attack(enemy_pokemon,player_pokemon):
    #RANDOM EMENY ATTACK
    random_attack = random.choice(enemy_pokemon["attacks"])
    damage = int(random_attack["damage"])
    print("Daño de ataque {}".format(damage),get_attack_info(random_attack))
    player_pokemon["current_health"] -= damage
    print("Vida restante de {} es {}".format(player_pokemon["name"],player_pokemon["current_health"]))
    input("ENTER")
    os.system("cls")
    
def assign_experience(attack_history):
    for pokemon in attack_history:
        points = random.randint(1, 5)
        pokemon["current_exp"] += points

    while pokemon["current_exp"] > 20:
        pokemon["level"] += 1
        pokemon["current_health"] = pokemon["base_health"]
        print("Tu pokemon ha subido de nivel {}".format(get_pokemon_info(pokemon)))

def cure_pokemon(player_profile,player_pokemon):
    if player_profile["heat_potion"] > 0:
       player_pokemon["current_health"] = player_pokemon["base_health"]  
       print("Vida de {} es {}/ te quedan {} posiones".format( player_pokemon["name"], player_pokemon["current_health"],player_profile["heat_potion"]))
    else:
         print("No tienes mas posiones")

def fight(player_profile,enemy_pokemon):
    os.system("cls")
    print("---NUEVO COMBATE---")

    attack_history = []
    player_pokemon = choose_pokemon(player_profile)
    
    print("Contrincantes: \n{} \n{}VS \n{}".format(get_pokemon_info(player_pokemon),
                                                 " "* 17,
                                                 get_pokemon_info(enemy_pokemon)))

    while any_player_pokemon_lives(player_profile) and enemy_pokemon["current_health"] > 0:
        action = None
        #make a while control with "¿Que deseas hacer? [A]tacar , [P]okeball, Posion de [V]ida, [C]ambiar: " and create por each case a if or elif control with each letter
        
        while action not in ["A", "P", "V", "C"]: 
            action = input("¿Que deseas hacer? [A]tacar , [P]okeball, Posion de [V]ida, [C]ambiar: ").upper()
            os.system("cls")
        if action == "A":
            player_attack(player_pokemon,enemy_pokemon)
            enemy_attack(enemy_pokemon,player_pokemon)
            attack_history.append(player_pokemon)
            attack_history.append(enemy_pokemon)
            player_profile["combats"] += 1
        elif action == "P":
            player_profile["pokeballs"] -= 1
            enemy_attack(enemy_pokemon,player_pokemon)
            attack_history.append(player_pokemon)
            attack_history.append(enemy_pokemon)
            player_profile["combats"] += 1
        elif action == "V":
            cure_pokemon(player_profile,player_pokemon)
        elif action == "C":
            if player_pokemon["current_health"] == 0 and any_player_pokemon_lives(player_profile):
                player_pokemon = choose_pokemon(player_profile)
                print("Contrincantes: \n{} \n{}VS \n{}".format(get_pokemon_info(player_pokemon),
                                                 " "* 17,
                                                 get_pokemon_info(enemy_pokemon)))
        else:
            print("Opción no valida")

    
    if enemy_pokemon["current_health"] == 0:
        assign_experience(attack_history)
        print("Has ganado")
    else:    
        print("Has perdido")

    print("---FIN DEL COMBATE---")
    input("Presiona ENTER para continuar...")
    os.system("cls")

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




