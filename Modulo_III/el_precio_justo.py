from requests_html import HTMLSession
import random
from speak_and_listen import listen, speak


def main():
    #speak("Bienvenido al precio justo, vamos a intentar adivinar el precio de algunos productos")
    session = HTMLSession()
    main_site = session.get("https://www.officedepot.com.mx/")
    categories = main_site.html.find(".item-menu-quaternary")
    
    for a in range(1000):
        category = random.choice(categories)
        while category.text == "Papel Cascaron":
            print("Toco Papel Cascaron")
            category = random.choice(categories)
        print(category.text)






if __name__ == '__main__':
    main()
