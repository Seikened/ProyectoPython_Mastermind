import  string
texto_del_usuario= input("Introdusca el texto")
letras_mayusculas=0

for letra in texto_del_usuario:
    if letra in string.ascii_uppercase:
        letras_mayusculas += 1

print("las letars mayusculas son {}".format(letras_mayusculas)