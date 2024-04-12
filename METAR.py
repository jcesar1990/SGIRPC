import paths
import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService

# Function to create directories
def makedir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("El directorio " + path + " ha sido creado")
    else:
        print("El directorio " + path + " ya existe")

# Directories
pathestaciones = "../estaciones"
pathfiles = "../files"

makedir(pathestaciones)
makedir(pathfiles)

# URLs and file paths
url = "https://aviationweather.gov/data/metar/?id=MMMX&hours=48&include_taf=yes"
fileoutmmmx = paths.file+"MMMX.txt"
fileoutmmsm = paths.file+"MMSM.txt"

# Selenium configuration
chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument("--disable-gpu")  # Necessary on some systems
chrome_options.add_argument("--window-size=1920,1080")  # Window size
driver_path = paths.chromedriver
service = ChromeService(executable_path=driver_path)

# Create a Selenium WebDriver instance
driver = webdriver.Chrome(service=service, options=chrome_options)

# Access the page with Selenium
driver.get(url)
print("Acceso a la página...")
driver.find_element(By.XPATH,'//*[@id="main-display"]/div[2]/div[4]/div[1]/label')\
    .click()
print("Deseleccionamos TAF")
driver.find_element(By.XPATH,'//*[@id="go_btn"]')\
    .click()
print("Load data")
time.sleep(5)


# Wait for the element with id "data-container" to be present in the DOM from MMMX
data_containermmmx = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'data-container'))
)

# Print the content of the div
print(data_containermmmx.text)

# Save the data to the text file
with open(fileoutmmmx, 'w', encoding='utf-8') as file:
    file.write(data_containermmmx.text)

print("Los datos se han guardado en el txt", fileoutmmmx)

# Find the datapicker
driver.find_element(By.XPATH,'//*[@id="id"]')\
    .clear()
time.sleep(2)

# Enter ID from Santa Lucia Airport
driver.find_element(By.XPATH,'//*[@id="id"]')\
    .send_keys("MMSM")

time.sleep(5)

driver.find_element(By.XPATH,'//*[@id="go_btn"]')\
    .click()
print("Load data")
time.sleep(10)

# Wait for the element with id "data-container" to be present in the DOM from MMMX
data_containermmsm = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'data-container'))
)

# Print the content of the div
print(data_containermmsm.text)

# Save the data to the text file
with open(fileoutmmsm, 'w', encoding='utf-8') as file:
    file.write(data_containermmsm.text)

print("Los datos se han guardado en el txt", fileoutmmsm)

# Close the browser
driver.quit()