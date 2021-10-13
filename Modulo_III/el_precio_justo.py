from requests_html import HTMLSession
import random
from speak_and_listen import listen, speak
import re



def obtain_link_image (product):
    
    image = product.find(".lazy", first=True).html #Dejo que todo lo que contiene html se filtre por medio de un regular expression
    results = str(re.findall("/medias/[A-Za-z0-9-/./?=]+", image)).replace("[","").replace("'","").replace("]","") #La regular expression
    

    main_link = "https://www.officedepot.com.mx"
    imagen_src = main_link + (results)
    return imagen_src

def obtain_price(product):

    p = str(product.find(".product-item", first=True).text)         #float(.replace("[","").replace("'","").replace("]","" 
    price = (p.replace("\n","/").replace("{","").replace("[","").replace("]","").replace("}",""))

    final_price = (str(re.findall("/[$0-9.]+", price)).replace("/","").replace("$","").split("."))
    product_price = float((final_price[0].replace("[", "").replace("'", "").replace("]", "")))
    return product_price

def random_pruduct(products):
    
    product = random.choice(products)
    return product
            
    

def black_list(categories):
    
    kicks_items = ["Papel Cascaron"]
    category = random.choice(categories)
    while category.text == kicks_items:
        category = random.choice(categories) #Esto es para saltar estos elementos
    return category
    
    

def main():
    #speak("Bienvenido al precio justo, vamos a intentar adivinar el precio de algunos productos")
    session = HTMLSession()
    main_site = session.get("https://www.officedepot.com.mx/")
    categories = main_site.html.find(".item-menu-quaternary")
    
    
    for link in (black_list(categories).absolute_links):
        product_page = session.get(link)
    
    
    #Todos los productos de la categoria
    products = product_page.html.find(".product-item")
    #Selecciona aleatoriamente un producto    
    product= random_pruduct(products)

    long = len(obtain_link_image(product))
    #Obtengo la imagen del producto
    print("-"*long,"\n"+obtain_link_image(product))    
    #Obtengo el nombre del producto
    product_name = product.find(".contnet-name ", first=True).text
    print("\n"+ product_name)
    #Obtengo el precio del producto
    print("\n", obtain_price(product), "\n","-"*long)


    numero = listen()
    print(numero)



    pass
    
if __name__ == '__main__':
    main()
