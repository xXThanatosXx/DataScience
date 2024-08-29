from selenium import webdriver
from bs4 import BeautifulSoup

# Configuración de Selenium
driver = webdriver.Chrome()  # Asegúrate de que tienes el ChromeDriver configurado
driver.get("https://www.alkosto.com/computadores-tablet/c/BI_COMP_ALKOS")  # Cambia a la URL específica

# Espera a que la página cargue completamente
driver.implicitly_wait(10)  # Espera hasta 10 segundos

# Obtén el contenido HTML
page_content = driver.page_source
soup = BeautifulSoup(page_content, "html.parser")

# A partir de aquí, el código de scraping sigue siendo el mismo
productos = soup.find_all("li", class_="ais-InfiniteHits-item")
print(productos)  # Imprime la lista de elementos de productos encontrados

driver.quit()  # Cierra el navegador al finalizar
