from requests_html import HTMLSession
import random
from speak_and_listen import listen, speak
import re



def obtain_link_image (product):
    image = product.find(".lazy", first=True).html #Dejo que todo lo que contiene html se filtre por medio de un regular expression
    results = str(re.findall("/medias/[A-Za-z0-9-/./?=]+", image)).replace("[","").replace("'","").replace("]","") #La regular expression
    

    main_link = "https://www.officedepot.com.mx"
    imagen_src = main_link + (results)
    print(imagen_src)
    return imagen_src



def main():
    #speak("Bienvenido al precio justo, vamos a intentar adivinar el precio de algunos productos")
    session = HTMLSession()
    main_site = session.get("https://www.officedepot.com.mx/")
    categories = main_site.html.find(".item-menu-quaternary")
    category = random.choice(categories)


    kicks_items = ["Papel Cascaron"]

    while category.text == kicks_items:
        category = random.choice(categories) #Esto es para saltar estos elementos

    for link in (category.absolute_links):
        product_page = session.get(link)
        

    products = product_page.html.find(".product-item")

    
    while True:
        try:
            product = random.choice(products) #Selecciona aleatoriamente un producto
            break
        except IndexError:
            product = random.choice(products)
            pass


    obtain_link_image(product)      

    product_name = product.find(".contnet-name ", first=True).text
    product_price = product.find(".discountedPrice-grid cont-price-grid bp-original").text
    print(float(product_price.replace("$", "").replace(",",".")))



    







if __name__ == '__main__':
    main()
