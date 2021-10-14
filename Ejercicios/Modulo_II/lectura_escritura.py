import os 
SALIDA = "SALIR"


def preguntar_producto_usuario():
    return input("Introduce un producto [{} para salir]: ".format(SALIDA))


def main():
    nombre_lista= input("¿Qué nombre llevara esta lista? ")
    lista_compra= []
    input_usuario= preguntar_producto_usuario() 
    while input_usuario != SALIDA:
        os.system("cls")
        lista_compra.append(input_usuario)
        print(nombre_lista)
        print ("\n".join(lista_compra))
        input_usuario= preguntar_producto_usuario()
    pasar_texto= open("{}.txt".format(nombre_lista), "w") # w es modo escritura (w = write)
    pasar_texto.write("\n".join(lista_compra))
    pasar_texto.close()


if __name__ == "__main__":
    main()
