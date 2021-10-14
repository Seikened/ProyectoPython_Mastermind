def pars(numb):
    resultados_pars = []
    for n in numb:
        if n % 2 == 0:
            resultados_pars.append(n)

    return resultados_pars



def nones(numb):
    
    result_none= []
    for n in numb:
        if n % 2 != 0:
            result_none.append(n)

    return result_none



def main():
    serie_num_user =[]
    stay=True
    seguir=None
    while seguir != "N":
        serie_num_user.append(int(input("Digita un sumero:  ")))
        seguir=(input("seguir  [S/N]: "))
        
    (print("De la lista de numeros pares: {}".format(pars(serie_num_user))))
    (print("De la lista de numeros impares: {}".format(nones(serie_num_user))))


if __name__ == "__main__":
    main()