import paths
from os import close, remove, write
import os
import time  
from datetime import date, datetime, timedelta
import shutil 
from shutil import copy2, copytree
from shutil import copy
from shutil import move
import glob
from os import remove

def weatherlinktext(estacion):
    filetxt1 = paths.file+estacion+".txt"
    print(filetxt1)
    filetxt2 = paths.file+estacion+"2.txt"
    print(filetxt2)
    filecsv = paths.file+estacion+".csv"
    print(filecsv)



    espacio="-------------"
    now = datetime.now()
    fecha= date.today()
    print(espacio)
    """date"""
    fecha_weatherlink=fecha


    format_temp = fecha_weatherlink.strftime('Día :%d, Mes: %m, Año: %Y, Hora: %H, Minutos: %M, Segundos: %S')
    print(format_temp)


    def current_date_format(date):
        months = ("Junuary", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
        day = date.strftime("%d")
        month = months[date.month - 1]
        year = date.year
        messsage = "{} {},{}".format(day, month, year)

        return messsage


    fecha_final_weatherlink=(current_date_format(fecha_weatherlink))
    print(fecha_final_weatherlink)

    fecha_reemplazo=fecha.strftime('%d/%m/%Y')
    print(fecha_reemplazo)

    with open(filetxt1,'r',encoding='utf8') as lines, open(filetxt2,'w',encoding='utf-8') as output:
        for line in lines: #Lee cada linea una por una 
            if line.strip(): #Si encuentra una linea vacia la elimina
                output.write(line)


    with open(filetxt2,'r+',encoding='utf-8') as datos:
        contenido=datos.read()
        text0=contenido.replace('Last updated:','fechaHora')
        text1=text0.replace('Barometer','presionBar')
        text2=text1.replace('Temperature', 'temperatura')
        text3=text2.replace('Humidity','humedadRelativa')
        text4=text3.replace('Wind Speed','velocidadViento')
        text5=text4.replace('Wind Direction','direccionViento')
        text6 = text5.replace(fecha_final_weatherlink, fecha_reemplazo)
        text7 = text6.replace(' ',',')
        print(text7)
    with open(filecsv,'w') as new:
        rewrite=filecsv(text7)


            
try:
    test=weatherlinktext('LALADRILLERA')
except Exception as e:
    print('ERROR:',e)