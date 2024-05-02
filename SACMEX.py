import paths
from operator import not_
from os import close, remove, write, path
import os
import time  
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
import shutil 
from shutil import copy2, copytree
from shutil import copy
from shutil import move
import glob
from os import remove
import pandas as pd
import numpy as np
import csv
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import threading

def timer(timer_runs):
    while timer_runs.is_set():

        # Ruta del ejecutable del Chrome WebDriver
        ruta_webdriver = paths.chromedriver

        espacio='-------------'

        # Insertamos la fecha
        now=datetime.now()
        fechahora=(now.strftime("%d/%m/%y %H:%M"))
        fechadia=(now.strftime("%d-%m-%y"))
        print(fechadia)
        #Para el script de windows se debe reemplazar / por \\
        #Se eliminan los archivos .dat que puedan existir en la carpeta de descargas para evitar errores al momento de la compilación.
        descargas=paths.tempo+'/'
        tipo="*.dat"
        delite=glob.glob(descargas + tipo)
        for f in delite:
            os.remove(f)
            print("Los archivos .dat fueron eliminados")

        #Definimos los PATHS para los archivos.
        dircsvsacmex0 = paths.tempo+'/SACMEX0.csv'
        dircsvsacmex1 = paths.tempo+'/SACMEX1.csv'
        dirtxtsacmex1 = paths.tempo+'/SACMEX1.txt'
        dircsvsacmex2 = paths.tempo+'/SACMEX2.csv'
        dircsvsacmex3 = paths.tempo+'/SACMEX3.csv'
        dircsvsacmex4 = paths.tempo+'/SACMEX4.csv'
        dircsvsacmex5 = paths.file+'/SACMEX.csv'
        dirsacmex_save= paths.save+'/'+fechadia+'-SACMEX.csv'

        #Copiar el archivo de SACMEX con la tabla en ceros si es que la hora es entre 6:00 y 6:10 horas.
        #Obteniendo la hora actual.
        hora_actual=time.strftime("%H:%M")
        print("La hora actual es:",hora_actual)
        # Se crea un objeto de hora para las 00:00am.
        hora_0 = "00:00"
        hora_principio = time.strftime(hora_0)
        # Se crea un objeto de hora para las 00:00am.
        hora_00 = "00:15"
        hora_final0 = time.strftime(hora_00)
        # Se crea un objeto de hora para las 6:00am.
        hora_1 = "06:00"
        hora_inicio = time.strftime(hora_1)
        print(hora_inicio)
        # Se crea un objeto de hora para las 6:10am.
        hora_2 = "06:10"
        hora_final = time.strftime(hora_2)
        print(hora_final)

        #Si el archivo no existe, generar una tabla inicial para la operación matematica que se hará más adelante.
        if not os.path.exists(dircsvsacmex0):
            # Dataframe de estaciones
            estaciones = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46','47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78']
            nodata=['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
            # Crear un diccionario con los datos
            data = {
            'idEstacion': estaciones,
            'lluvia': nodata
            }

            # Crear el DataFrame a partir del diccionario
            archivo_origen = pd.DataFrame(data)
            #print(archivo_origen)
            archivo_origen.to_csv(dircsvsacmex0, index=False)
            print('El archivo',dircsvsacmex0,'ha sido creado')
        else:
            print('El archivo',dircsvsacmex0,'ya existe')

        #Comprobando la hora, de ser las 6am, se compiara una tabla con los valores de las estaciones en 0mm para evitar algun valor negativo.
        print("Comprobando corte de datos a las 6am")
        if hora_inicio <= hora_actual <= hora_final:
            # Dataframe de estaciones
            estaciones = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37','38','39','40','41','42','43','44','45','46',',47','48','49','50','51','52','53','54','55','56','57','58','59','60','61','62','63','64','65','66','67','68','69','70','71','72','73','74','75','76','77','78']
            nodata=['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
            # Crear un diccionario con los datos
            data = {
            'idEstacion': estaciones,
            'lluvia': nodata
            }

            # Crear el DataFrame a partir del diccionario
            archivo_origen = pd.DataFrame(data)
            #print(archivo_origen)
            archivo_origen.to_csv(dircsvsacmex0, index=False)
            print('El archivo',dircsvsacmex0,'ha sido creado')
        elif hora_inicio != hora_actual != hora_final:
            print("El corte de datos es a las 06:00 am")

        #Comprobando la hora, de ser las 6am, se compiara una tabla con los valores de las estaciones en 0mm para evitar algun valor negativo.
        print("Generando nuevo archivo para concatenar")
        if hora_principio <= hora_actual <= hora_final0:
            # Dataframe de estaciones
            os.remove(dircsvsacmex4)
            print('El archivo',dircsvsacmex4,'fue eliminado')
        elif hora_inicio != hora_actual != hora_final:
            print("Se creara nuevo archivo para concatenar")

        # Se obtiene la fecha con cambio de formato.
        fecha_a= date.today()
        print(fecha_a)

        # Establecemos el parametro de la fecha para despues con el bot colocarla en el datapicker del navegador web.
        # Primero verificamos la fecha para asignar la del día en curso, hay que recordar que el corte de datos es a las 6 am
        print("Estableciendo fechas para la descarga de los al corte")
        now=datetime.now()
        fecha_0=(now.strftime("%d/%m/%Y"))
        fecha_1=now - timedelta(days=1)
        fecha_2=(fecha_1.strftime("%d/%m/%Y"))
        print(fecha_0)
        print(fecha_2)

        # Establecemos el parametro de la fecha de los datos actuales dependiendo de la hora, si la hora actual esta entre las 00:00 y las 06:00 horas, 
        # se seguira obteniendo los datos del dia anterior, despues de las 06:00 horas se obtendran los datos de la fecha en curso.
        print("Comprobando la fecha para la obtención de los datos de la fecha correspondiente al corte.")
        if hora_principio <= hora_actual <= hora_inicio:
            fecha_datapicker=fecha_2
            fecha=fecha_a-timedelta(days=1)
            print("La fecha a colocar en el datapicker de SACMEX es", fecha_datapicker,"debido a que aun no se realiza el corte de los datos")
            print("La fecha del archivo descargado de SACMEX es", fecha,"debido a que aun no se realiza el corte de los datos")
        elif hora_principio != hora_actual != hora_inicio:
            fecha_datapicker=fecha_0
            fecha=fecha_a
            print("La fecha a colocar en el datapicker de SACMEX es", fecha_datapicker,"debido a que ya se realizo el corte de los datos")
            print("La fecha del archivo descargado de SACMEX es", fecha,"debido a que ya se realizo el corte de los datos")

        print(fecha_datapicker)
        print(fecha)

        # Se modifica el formato de la fecha con el mes en texto.
        def current_date_format(date):
            #date tomara la fecha del sistema para despues cambiar las fechas con el formato de message.
            months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
            day = date.strftime("%d")
            month = months[date.month - 1]
            year = date.year
            messsage = "{}{}{}".format(day, month, year)
            #Retornamos el nuevo formato de current_date_format, para usar este nuevo formato debemos mencionarlo al momento de mandar a llamar un date
            return messsage

        #Ya con el nuevo formato para las fechas actualizamos el formato.
        fecha_final_lluvia0=(current_date_format(fecha))
        fecha_final_lluvia=str(fecha_final_lluvia0)
        print(fecha_final_lluvia)


        try:
            # Selenium configuration with chrome. 
            # NOTA: Hasta el dia de hoy 15/04/2024 la version de chrome para linux estable con webdriver es la 114
            # Chromedriver se puede descargar desde la siguiente liga  
            # https://chat.openai.com/c/61d07157-c3d1-4808-adc5-6e1e0cbbf06f
            # Selenium configuration with chrome
            #web_options = ChromeOptions()
            # Selenium configuration with firefox
            web_options = FirefoxOptions()
            # Selenium configuration with opera
            #web_options = OperaOptions()
            #web_options.add_argument('--headless')
            web_options.add_argument('--disable-gpu')  # Necessary on some systems
            web_options.add_argument('--window-size=1920,1080')  # Window size
            web_options.add_argument('--no-sandbox') # Necesari
            web_options.add_argument('--remote-debugging-port=9222')
            # Download path
            download_path = paths.tempo
            prefs = {'download.default_directory': download_path}
            web_options.add_experimental_option('prefs', prefs)

            # Webdriver localpath
            # Para poder usar firefox driver hay que descargar el complemento geckodriver desde la siguiente liga 
            # https://github.com/mozilla/geckodriver/releases


            # Create a selenium WebDriver instance with chrome
            Service = ChromeService(executable_path=paths.chromedriver)
            driver = webdriver.Chrome(service=Service, options=web_options)

            # Create a selenium WebDriver instance with firefox
            #Service = FirefoxService(executable_path=paths.firefoxdriver)
            #driver = webdriver.Firefox(service=Service, options=web_options)
            
            driver.get('http://10.11.11.154/SACMEX/')
            driver.implicitly_wait(60)
            print("Ya en menu")

            # El bot realizara los pasos o clicks a seguir para descargar los datos de la plataforma
            # click en informes
            print("Click en informes")
            driver.find_element(By.CSS_SELECTOR, "#menu > ul > li:nth-child(3) > a")\
                .click()
            # click en isoyetas
            print("Click en isoyetas")
            driver.find_element(By.XPATH, "/html/body/div[4]/div[4]/div[1]/ul/li[7]/a")\
                .click()

            time.sleep(5)

            print("Ventana emergente")
            span=driver.find_element(By.CSS_SELECTOR, "#tab4_7 > iframe")

            driver.switch_to.frame(span)

            print("Selecciona la fecha actual")
            driver.find_element(By.XPATH,"//*[@id='form:calendar_input']")\
                .clear()

            #Si inserta la fecha actual en el datapicker.
            driver.find_element(By.XPATH,"//*[@id='form:calendar_input']")\
                .send_keys(fecha_datapicker)

            #Selecciona descargar en .DAT
            print("Selección del archivo .DAT")
            driver.find_element(By.CSS_SELECTOR,"#form\:j_idt20 > span")\
                .click()
            
            #Tiempo de espera para que salga la nueva ventana de descarga.
            time.sleep(5)
            
            #Selecciona Descargar
            print("Se descarga el archivo")
            driver.find_element(By.XPATH,"//*[@id='formDownload:j_idt31']/span")\
                .click()
            time.sleep(15)

            driver.close()
            # Cerrar la página después de realizar las operaciones necesarias
            driver.quit()

            print("Se obtuvieron los datos del portal de SACMEX")
        except Exception as e:
            print("No fue posible la descarga de los datos de SACMEX")
            print("Error:",e)

        try:
            # Se designa la ruta del archivo recien descargado.
            archivo = descargas+fecha_final_lluvia+'_A.dat'
            print("El .dat es")
            print(archivo)

            
            # Se filtran las columnas y se dejan los valores de lluvia con 2 decimales
            DSACMEX= pd.read_csv(archivo, index_col=0, header=0 , usecols=(0,1))
            print("Se imprime la lectura de las columas filtradas")
            print(DSACMEX)
            roundplaces = np.round(DSACMEX,decimals=2)
            roundplaces.to_csv(dircsvsacmex1)
            print('Datos de SACMEX obtenidos')

            # # Cambiamos los nombres de las columnas

            fecha_3=(now.strftime("%d/%m/%y %H:%M"))
            print(fecha_3)
            SACMEX=open(dircsvsacmex1)
            texto1=SACMEX.read()
            cambio1=texto1.replace("cat", "idEstacion")
            cambio2=cambio1.replace("elev", "lluvia")
            print("imprimiento cambios a nombres de columnas")
            #print(cambio2)
            print("cambios echos")
            SACMEX1=open(dircsvsacmex1, "w")
            SACMEX1.write(cambio2)
            SACMEX.close()
            SACMEX1.close()
            
            print("Se designan los valores de archivo en un dataframe")
            df00=pd.read_csv(dircsvsacmex0, index_col=0)
            df01=pd.DataFrame(df00)
            print("archivo 1")
            print(df01)

            df10=pd.read_csv(dircsvsacmex1, index_col=0)
            df11=pd.DataFrame(df10)
            print("archivo 2")
            print(df11)

            # Operación de resta para obtener el valor del acumulado en deacuerdo al programador de tareas (10 minutos)
            dfn=df11.sub(df01)
            print("resta")
            print(dfn)
            dfn.to_csv(dircsvsacmex2)

            dfr=pd.read_csv(dircsvsacmex2, index_col=0)
            dfr1=pd.DataFrame(dfr)
            dfr1['lluvia']=dfr1['lluvia'].round(2)
            print("Datos redondeados a 2 decima")
            print(dfr1)
            dfr1.to_csv(dircsvsacmex2)


            # Recorre las filas del csv final y en caso de encontrar valores negativos en la columna de mm, los volverá 0.
            print("Se buscan datos negativos a fin de eliminarlos porque debe tratarse de una falla al momento de hacer la resta")
            def reemplazar_negativos(valor):
                if valor < 0:
                    return (0)
                else:
                    return valor

            sacmex=pd.read_csv(dircsvsacmex2, index_col=0) 
            print(sacmex)
            sacmex["lluvia"] = sacmex['lluvia'].apply(reemplazar_negativos)
            sacmex.to_csv(dircsvsacmex2)

            if not os.path.exists(dircsvsacmex3):

                # Dataframe de estaciones
                estaciones = []
                nodata=[]
                # Crear un diccionario con los datos
                data = {
                'idEstacion': estaciones,
                'lluvia': nodata,
                }

                # Crear el DataFrame a partir del diccionario
                archivo_origen = pd.DataFrame(data)
                print(archivo_origen)
                archivo_origen.to_csv(dircsvsacmex3, index=False)
                print('El archivo',dircsvsacmex3,'ha sido creado')
            else:
                print('El archivo',dircsvsacmex3,'ya existe')

            with open(dircsvsacmex2, 'r') as entrada, open(dircsvsacmex3, 'w', newline='') as salida:
                read_csv = csv.reader(entrada)
                write_csv = csv.writer(salida)
                
                for fila in read_csv:
                    fila_modificada = [valor if valor != '' else '0.0' for valor in fila]
                    print(fila_modificada)
                    write_csv.writerow(fila_modificada)
            print('Se eliminan valores negativos en caso de exstir')
            

            sacmex=pd.read_csv(dircsvsacmex3, index_col=0) 
            print(sacmex)

            # Se agrega la columna de fecha y hora CONTINUAR AQUI

            sacmex=pd.read_csv(dircsvsacmex3, index_col=0)
            sacmex['fechaHora']=np.where(sacmex['lluvia'] !='[]', fecha_3, ' ', )
            print(sacmex)
            sacmex.to_csv(dircsvsacmex3)
            shutil.copy(dircsvsacmex3,dircsvsacmex5)

            if not os.path.exists(dircsvsacmex4):
                shutil.copy(dircsvsacmex3,dircsvsacmex4)
                print('Se ha copiado el archivo',dircsvsacmex3,'en',dircsvsacmex4)
            else:
                sacmexdescargado=pd.read_csv(dircsvsacmex3, index_col=0, header=0)
                sacmexanterior=pd.read_csv(dircsvsacmex4, index_col=0, header=0) 
                print('el sacmex descargado es:')
                print(sacmexdescargado)
                print('y el sacmex anterior es:')
                print(sacmexanterior)

                nuevosacmex= pd.concat([sacmexdescargado, sacmexanterior])
                print('Archivo contatenado')
                print(nuevosacmex)
                nuevosacmex.to_csv(dircsvsacmex4)
            shutil.copy(dircsvsacmex4, dirsacmex_save)


            time.sleep(5)
            remove(dircsvsacmex0)
            os.rename(dircsvsacmex1, dircsvsacmex0)
            remove(archivo)
            print("Se han obtenido los datos de SACMEX, asi mismo se ha eliminado el archivo .dat para la siguiente ejecución en 10 minutos")
        except Exception as e:
            print("Se presento una falla con el filtrado de los datos y no se ha eliminado el archivo .dat en este punto")
            print("Error:",e)
        final=datetime.now()
        print(final)

        time.sleep(510)
timer_runs = threading.Event()
timer_runs.set()

t = threading.Thread(target=timer, args=(timer_runs,))
t.start()
