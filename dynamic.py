from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time
 
# set up Chrome options for headless mode
options = webdriver.ChromeOptions()
options.add_argument('--headless=new')


# instantiate Chrome WebDriver with options
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)


# load target website
url = 'https://www1.upme.gov.co/sipg/Paginas/Estructura-precios-combustibles.aspx#k=#l=3082'
driver.get(url)


# scroll to the bottom of the page three times
scroll_times = 3
for _ in range(scroll_times):
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
    time.sleep(1)  # wait for content to load


# select elements by XPath
product_names = driver.find_elements(By.XPATH, '//*[@class="RefinementName"]')
product_name_texts = [product_name.text for product_name in product_names]


# print the product names
print(product_name_texts)


# close the browser
driver.quit()
