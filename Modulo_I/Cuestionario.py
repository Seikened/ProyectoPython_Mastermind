nombre = input("Como te llamas: ")
titulo="Este es un test de cuanto conoces de Minecraft"

print("-"*len(titulo)+"\n"+" Genial ", nombre, "\n",titulo,"\n"+"-"*len(titulo)+"\n")
print("Mientras mas preguntas aciertes aumentara tu puntaje\n")
score = 0
# Primera pregunta
print("Primer pregunta")
pregunta_1 = input("¿Cual de estos mobs no les gusta el agua?\n"
             "A - Zombie\n"
             "B - Enderman\n"
             "C - Esqueleto\n"
             "Escribe una respuesta:  ")
# Primera pregunta
if pregunta_1 == "A":
    score += 0
    print("\n""O no te as equibocado\n")

elif pregunta_1 == "B":
    score += 20
    print("\n""En hora buena has asertado\n")

elif pregunta_1 == "C ":
    score += 0
    print("\n""O no te as equibocado\n")
else: print("Las opciónes posibles son A,B o C")

print("\n Tu puntuacion es:", score, "\n")


# Segunda pregunta
print("Segunda pregunta")
pregunta_2 = input("¿Que es el nether?\n"
             "A - El infierno de Minecraft\n"
             "B - El mundo donde enpezamos\n"
             "C - La ultima dimension a la que bamos\n "
             "Escribe una respuesta:  ")

if pregunta_2 == "A":
    score += 20
    print("\n""En hora buena has asertado\n")

elif pregunta_2 == "B":
    score += 0
    print("\n""O no te as equibocado\n")

elif pregunta_2 == "C":
    score += 0
    print("\n""O no te as equibocado\n")
else: print("Las opciónes posibles son A,B o C")


print("\n Tu puntuacion es:", score, "\n")


#Tercer pregunta
print("Tercer y ultima pregunta\n")
pregunta_3 = input("¿En que dimencion matamos al ender dragon?\n"
             "A - En el End\n"
             "B - En el Nether\n"
             "C - En el overworld\n"
             "Escribe la respuesta:   ")

if pregunta_3 == "A":
    score += 20
    print("\n""En hora buena has asertado\n")

elif pregunta_3 == "B":
    score += 0
    print("\n""O no te as equibocado\n")

elif pregunta_3 == "C":
    score += 0
else: print("Las opciónes posibles son A,B o C")



#Comparación score
if score == 60:
    print("Eres todo un pro tienes una puntuacion perfecta.\n"
             "Tu puntuacion es:", score)

elif score == 40:
    print("Eres bueo conoses Minecraft pero te falta aprender mas.\n"
              "Tu puntacion es", score)

elif score == 20:
    print("No conoses casi nada del juego. \n"
             "Tu puntuacion es", score)

elif score == 0:
    print("No conoses el juego.\n"
            "Tu puntuación es", score)




exit()