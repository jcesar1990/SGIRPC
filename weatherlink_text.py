import paths
from os import close, remove, write
import os
import time  
from datetime import date, datetime, timedelta
import shutil 
from shutil import copy2, copytree, copy, move
import glob
import pandas as pd

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
    fecha_weatherlink=now

    #Se escribe una funcion para dar formato a la fecha
    def current_date_format(date):
        months = ("Junuary", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
        day = date.strftime('%d').lstrip("0")
        month = months[date.month - 1]
        year = date.year
        messsage = "{},{},,{},/,".format(day, month, year)

        return messsage



    fecha_portal_weatherlink=(current_date_format(fecha_weatherlink))
    print(fecha_portal_weatherlink)

    fecha_reemplazo=fecha.strftime('%d/%m/%Y ')
    print(fecha_reemplazo)

    with open(filetxt1,'r',encoding='utf8') as lines, open(filetxt2,'w',encoding='utf-8') as output:
        for line in lines: #Lee cada linea una por una 
            if line.strip(): #Si encuentra una linea vacia la elimina
                output.write(line)


    with open(filetxt2,'r+',encoding='utf-8') as datos:
        contenido=datos.read()
        text0=contenido.replace('Last updated:','fechaHora')
        text1=text0.replace('Barometer','presionBar')
        text2=text1.replace('Temperature','temperatura')
        text3=text2.replace('Humidity','humedadRelativa')
        text4=text3.replace('Wind Speed','velocidadViento')
        text5=text4.replace('Wind Direction','direccionViento')
        text6=text5.replace('Heat Index','HeatIndex')
        text7=text6.replace('THSW Index','THSWIndex')
        text8=text7.replace('Wind Chill','WindChill')
        text9=text8.replace('Dew Point','DewPoint')
        text10=text9.replace('Solar Radiation','SolarRadiation')
        text11=text10.replace('Avg velocidadViento','AvgWindSpeed')
        text12=text11.replace('Wind Gust Speed','WindGustSpeed')
        text13=text12.replace('Current','Value,Current')
        text14=text13.replace('Wet Bulb','WetBulb')
        text15=text14.replace('Rain & ET','Rain&ET')
        text16=text15.replace(' ',',')
        text17=text16.replace(',°C','')
        text18=text17.replace(',%','')
        text19=text18.replace(',km/h','')
        text20=text19.replace(',mm/h','')
        text21=text20.replace(',mm','')
        text22=text21.replace(',W/m2','')
        text23=text22.replace(',hPa','')
        text24=text23.replace(fecha_portal_weatherlink, fecha_reemplazo)
        print('Texto editado')
        print(text24)

    with open(filetxt2,'w') as new:
        new.write(text24)

    # df=pd.read_csv(filetxt2,header=None, encoding='utf-8',delimiter=',')
    # dfTransposed=df.T
    # print(dfTransposed)


try:
    test=weatherlinktext('LALADRILLERA')
except Exception as e:
    print('ERROR:',e)