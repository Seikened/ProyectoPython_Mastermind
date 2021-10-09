def suma(numeros_suma):
    resultados_suma = 0
    for n in numeros_suma:
        resultados_suma=resultados_suma+n
    return resultados_suma




def main():
    serie_num_user =[]
    stay=True
    seguir=None
    while seguir != "N":
        serie_num_user.append(int(input("Digita un sumero:  ")))
        seguir=(input("seguir  [S/N]: "))
    
    (print("De la lista de numeros: - {} - \nLa suma es:  {}c".format(serie_num_user, suma(serie_num_user))))



if __name__ == "__main__":
    main()