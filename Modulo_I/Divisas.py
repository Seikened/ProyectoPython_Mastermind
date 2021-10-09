titulo="CONVERSOR DE DIVISAS"
print("-"*len(titulo)+"\n",titulo,"\n"+"-"*len(titulo)+"\n")
dolar_euro=0.91
libra_euro=1.18
opcion=input("¿Qué divisa elijes?\n"
             "A) - Convertir de Dolar a Euro\n"
             "B) - Convertir de Euro a Dolar\n"
             "C) - Convertir de Lbra a Euro\n"
             "D) - Convertir de Euro a Libra\n")

text_user= "--Introdusca la cantidad de {} a convertir-- \n"



#Convertir de Dolar a Euro
if opcion== "A":
    monto_a_convertir = float(input(text_user.format("dolares")))
    print(monto_a_convertir,"Dolares equivalen a: {}".format(monto_a_convertir*dolar_euro),"Euros")

# Convertir de Euro a Dolar
elif opcion== "B":
    monto_a_convertir = float(input(text_user.format("euros")))
    print(monto_a_convertir, "Euros equivalen a: {}".format(monto_a_convertir/dolar_euro), "Dolares")

# Convertir de Lbra a Euro
elif opcion=="C":
    monto_a_convertir = float(input(text_user.format("libras")))
    print(monto_a_convertir, "Lbras equivalen a: {}".format(monto_a_convertir*libra_euro), "Euros")

# Convertir de Euro a Libra
elif opcion=="D":
    monto_a_convertir = float(input(text_user.format("euros")))
    print(monto_a_convertir, "Euros equivalen a: {}".format(monto_a_convertir/libra_euro), "Lbras")

# Nada
else: print("Por favor selecciona una de las 4 opciones de arriba (A, B, C o D)")

