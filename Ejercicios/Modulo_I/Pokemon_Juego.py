from random import randint
import os

VIDA_INICIAL_PIKACHU = 80
VIDA_INICIAL_SQUIRTLE = 90

vida_pikachu = VIDA_INICIAL_PIKACHU
vida_squirtle = VIDA_INICIAL_SQUIRTLE
TAMANIO_BARRA=25




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


    if vida_squirtle<0:
        vida_squirtle=0
    if vida_pikachu<0:
        vida_pikachu=0

    barra_vida_pikachu = int((TAMANIO_BARRA * vida_pikachu) / VIDA_INICIAL_PIKACHU)
    barra_vida_squirtle = int((TAMANIO_BARRA * vida_squirtle) / VIDA_INICIAL_SQUIRTLE)
    print("PIKACHU: [{}{}] Vida: ({}/{})".format("*" * barra_vida_pikachu, " " * (TAMANIO_BARRA - barra_vida_pikachu),
                                                 vida_pikachu, VIDA_INICIAL_PIKACHU))
    print("SQUIRTLE: [{}{}] Vida: ({}/{})\n\n".format("*" * barra_vida_squirtle,
                                                      " " * (TAMANIO_BARRA - barra_vida_squirtle), vida_squirtle,
                                                      VIDA_INICIAL_SQUIRTLE))

    input("Enter para continua el combate...")
    os.system("cls")


    # TURNO DE SQUIRTLE###############################################################################################
    print("\n\n               TURNO DE SQUIRTLE\n")

    # Elección de ataque por el usuario
    ataque_squirtle = None
    while ataque_squirtle not in ["A","B", "C","N"]:
        ataque_squirtle = input("[A] Chorro de agua \n[B] Bola de agua \n[C] Tsunami \n[N] No hacer nada \n")

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


    if vida_squirtle<0:
        vida_squirtle=0
    if vida_pikachu<0:
        vida_pikachu=0

    barra_vida_pikachu = int((TAMANIO_BARRA * vida_pikachu) / VIDA_INICIAL_PIKACHU)
    barra_vida_squirtle = int((TAMANIO_BARRA * vida_squirtle) / VIDA_INICIAL_SQUIRTLE)
    print("PIKACHU: [{}{}] Vida: ({}/{})".format("*" * barra_vida_pikachu, " " * (TAMANIO_BARRA - barra_vida_pikachu),
                                                 vida_pikachu, VIDA_INICIAL_PIKACHU))
    print("SQUIRTLE: [{}{}] Vida: ({}/{})\n\n".format("*" * barra_vida_squirtle,
                                                      " " * (TAMANIO_BARRA - barra_vida_squirtle), vida_squirtle,
                                                      VIDA_INICIAL_SQUIRTLE))

    input("Enter para continua el combate...")
    os.system("cls")

if vida_squirtle < vida_pikachu:
    os.system("cls")
    print("                        Pikachu GANA!!!!")
else:
    os.system("cls")
    print("                        Squirtle GANAAAAA!!!!!!!")
