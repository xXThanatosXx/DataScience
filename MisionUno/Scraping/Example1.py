from bs4 import BeautifulSoup
import requests, csv, re
from datetime import datetime

date = datetime.today().date()
print(str(date))
URL = "https://apewisdom.io/all-crypto/"
#product__item__top__title js-algolia-product-click js-algolia-product-title

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
criptos = soup.find_all("div", class_="company-name")
criptos = str(criptos)

criptos = criptos.replace('<div class="company-name">','|')


criptos = criptos.replace('</div>,','|')
print(criptos)
# criptos = criptos.replace('[','')
# criptos = criptos.replace('</div>]','')
# criptos = criptos.replace(' ','')
# criptoclean = criptos.split("|")

# print("------------------------------")
# #clean empty data from the list
# criptoclean[:] = [x for x in criptoclean if x]
# print(criptoclean)
# with open('Info.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=',')
#     writer.writerow(criptoclean)