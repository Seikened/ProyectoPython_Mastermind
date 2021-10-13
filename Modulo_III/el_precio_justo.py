from requests_html import HTMLSession
import random
from speak_and_listen import listen, speak


def main():
    #speak("Bienvenido al precio justo, vamos a intentar adivinar el precio de algunos productos")
    session = HTMLSession()
    main_site = session.get("https://www.officedepot.com.mx/")
    categories = main_site.html.find(".item-menu-quaternary")
    category = random.choice(categories)

<<<<<<< HEAD
    kicks_items = ["Papel Cascaron"]

    while category.text == kicks_items:
        category = random.choice(categories) #Esto es para saltar estos elementos

    for link in (category.absolute_links):
        product_page = session.get(link)
        print(link)

    products = product_page.html.find(".product-item")

    product = random.choice(products) #Selecciona aleatoriamente un producto

    for image in (product.find(".lazy", first=True).html):

        imagen_src = "https://www.officedepot.com.mx/" + image
        

    for items in chrome_history:
        results = re.findall(
            "https://www.instagram.com/([A-Za-z0-9_.-]+)/+$", items[2])
        if results and results[0] not in ["fer_leonfranco"]:  # FILTRO
            profiles_visited.append(results[0])







    product_name = product.find(".contnet-name ", first=True).text
    product_price = product.find(".discountedPrice-grid cont-price-grid bp-original").text
    print(float(product_price.replace("$", "").replace(",",".")))



    







if __name__ == '__main__':
    main()
