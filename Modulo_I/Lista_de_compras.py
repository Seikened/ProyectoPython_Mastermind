lista=[]
input_usuario=None

titulo="Lista de compras"
print("_"* len(titulo)+"\n",titulo,"\n"+"_"* len(titulo)+"\n")

#------------------------------------------------------------------------------------------------------------------
while True:
    input_usuario = input("\n[Q] Para salir \n¿Que desea comprar?\nR= ")
    if input_usuario=="Q":
        break
    elif input_usuario in lista:
        print("{} ya esta en tu lista".format(input_usuario))
    else:
        if input("\n[SI/NO] \n¿Seguro que quiere añadir {} a la lista?".format(input_usuario)) == "SI":
            lista.append(input_usuario)
            print("{} Se ha añadido a tu lista".format(input_usuario))
#------------------------------------------------------------------------------------------------------------------


print("La lista de la compra es:\n")
print(lista)
