import os

SALIDA = "Q"

products=["leche","cereal","arandanos","frijoles","lentejas","huevos"]

def preguntar_producto_usuario():
    product_selected=input("Introduce un producto [{} para salir]: ".format(SALIDA))
    while product_selected.lower() not in products and product_selected != SALIDA:
        print("Este producto no esta, intenta con otro")
        product_selected=input("Introduce un producto [{} para salir]: ".format(SALIDA))
    return product_selected
    

    

def crear_archivo(name,lista_compra):
    
    #pasar_texto= open(name+".txt", "w") # w es modo escritura (w = write)
    #pasar_texto.write("\n".join(lista_compra))
    #pasar_texto.close()

    with open(name+".txt","w") as mi_archivo:
        mi_archivo.write("\n".join(lista_compra))

    #NO ocupo poner .close() pues mi fichero al estar ententado 4 a dentro al salir de esto me dice que ya no estoy trabajando dentro del archivo avierto

    print("Se ha creado el archivo {} con exito!!!".format(name))






def main():
    nombre_lista= input("¿Qué nombre llevara esta lista? ")
    lista_compra= []
    input_usuario= preguntar_producto_usuario() 
    while input_usuario != SALIDA:
        os.system("cls")
        lista_compra.append(input_usuario)
        print("--------",nombre_lista.upper(),"--------")
        print ("\n".join(lista_compra))
        input_usuario= preguntar_producto_usuario()
    crear_archivo(nombre_lista,lista_compra)


if __name__ == "__main__":
    main()
