from bs4 import BeautifulSoup
import requests
import re

source = requests.get('https://tienda.mimo.com.ar/mimo/junior/ropa-para-ninas.html').text

soup = BeautifulSoup(source, 'lxml')

for name_product, old_price, special_price in zip(soup.select('h3.titprod'),
                                                  soup.select('span[id^="old-price"]'),
                                                  soup.select('span[id^="product-price"]')):
    print(f'Name: {name_product.text.strip()} |  Old price = {old_price.text.strip()} | Discounted price = {special_price.text.strip()}')

# for article in soup.find_all('h3', {'class': 'titprod'}):
#    print(article.text)