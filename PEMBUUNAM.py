# Importamos las librerías necesarias
import time
from datetime import datetime
from datetime import date, datetime, timedelta,timezone
import ModuloPEMBU
import threading

def timer(timer_runs):
    while timer_runs.is_set():

        try:
            ModuloPEMBU.proceso("ICAyCC")
        except:
            print("Hubo un problema al descargar los datos de esta estación")
            continue

        try:
            ModuloPEMBU.proceso("ccha")
        except:
            print("Hubo un problema al descargar los datos de esta estación")
            continue

        try:
            ModuloPEMBU.proceso("cchn")
        except:
            print("Hubo un problema al descargar los datos de esta estación")
            continue

        try:
            ModuloPEMBU.proceso("ccho")
        except:
            print("Hubo un problema al descargar los datos de esta estación")
            continue

        try:
            ModuloPEMBU.proceso("cchs")
        except:
            print("Hubo un problema al descargar los datos de esta estación")
            continue

        try:
            ModuloPEMBU.proceso("cchv")
        except:
            print("Hubo un problema al descargar los datos de esta estación")
            continue

        try:
            ModuloPEMBU.proceso("enp1")
        except:
            print("Hubo un problema al descargar los datos de esta estación")
            continue

        try:
            ModuloPEMBU.proceso("enp2")
        except:
            print("Hubo un problema al descargar los datos de esta estación")
            continue

        try:
            ModuloPEMBU.proceso("enp3")
        except:
            print("Hubo un problema al descargar los datos de esta estación")
            continue

        try:
            ModuloPEMBU.proceso("enp4")
        except:
            print("Hubo un problema al descargar los datos de esta estación")
            continue

        try:
            ModuloPEMBU.proceso("enp5")
        except:
            print("Hubo un problema al descargar los datos de esta estación")
            continue

        try:
            ModuloPEMBU.proceso("enp6")
        except:
            print("Hubo un problema al descargar los datos de esta estación")
            continue

        try:
            ModuloPEMBU.proceso("enp7")
        except:
            print("Hubo un problema al descargar los datos de esta estación")
            continue

        try:
            ModuloPEMBU.proceso("enp8")
        except:
            print("Hubo un problema al descargar los datos de esta estación")
            continue

        try:
            ModuloPEMBU.proceso("enp9")
        except:
            print("Hubo un problema al descargar los datos de esta estación")
            continue

        final=datetime.now()
        print(final)
        time.sleep(30)   # 15 minutos=850.
timer_runs = threading.Event()
timer_runs.set()
t = threading.Thread(target=timer, args=(timer_runs,))
t.start()   