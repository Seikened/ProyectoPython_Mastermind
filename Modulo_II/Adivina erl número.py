from random import randint

def rand():
    rand_numb = randint(1,101)
    return rand_numb




def main():
    num_user= 0
    guest_number= rand()
    num_user = int(input("Adivina el numero: "))
    while num_user != guest_number:

        num_user = int(input("No adivinaste otra vez: "))
    

    print("El numero ganador es: {} \nY tu introdujiste {}, es decir, ganaste".format(guest_number, num_user))


if __name__ == "__main__":
    main()