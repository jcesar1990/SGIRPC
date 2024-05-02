import paths
import os
import shutil
import json
import requests
import urllib, urllib3
import csv
from datetime import date, datetime
import pandas as pd


def conagua(parametro):
    try:    
        print('Inicio de programa CONAGUA para descargar',parametro)
        # Insertamos la fecha
        now=datetime.now()
        fecha=(now.strftime('%d-%m-%y'))
        fechahora=(now.strftime('%d-%m-%y %H:%M'))
        print(fecha)
        print(fechahora)
        #URL's
        urltemp = 'https://smn.conagua.gob.mx/tools/PHP/sivea_v3/php/getTemperatura.php?per=T'
        urlpre = 'https://smn.conagua.gob.mx/tools/PHP/sivea_v3/php/getPrecipitacion.php?per=B30'
        urlwind = 'https://smn.conagua.gob.mx/tools/GUI/sivea_v3/php/getViento.php?per=T30'
        file = paths.file+'CONAGUA'+parametro+'.json'
        filecsv =  paths.file+'CONAGUA'+parametro+'.csv'
        csvsave =  paths.file+'CONAGUA'+parametro+fecha+'.csv'
        
        if parametro == 'temperatura':
            url=urltemp
        elif parametro == 'velocidad':
            url=urlwind
        elif parametro == 'precipitacion':
            url=urlpre
        
        print(url)

        #Descarga del json del portal de CONAGUA
        r = urllib.request.urlopen(url)
        f = open(file,'wb')
        f.write(r.read())
        f.close()
        print(file)
        print('JSON de CONAGUA obtenido')

        def extraer_variables(file):
            with open(file) as contenido:
                variables = json.load(contenido)
                for valores in variables:
                    fechalocal=(valores.get("fecha_local"))
                    estado=(valores.get("estado")) 
                    estacion=(valores.get("nombre_estacion"))
                    valor=(valores.get(parametro))
                    longitud=(valores.get("longitud"))
                    latitud=(valores.get("latitud"))
                    extraccion=(f"{fechalocal},{estado},{estacion},{valor},{longitud},{latitud}")
                    print(extraccion)
                    #Si el archivo csv no existe, lo crea, en caso de existir, conctatenara los nuevos datos
                    if not os.path.exists(filecsv):
                        with open(filecsv,'w',newline='') as csvfile:
                            csv_writer=csv.writer(csvfile)
                            csv_writer.writerow(['fecha', 'localidad', 'estacion', parametro, 'longitud', 'latitud'])
                            csv_writer.writerow([fechalocal, estado, estacion, valor, longitud, latitud])
                        print('Archivo guardado')
                    else:
                        with open(filecsv, 'a', newline='') as csvfile:
                            csv_writer = csv.writer(csvfile)
                            csv_writer.writerow([fechalocal, estado, estacion, valor, longitud, latitud])
                            shutil.copy(filecsv,csvsave)
                        print('Datos añadidos al archivo existente')
                    
        extraer_variables(file) 
    # Archivo de errores
    except Exception as e:
        error_message = str(e)
        direrror0 = os.path.join(paths.message,fecha+'-ERROR.csv')
        direrror1 = os.path.join(paths.tempo,fecha+'-ERROR1.csv')
        direrror2 = os.path.join(paths.tempo,fecha+'-ERROR2.csv')
        
        # Crear DataFrame vacío si el archivo de error no existe
        # Nombre de las columnas
        namecolumns=['fechaHora','programa', 'parametro', 'alerta', 'descripcion']
        # Codigo de error
        #message = f"{fechahora},{parametro},ERROR,{error_message}"
        message = [fechahora, 'CONAGUA' , parametro, 'ERROR', error_message]
        print(message)
        print('Generando archivo de error en el directorio de error')
        # Crear el archivo de error y guardar el DataFrame
        if not os.path.exists(direrror0):
            #Se abre el archivo error
            with open(direrror0,'a',newline='') as origen:
                writer=csv.writer(origen)
                #Se escriben los nombres de las columnas
                writer.writerow(namecolumns)
                #Agregando datos
                writer.writerow(message)
        elif os.path.exists(direrror0):
            with open(direrror0,'a') as existente:
                writer=csv.writer(existente)
                writer.writerow(message)


temperaturas=conagua("temperatura")
lluvias=conagua("precipitacion")
vientos=conagua("velocidad")
