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

principal='C:/Users/meteorologia/'
file=principal+'Documents/files/'
tempo=principal+'Documents/temporal/'
save=principal+'Documents/save/'
screenshot=principal+'Documents/screenshot'

makedir(principal)
makedir(file)
makedir(tempo)
makedir(save)
makedir(screenshot)

#Drivers
drivers=principal+'Documents/drivers/'
chromedriver=drivers+'chromedriver-win64/chromedriver-win64/chromedriver.exe'