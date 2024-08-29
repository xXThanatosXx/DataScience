from bs4 import BeautifulSoup
import requests, csv, re
from datetime import datetime

# Obtención de la fecha actual
date = datetime.today().date()
print(str(date))

# Define las URLs de las páginas web que deseas analizar
URL = "https://www.compulago.com/tienda/computo/"  # Cambia a la nueva URL



page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# Extracción de los nombres de las criptomonedas
# Modifica la clase y etiqueta en función de la estructura HTML de la nueva web
criptos = soup.find_all("div", class_="elementor-widget-heading")  # Cambia a la clase correcta (elementor-element,elementor-widget-heading)
criptos = [cripto.text.strip() for cripto in criptos]

# Limpieza adicional si es necesario
criptoclean = [x for x in criptos if x]
print("###########")
print(criptoclean)

# # Guardar los nombres de las  en un CSV
# with open('Computadores.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=',')
#     writer.writerow(criptoclean)

with open('computadores_dos.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(criptoclean)
