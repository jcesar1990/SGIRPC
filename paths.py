#Librerias
import os
#Credenciales
#Weatherlink
User=
Password=
#Paths
def makedir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("El directorio " + path + " ha sido creado")
    else:
        print("El directorio " + path + " ya existe")

principal='/home/cesar/Documents/Estaciones/'
file=principal+'files/'
tempo=principal+'temporal/'
save=principal+'save/'
screenshot=principal+'screenshot/'
message=principal+'error/'

makedir(principal)
makedir(file)
makedir(tempo)
makedir(save)
makedir(screenshot)
makedir(message)

#Drivers
drivers=principal+'drivers/'
makedir(drivers)
# NOTA: Hasta el dia de hoy 15/04/2024 la version de chrome para linux estable con webdriver es la 114
# Chromedriver se puede descargar desde la siguiente liga  
# https://chat.openai.com/c/61d07157-c3d1-4808-adc5-6e1e0cbbf06f
chromedriver=drivers+'chromedriver-linux64/chromedriver-linux64/chromedriver-exe'
# Para poder usar firefox driver hay que descargar el complemento geckodriver desde la siguiente liga 
# https://github.com/mozilla/geckodriver/releases
firefoxdriver=drivers+'geckodriver-v0.34.0-linux-aarch64/geckodriver-exe'
