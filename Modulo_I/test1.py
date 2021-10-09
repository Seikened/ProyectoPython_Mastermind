nombre=(input("Cual es tu nombre? "

              ))
print("Vale, ahora dime 3 número y yo te dire el mayor y el menor, ¿Va?")
n1=int(input("Introduce el primero número: "))
n2=int(input("Introduce el segundo número: "))
n3=int(input("Introduce el tercer número: "))
UPPER=max(n1,n2,n3)
LOWER=min(n1,n2,n3)
print("¡Gracias! Aquí están los resultados...")
print(nombre," el número mas grande entre {}, {} y {}  es {} \n"
              "y el numero mas pequeño es {}".format(n1,n2,n3,UPPER,LOWER))


