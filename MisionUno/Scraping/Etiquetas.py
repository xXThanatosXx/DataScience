from bs4 import BeautifulSoup
import requests
import csv
from datetime import datetime

# Obtención de la fecha actual
date = datetime.today().date()

# Define la URL de la página web que deseas analizar
URL = "https://www.alkosto.com/computadores-tablet/c/BI_COMP_ALKOS"  # Cambia a la URL específica
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")

# Extracción de etiquetas y sus clases
tags_and_classes = []

# Definir las etiquetas HTML que deseas extraer
tags_to_extract = ["title", "h1", "h2", "h3", "div", "p", "span", "meta"]

# Loop sobre las etiquetas definidas para extraer su información
for tag in tags_to_extract:
    elements = soup.find_all(tag)
    for element in elements:
        # Extrae la clase y el contenido de la etiqueta
        tag_class = " ".join(element.get("class", []))  # Une las clases en un solo string
        tag_content = element.text.strip() if element.text else "N/A"
        tags_and_classes.append([tag, tag_class, tag_content])

# Guardar los datos en un archivo CSV
with open('tags_and_classes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Etiqueta", "Clase(s)", "Contenido"])  # Cabeceras del CSV
    writer.writerows(tags_and_classes)

print("Datos guardados en 'tags_and_classes.csv'")
