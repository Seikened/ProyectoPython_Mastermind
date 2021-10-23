action = input("¿Que deseas hacer? [A]tacar , [P]okeball, Posion de [V]ida, [C]ambiar: ")

        if action == "A":
            player_attack(player_pokemon,enemy_pokemon)
            attack_history.append(player_pokemon)
            
        elif action =="V":
            cure_pokemon(player_profile ,player_pokemon)
      
        elif action == "P":
            if player_profile["pokeballs"] > 0:
                player_profile["pokeballs"] -= 1
                if enemy_pokemon["current_health"] <= random.randint(0,enemy_pokemon["base_health"]):
                    player_profile["pokemon_inventory"].append(enemy_pokemon)
                    print("Has capturado a {}".format(enemy_pokemon["name"]))
                    enemy_pokemon["current_health"] = enemy_pokemon["base_health"]
                else:
                    print("No has capturado a {}".format(enemy_pokemon["name"]))
            else:
                print("No tienes mas pokeballs")

        elif action == "C":
            player_pokemon = choose_pokemon(player_profile)
            print("Contrincantes: \n{} \n{}VS \n{}".format(get_pokemon_info(player_pokemon),
                                                 " "* 17,
                                                 get_pokemon_info(enemy_pokemon)))

        else:
            print("Opción no valida")