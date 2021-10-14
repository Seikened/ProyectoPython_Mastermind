import os
from random import randint

import readchar as readchar

VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 90

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE
TAMANIO_BARRA=25

POS_X=0
POS_Y=1

NUM_POKEMONS = 4

obstacle_definition = """\
#########################################
##                                    ###
########################       ###      #
########################         ###    #
##                                      #
###  ###################           ######
###  ###############                  ###
###  ######            #######          #
###                       ###############
######################    ###############
####                                    #
####                              ###   #
####       #########              ###   #
####            ####       ##########   #
#########################################\
"""


win=None
victories = 0
pokemons = []
my_position = [2,1]
map_objects= [[14,13]]
#map_objects=[[10,1]] 
#,[39,13],[7,8],[39,4]
end_game = False
died = False



#Create obstacle map
obstacle_definition = [list(row) for row  in obstacle_definition.split("\n")]
print(obstacle_definition)
MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)


#Este generador de objetos es inutil en este proyecto

# Generete random objebs in the maps
#  while len(map_objects) < NUM_POKEMONS:
#        new_position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]

#        if new_position not in map_objects and new_position != my_position and \
#           obstacle_definition [new_position[POS_Y]][new_position[POS_X]] != "#" :
#            map_objects.append(new_position)


#MAIN LOOP
while win != True:

    os.system("cls")



    #Esto pinta el mapa
    print("╔"+"═" * MAP_WIDTH *2+"╗")

    for cordinate_y in range(MAP_HEIGHT):

        print("║",end="")#el (,end="") es para que al final no nos de un enter al generar un print
        for cordinate_x in range(MAP_WIDTH):
            #cambiamos el dibujar de una forma manual a dibujar el caracter que nos sugiere segun lo que la función nos indique
            char_to_draw= "  "
            objet_in_cell = None
            tail_in_cel = None

            for map_object in map_objects:
                if map_object[POS_X] == cordinate_x and map_object[POS_Y] == cordinate_y:
                    char_to_draw = " ©"
                    objet_in_cell = map_object

            #Aqui pinto la cola
            for tail_piece in pokemons:
                if tail_piece[POS_X] == cordinate_x and tail_piece[POS_Y] == cordinate_y:
                    char_to_draw = " ■"
                    tail_in_cel = tail_piece


            #Aqui dibujo la posicion del jugador
            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                char_to_draw = " ¶"

                if objet_in_cell :

                    while vida_pikachu > 0 and vida_squirtle > 0:

                        # TURNO DE PIKACHU###############################################################################################
                        print("\n\n               TURNO PIKACHU\n")
                        # Elección de ataque por la maquina
                        ataque_pikachu = randint(1, 3)

                        if ataque_pikachu == 1:
                            # BOLA VOLTIO ataque: 10
                            print("¡Bola voltio!")
                            vida_squirtle -= 10
                            print("A squirtle le han aquitado 10 de vida\n")
                        elif ataque_pikachu == 2:
                            # Impactrueno ataque: 15
                            print("¡PIKAAAAAAA CHUUUUUU!")
                            vida_squirtle -= 15
                            print("A squirtle le han aquitado 15 de vida por impactrueno\n")

                        elif ataque_pikachu == 3:
                            # Electrocular ataque: 8
                            print("¡Electrocutar!")
                            vida_squirtle -= 8
                            print("A squirtle le han aquitado 8 de vida por electrocutar\n")

                        if vida_squirtle < 0:
                            vida_squirtle = 0
                        if vida_pikachu < 0:
                            vida_pikachu = 0

                        barra_vida_pikachu = int((TAMANIO_BARRA * vida_pikachu) / VIDA_INICIAL_PIKACHU)
                        barra_vida_squirtle = int((TAMANIO_BARRA * vida_squirtle) / VIDA_INICIAL_SQUIRTLE)
                        print("PIKACHU: [{}{}] Vida: ({}/{})".format("*" * barra_vida_pikachu,
                                                                     " " * (TAMANIO_BARRA - barra_vida_pikachu),
                                                                     vida_pikachu, VIDA_INICIAL_PIKACHU))
                        print("SQUIRTLE: [{}{}] Vida: ({}/{})\n\n".format("*" * barra_vida_squirtle,
                                                                          " " * (TAMANIO_BARRA - barra_vida_squirtle),
                                                                          vida_squirtle,
                                                                          VIDA_INICIAL_SQUIRTLE))

                        input("Enter para continua el combate...")
                        os.system("cls")

                        # TURNO DE SQUIRTLE###############################################################################################
                        print("\n\n               TURNO DE SQUIRTLE\n")

                        # Elección de ataque por el usuario
                        ataque_squirtle = None
                        while ataque_squirtle not in ["A", "B", "C", "N"]:
                            ataque_squirtle = input(
                                "[A] Chorro de agua \n[B] Bola de agua \n[C] Tsunami \n[N] No hacer nada \n")

                        if ataque_squirtle == "A":
                            print("¡CHORRO DE AGUUUAAAA!")
                            vida_pikachu -= 8
                            print("A pikachu le han aquitado 8 de vida\n")
                        elif ataque_squirtle == "B":
                            print("¡PUM PAOOO!")
                            vida_pikachu -= 9
                            print("A pikachu le han aquitado 9 de vida por bola de agua\n")

                        elif ataque_squirtle == "C":
                            print("¡Tsunamiiii!")
                            vida_pikachu -= 17
                            print("A pikachu le han aquitado 17 de vida por Tsunami\n")
                        elif ataque_squirtle == "N":
                            print("Squirtle no hace nada...")

                        if vida_squirtle < 0:
                            vida_squirtle = 0
                        if vida_pikachu < 0:
                            vida_pikachu = 0

                        barra_vida_pikachu = int((TAMANIO_BARRA * vida_pikachu) / VIDA_INICIAL_PIKACHU)
                        barra_vida_squirtle = int((TAMANIO_BARRA * vida_squirtle) / VIDA_INICIAL_SQUIRTLE)
                        print("PIKACHU: [{}{}] Vida: ({}/{})".format("*" * barra_vida_pikachu,
                                                                     " " * (TAMANIO_BARRA - barra_vida_pikachu),
                                                                     vida_pikachu, VIDA_INICIAL_PIKACHU))
                        print("SQUIRTLE: [{}{}] Vida: ({}/{})\n\n".format("*" * barra_vida_squirtle,
                                                                          " " * (TAMANIO_BARRA - barra_vida_squirtle),
                                                                          vida_squirtle,
                                                                          VIDA_INICIAL_SQUIRTLE))

                        input("Enter para continua el combate...")
                        os.system("cls")

                    if vida_squirtle < vida_pikachu:
                        os.system("cls")
                        print("                        Pikachu GANA!!!!")
                    else:
                        os.system("cls")
                        print("                        Squirtle GANAAAAA!!!!!!!")
                        win=True
                        victories += 1
                        map_objects.remove(objet_in_cell)









            if obstacle_definition[cordinate_y][cordinate_x] == "#":
                 char_to_draw = "██"

            print("{}".format(char_to_draw),end="")

        print("║")

    print("╚"+"═" * MAP_WIDTH *2+"╝")
    print("Numero de victorias: {}".format(victories))
    #Ask user where he wants to move
    #direction = input("¿Donde te quieres mover? [WASD]: ")

    direction= readchar.readchar().decode()
    new_position=None

    #Moverme hacia arriba
    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1) % MAP_WIDTH]

    # Moverme hacia abajo
    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1) % MAP_WIDTH]

    #Moverme hacia izquierda
    elif direction == "a":
        new_position = [(my_position[POS_X] - 1) % MAP_WIDTH, my_position[POS_Y]]

    #Moverme hacia derecha
    elif direction == "d":
        new_position = [(my_position[POS_X] + 1) % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "q":
        end_game = True

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            pokemons.insert(0, my_position.copy())
            pokemons = pokemons[:victories]
            my_position= new_position



if win:
    print("GANASTE")

