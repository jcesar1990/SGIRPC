import paths
import os
import shutil
import json
import requests
import urllib, urllib3
import csv
from datetime import date, datetime
import pandas as pd

# Archivo de errores
def handle_error(programa, parametro, error_message):
    # Insertamos la fecha
    now=datetime.now()
    fecha=(now.strftime('%d-%m-%y'))
    fechahora=(now.strftime('%d-%m-%y %H:%M'))
    print(fecha)
    print(fechahora)
    direrror0 = os.path.join(paths.message,fecha+'-ERROR.csv')
    direrror1 = os.path.join(paths.tempo,fecha+'-ERROR1.csv')
    direrror2 = os.path.join(paths.tempo,fecha+'-ERROR2.csv')

    # Crear DataFrame vacío si el archivo de error no existe
    # Nombre de las columnas
    namecolumns=['fechaHora','programa', 'ERROR','descripcion']
    # Codigo de error
    message = [fechahora, programa , parametro, error_message]
    print(message)
    print('Generando archivo de error en el directorio de error')
    # Crear el archivo de error y guardar el DataFrame
    if not os.path.exists(direrror0):
        # Se abre el archivo error
        with open(direrror0,'a',newline='') as origen:
            writer=csv.writer(origen)
            #Se escriben los nombres de las columnas
            writer.writerow(namecolumns)
            #Agregando datos
            writer.writerow(message)
    # Si el archivo ya existe, agrega la fila con el error
    elif os.path.exists(direrror0):
        with open(direrror0,'a') as existente:
            writer=csv.writer(existente)
            writer.writerow(message)
