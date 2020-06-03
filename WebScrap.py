from bs4 import BeautifulSoup
import requests
import re

# Source Sites
mimo = 'https://tienda.mimo.com.ar/mimo/junior/ropa-para-ninas.html'
cheeky = ''
grisino = ''


source = requests.get(mimo).text

soup = BeautifulSoup(source, 'lxml')

special_prices_with_defaults_added = []
for sp in soup.select('span[id^="product-price"]'):
    try:
        special_prices_with_defaults_added.append(sp.text.strip().replace('\xa0', ' '))
    except:
        special_prices_with_defaults_added.append("No default price available")

for name_product, old_price, special_price in zip(
        soup.select('h3.titprod'), soup.select('span[id^="old-price"]'), special_prices_with_defaults_added):
    print(
        f'Name: {name_product.text.strip()} |  Old price = {old_price.text.strip()} | Discounted price = {special_price}')

# for name_product, old_price, special_price in zip(soup.select('h3.titprod'),
#                                                   soup.select('span[id^="old-price"]'),
#                                                   soup.select('span[id^="product-price"]')):
#     print(f'Name: {name_product.text.strip()} |  Old price = {old_price.text.strip()} | Discounted price = {special_price.text.strip()}')

# name_product = soup.select('h3.titprod')
# old_price = soup.select('span[id^="old-price"]')
#
# for i in name_product:
#     for j in old_price:
#         print(i.text.strip(), j.text.strip())

# for article in soup.find_all('h3', {'class': 'titprod'}):
#    print(article.text)