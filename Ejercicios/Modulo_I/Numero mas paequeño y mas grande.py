
#numeros=[]
#numero_mas_pequeño=0
#numero_mas_grande=0

#numero_elejido = int(input("Introduce un numero: "))
#numeros.append(numero_elejido)
#while True:
#    numero_elejido = int(input("Si deseas salir [Q]\nIntroduce otro numero: "))
#    if numero_elejido == "Q":
#        break
#for number in numeros
 #   if number == int:


lista_introducida = input("Introduce una lista de numeros separados por comas (1,2,34,55,etc): ")
#Aqui se vuelve en uno solo ytodo compacto la lista de los numeros que se limpiaran y pasaran de ser string a int
numeros_de_usuario= [int(numero) for numero in lista_introducida.split(",")]

numero_mas_pequenio = numeros_de_usuario[0]
numero_mas_grande = numeros_de_usuario[0]
                                 #Filtrado de lista, evita que comience desde el cero ejemplo [1,3] ve las posiciones del uno al 3
for numero in numeros_de_usuario [1:]:
    if numero_mas_pequenio > numero:
        numero_mas_pequenio=numero

    if numero_mas_grande < numero:
        numero_mas_grande=numero


print("De estos numeros: {}\nEl mas garnde es: {} \nY el mas chico es:{}".format(numeros_de_usuario,numero_mas_grande,numero_mas_pequenio))

