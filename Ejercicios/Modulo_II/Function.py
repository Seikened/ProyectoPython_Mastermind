from math import sqrt

def exponete(numero_usuario):
    valor_exponete= numero_usuario*numero_usuario
    return valor_exponete


def main():
    pregunta_usuario = int(input("Introduce primer numero: "))
    exponente_inicial = int(input("Introduce segundo numero: "))
    resultado = 0
    if exponente_inicial == " ":
        resultado = exponete(pregunta_usuario)
    else:
        for a in range(exponente_inicial):
             resultado=exponete(pregunta_usuario)

    print("Aqui esta tu resultado de poner en exponente {}: resultado {}".format(pregunta_usuario,resultado))



if __name__ == "__main__":
    main()

