import os
import random

import readchar as readchar

POS_X=0
POS_Y=1

NUM_MAP_OBJECTS = 11

obstacle_definition = """\
#################           #############
                                      ###
########################       ###       
########################         ###     
########                                 
########################           ####  
####################                  ## 
#########              #######           
###############                          
##################################   ####
####               ##                    
#######                   #####          
#######    ########                      
####       #########       #####         
###############################          \
"""



tail_length = 0
tail = []
my_position = [5,1]
map_objects= []

end_game = False
died = False



#Create obstacle map
obstacle_definition = [list(row) for row  in obstacle_definition.split("\n")]
print(obstacle_definition)
MAP_WIDTH = len(obstacle_definition[0])
MAP_HEIGHT = len(obstacle_definition)






#MAIN LOOP
while not end_game:

    os.system("cls")
    # Generete random objebs in the maps
    while len(map_objects) < NUM_MAP_OBJECTS:
        new_position = [random.randint(0, MAP_WIDTH - 1), random.randint(0, MAP_HEIGHT - 1)]

        if new_position not in map_objects and new_position != my_position and \
            obstacle_definition [new_position[POS_Y]][new_position[POS_X]] != "#" :
            map_objects.append(new_position)


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
                    char_to_draw = " *"
                    objet_in_cell = map_object

            #Aqui pinto la cola
            for tail_piece in tail:
                if tail_piece[POS_X] == cordinate_x and tail_piece[POS_Y] == cordinate_y:
                    char_to_draw = " ■"
                    tail_in_cel = tail_piece


            #Aqui dibujo la posicion del jugador
            if my_position[POS_X] == cordinate_x and my_position[POS_Y] == cordinate_y:
                char_to_draw = " ¥"

                if objet_in_cell :
                    map_objects.remove(objet_in_cell)
                    tail_length += 1

                if tail_in_cel:
                    end_game = True
                    died = True
            if obstacle_definition[cordinate_y][cordinate_x] == "#":
                 char_to_draw = "##"

            print("{}".format(char_to_draw),end="")

        print("║")

    print("╚"+"═" * MAP_WIDTH *2+"╝")
    print("Tu puntuación es: {}".format(tail_length))
    #Ask user where he wants to move
    #direction = input("¿Donde te quieres mover? [WASD]: ")

    direction= readchar.readchar().decode()
    new_position=None

    #Moverme hacia arriba
    if direction == "w":
        new_position = [my_position[POS_X], (my_position[POS_Y] - 1)  % MAP_WIDTH]

    # Moverme hacia abajo
    elif direction == "s":
        new_position = [my_position[POS_X], (my_position[POS_Y] + 1)  % MAP_WIDTH]

    #Moverme hacia izquierda
    elif direction == "a":
        new_position = [(my_position[POS_X] - 1)  % MAP_WIDTH, my_position[POS_Y]]

    #Moverme hacia derecha
    elif direction == "d":
        new_position = [(my_position[POS_X] + 1)  % MAP_WIDTH, my_position[POS_Y]]

    elif direction == "q":
        end_game = True

    if new_position:
        if obstacle_definition[new_position[POS_Y]][new_position[POS_X]] != "#":
            tail.insert(0, my_position.copy())
            tail = tail[:tail_length]
            my_position= new_position



if died:
    print("Has muerto...")

