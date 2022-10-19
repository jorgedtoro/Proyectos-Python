import os
import sys
import shutil
import time
from random import randint

#ruta de las pcps
ruta_pcps= "C:/Users/jorge/El Corte Inglés, S.A/División 21 - Documentos/0.PLANIFICACION/0.COLABORACIONES/152/2021/"
# ruta_mes ="C:/Users/jorge/El Corte Inglés, S.A/División 21 - Documentos/0.PLANIFICACION/0.COLABORACIONES/152/2021/05.MAYO/"

mes_Inicio=['202101','202102','202103','202104','202105','202106','202107'
            '202108','202109','202110','202111','202112']

#leer mes en el fichero

def buscaMes():
    for archivo in os.listdir(ruta_pcps):
        #nombre_archivo = os.path.splitext(archivo)
        startLoc = 4
        añoInicio = archivo.find("2021")
        endLoc = añoInicio ++ 6
        #si quiero empezar desde una posición concreta uso startloc
        #añoInicio = archivo[startLoc:].find("2021") #cuenta empezando por cero y cuenta espacios
        fecha = archivo[añoInicio:endLoc]
        #print(fecha)
        if fecha == '202101':
            mes= '01.ENERO'
            shutil.move(ruta_pcps+archivo, ruta_pcps + "/" + mes + "/" + archivo)
        if fecha == '202102':
            mes= '02.FEBRERO'
            shutil.move(ruta_pcps+archivo, ruta_pcps + "/" + mes + "/" + archivo)
        if fecha == '202103':
            mes= '03.MARZO'
            shutil.move(ruta_pcps+archivo, ruta_pcps + "/" + mes + "/" + archivo)        
        if fecha == '202104':
            mes= '04.ABRIL'
            shutil.move(ruta_pcps+archivo, ruta_pcps + "/" + mes + "/" + archivo)
        if fecha == '202105':
            mes= '05.MAYO'
            shutil.move(ruta_pcps+archivo, ruta_pcps + "/" + mes + "/" + archivo)
        if fecha == '202106':
            mes= '06.JUNIO'
            shutil.move(ruta_pcps+archivo, ruta_pcps + "/" + mes + "/" + archivo)
        if fecha == '202107':
            mes= '07.JULIO'
            shutil.move(ruta_pcps+archivo, ruta_pcps + "/" + mes + "/" + archivo)    
        if fecha == '202108':
            mes= '08.AGOSTO'
            shutil.move(ruta_pcps+archivo, ruta_pcps + "/" + mes + "/" + archivo)
        if fecha == '202109':
            mes= '09.SEPTIEMBRE'
            shutil.move(ruta_pcps+archivo, ruta_pcps + "/" + mes + "/" + archivo)
        if fecha == '202110':
            mes= '10.OCTUBRE'
            shutil.move(ruta_pcps+archivo, ruta_pcps + "/" + mes + "/" + archivo)
        if fecha == '202111':
            mes= '11.NOVIEMBRE'
            shutil.move(ruta_pcps+archivo, ruta_pcps + "/" + mes + "/" + archivo)
        if fecha == '202112':
            mes= '12.DICIEMBRE'
            shutil.move(ruta_pcps+archivo, ruta_pcps + "/" + mes + "/" + archivo)

buscaMes()


