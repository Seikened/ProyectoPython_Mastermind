import os

usuarios=["fer","mora","pedro"]
password=["2131","343","pedrito"]
check1=None
check2=None

entrada_ususario=input("Digita tu usuario: ")
if entrada_ususario in usuarios:
    check1=True
entrada_password=input("Digita tu contraseña: ")
if entrada_password in password:
    check2=True


if check1 and check2 == True:
    print("Entraste")
else:
    os.system("cls")
    resitro=input("[SI/NO]\n¿Quieres registrarte en nuestra web? \n")
    if resitro =="SI":
        registro_ususario=input("Digita tu usuario a registrar\n Usuario: ")
        usuarios.append(registro_ususario)

        registro_contrasena=input("Digita tu contraseña a registrar\n Contraseña: ")

        registro_contrasena_confirmación=input("confirma tu contraseña: ")

        while registro_contrasena_confirmación != registro_contrasena:
            registro_contrasena=input("NO cioncidio tu contraseña verifica que sean iguales\n Contraseña: ")
            registro_contrasena_confirmación=input("confirma tu contraseña: ")

        password.append(registro_contrasena)
print("Se registro el usuario {} con exito, su contraseña es: {}".format(registro_ususario,registro_contrasena))


