import paths
import os
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.opera.options import Options as OperaOptions

# URLs and file paths
url = url = "https://aviationweather.gov/data/metar/?id=MMMX&hours=48"
fileoutmmmx = paths.file+"MMMX.txt"
fileoutmmsm = paths.file+"MMSM.txt"

# Selenium configuration with chrome. 
# NOTA: Hasta el dia de hoy 15/04/2024 la version de chrome para linux estable con webdriver es la 114
# Chromedriver se puede descargar desde la siguiente liga  
# https://chat.openai.com/c/61d07157-c3d1-4808-adc5-6e1e0cbbf06f
# Selenium configuration with chrome
#web_options = ChromeOptions()
# Selenium configuration with firefox
#web_options = FirefoxOptions()
# Selenium configuration with opera
web_options = OperaOptions()
web_options.add_argument('--headless')
web_options.add_argument("--disable-gpu")  # Necessary on some systems
web_options.add_argument("--window-size=1920,1080")  # Window size
# Webdriver localpath
# Para poder usar firefox driver hay que descargar el complemento geckodriver desde la siguiente liga 
# https://github.com/mozilla/geckodriver/releases


# Create a selenium WebDriver instance with chrome
#Service = ChromeService(executable_path=paths.chromedriver)
#driver = webdriver.Chrome(service=Service, options=web_options)

# Create a selenium WebDriver instance with firefox
#Service = FirefoxService(executable_path=paths.firefoxdriver)
#driver = webdriver.Firefox(service=Service, options=web_options)

# Create a Selenium WebDriver instance with opera
driver = webdriver.Opera(executable_path=paths.operadriver, options=web_options)
# Create a Selenium WebDriver instance from network
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),chrome_options=web_options)

# Access the page with Selenium
driver.get(url)
print("Acceso a la página...")
driver.find_element(By.XPATH,'//*[@id="main-display"]/div[2]/div[4]/div[1]/label')\
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

