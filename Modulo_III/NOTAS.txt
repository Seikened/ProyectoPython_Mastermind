from requests_html import HTMLSession
import random
from speak_and_listen import listen, speak


def main():
    #speak("Bienvenido al precio justo, vamos a intentar adivinar el precio de algunos productos")
    session = HTMLSession()
    main_site = session.get("https://www.officedepot.com.mx/")
    categories = main_site.html.find(".item-menu-quaternary")
    category = random.choice(categories)

    while category.text == "Papel Cascaron":
        category = random.choice(categories)

    product_page = session.get(category.url[0])#,category.html["href"])
    products = product_page.html.find(".product-item")

    product = random.choice(products)
    imagen_src = product.find(".picture-product", first=True).attrs["src"]
    product_name = product.find(".contnet-name ", first=True).text
    product_price = product.find(".discountedPrice-grid cont-price-grid bp-original").text
    print(float(product_price.replace("$", "").replace(",",".")))



    







if __name__ == '__main__':
    main()
