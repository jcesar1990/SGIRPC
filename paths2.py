#Librerias
import os
#Credenciales
#Weatherlink
User="SGIRPC"
Password="sgirpc2023"
#Paths
def makedir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("El directorio " + path + " ha sido creado")
    else:
        print("El directorio " + path + " ya existe")

principal='C:\\Users\\meteorologia\\'
file=principal+'Documents\\files\\'
tempo=principal+'Documents\\temporal\\'
save=principal+'Documents\\save\\'
screenshot=principal+'Documents\\screenshot'

makedir(principal)
makedir(file)
makedir(tempo)
makedir(save)
makedir(screenshot)

#Drivers
drivers=principal+'Documents\\drivers\\'
makedir(drivers)
# NOTA: Hasta el dia de hoy 15\\04\\2024 la version de chrome para linux estable con webdriver es la 114
# Chromedriver se puede descargar desde la siguiente liga  
# https:\\\\chat.openai.com\\c\\61d07157-c3d1-4808-adc5-6e1e0cbbf06f
chromedriver=drivers+'chromedriver-win64\\chromedriver-win64\\chromedriver.exe'
# Para poder usar firefox driver hay que descargar el complemento geckodriver desde la siguiente liga 
# https:\\\\github.com\\mozilla\\geckodriver\\releases
firefoxdriver=drivers+'geckodriver-v0.34.0-win-aarch64\\geckodriver.exe'
# Para poder usar opera driver hay que descargar el complemento de opera desde la siguiente liga 
# https://github.com/operasoftware/operachromiumdriver/releases
operadriver=drivers+'operadriver_win64\\operadriver.exe'
print(operadriver)