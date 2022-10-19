
import os
from datetime import datetime, date, timedelta
import calendar
import shutil, sys



rutaInfosem= 'C:/LAST/'
rutaFin = 'C:/Users/67075622/El Corte Inglés, S.A/DEPARTAMENTO 152 - Documentos/INFOSEM/'
weekday = datetime.today().weekday()
day = datetime.today()
curr_date = date.today()

#print(calendar.day_name[curr_date.weekday()]) #imprime el nombre del día (Friday

lastDay = day + timedelta(days=-1) 
fecha = lastDay.date()
 
  #  if weekday == 4: #si es lunes, queremos el domingo
  #      lastDay = day + timedelta(days=-1) 
   #     fecha = lastDay.date()
        #Infosem152 = "D152 - " + str(fecha) + ".xlsx"
        #Infosem286 = "D286 - " + str(fecha) + ".xlsx"

    #else:
   #     fecha = "Hoy no es lunes"

infosem152 = 'D152'
infosem286 = 'D286'
infosem152c = infosem152 + " - " + str(fecha) + ".xlsx"
infosem286c = infosem286 + " - " + str(fecha) + ".xlsx"

def copiaInfosem(fecha, infosem152, infosem286,infosem152c,infosem286c):
    
    shutil.copy(rutaInfosem + infosem152 + ".xlsx" , rutaInfosem + infosem152c)
    shutil.copy(rutaInfosem + infosem286 + ".xlsx", rutaInfosem + infosem286c)

def mueveInfosem(infosem152c,infosem286c):
    shutil.move(rutaInfosem + infosem152c, rutaFin + infosem152c)
    shutil.move(rutaInfosem + infosem286c, rutaFin + infosem286c)


copiaInfosem(fecha, infosem152, infosem286,infosem152c,infosem286c)
mueveInfosem(infosem152c,infosem286c)