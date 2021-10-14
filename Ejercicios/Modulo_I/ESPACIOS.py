texto_usuario= input("Untroduce un texto: \n")
espacios=0
puntos=0
comas=0
for letra in texto_usuario:
    if letra == " ":
        espacios+=1
    elif letra  == ".":
        puntos+=1
    elif letra == ",":
        comas+=1
print("Espacios: {} \nPuntos: {}\nComas: {}\n".format(espacios,puntos,comas))