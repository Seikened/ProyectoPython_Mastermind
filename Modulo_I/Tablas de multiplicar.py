
numero_elegido_a_multiplicar= int(input("Elije el numero para su tabla de multiplicar"))
rango_de_la_tabla= int(input("Introduce el rango hasta el cual deseas que el numero {} se multiplique".format(numero_elegido_a_multiplicar)))

for numero in range(1,rango_de_la_tabla+1):
    #if numero % 2 == 0:
     print("{} x {} = {}".format(numero_elegido_a_multiplicar,numero,(numero*numero_elegido_a_multiplicar)))