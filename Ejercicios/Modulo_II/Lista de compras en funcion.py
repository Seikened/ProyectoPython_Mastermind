
def list():
    lista=["Soya","Frijoles","Pan"]
    while True:
        input_usuario = input("\n[Q] Para salir \n¿Que desea comprar?\nR= ")
        if input_usuario=="Q":
            break
        elif input_usuario in lista:
            print("{} ya esta en tu lista".format(input_usuario))
        else:
            if input("\n[Enter para continuar...] \n¿Seguro que quiere añadir {} a la lista?".format(input_usuario)) == "SI":
                lista.append(input_usuario)
                print("{} Se ha añadido a tu lista".format(input_usuario))
    return lista



def main():
    
    keep_list=True
    full_list=list()  
    print("La lista de la compra es:\n")
    for final_list in full_list:
        
        print(final_list)




if __name__ == "__main__":
    main()