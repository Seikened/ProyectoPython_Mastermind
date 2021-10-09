
def main(imprimir):
    longest_string_value=0
    longest_string=0
    stay=True
    input_string=[]
    while stay:
        input_string.append(input("Introduce un texto:  "))
        for char in input_string:
            if char != "Q": #Verifica que no salga del ciclo cada una de las entradas 
                value=len(char)
                s_string=char

                for val in char:
                    if value >= longest_string_value:

                        longest_string_value = value
                        longest_string=s_string

            else:
                stay=False
    
    imprimir=(print("Esta palabra con mas caracteres: - {} - \nTiene un valor de:  {}caracteres".format(longest_string, longest_string_value)))
    return imprimir

start=None
if __name__ == "__main__":
    start=input("Vamos a escribir algo:  ")
    main(start)