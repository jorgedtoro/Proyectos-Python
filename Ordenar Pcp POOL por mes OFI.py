import os
import sys
import shutil
import time
from random import randint

# ruta de las pcps
ruta_pcps = "Y:/COMPRAS/SALIDA/DIV 21/INFORMATICA/152/PCP/2022/"
#ruta_mes ="C:/Users/jorge/El Corte Inglés, S.A/División 21 - Documentos/0.PLANIFICACION/0.COLABORACIONES/152/2021/05.MAYO/"

mes_Inicio = ['202201', '202202', '202203', '202204', '202205', '202206', '202207'
              '202208', '202209', '202210', '202211', '202212']

# leer mes en el fichero


def buscaMes():
    for archivo in os.listdir(ruta_pcps):
        #nombre_archivo = os.path.splitext(archivo)
        #startLoc = 4
        añoInicio = archivo.find("2022")
        endLoc = añoInicio + + 6
        # si quiero empezar desde una posición concreta uso startloc
        # añoInicio = archivo[startLoc:].find("2021") #cuenta empezando por cero y cuenta espacios
        fecha = archivo[añoInicio:endLoc]
        # print(fecha)
        if fecha == '202201':
            mes = '01.ENERO'
            shutil.move(ruta_pcps+archivo, ruta_pcps +
                        "/" + mes + "/" + archivo)
        if fecha == '202202':
            mes = '02.FEBRERO'
            shutil.move(ruta_pcps+archivo, ruta_pcps +
                        "/" + mes + "/" + archivo)
        if fecha == '202203':
            mes = '03.MARZO'
            shutil.move(ruta_pcps+archivo, ruta_pcps +
                        "/" + mes + "/" + archivo)
        if fecha == '202204':
            mes = '04.ABRIL'
            shutil.move(ruta_pcps+archivo, ruta_pcps +
                        "/" + mes + "/" + archivo)
        if fecha == '202205':
            mes = '05.MAYO'
            shutil.move(ruta_pcps+archivo, ruta_pcps +
                        "/" + mes + "/" + archivo)
        if fecha == '202206':
            mes = '06.JUNIO'
            shutil.move(ruta_pcps+archivo, ruta_pcps +
                        "/" + mes + "/" + archivo)
        if fecha == '202207':
            mes = '07.JULIO'
            shutil.move(ruta_pcps+archivo, ruta_pcps +
                        "/" + mes + "/" + archivo)
        if fecha == '202208':
            mes = '08.AGOSTO'
            shutil.move(ruta_pcps+archivo, ruta_pcps +
                        "/" + mes + "/" + archivo)
        if fecha == '202209':
            mes = '09.SEPTIEMBRE'
            shutil.move(ruta_pcps+archivo, ruta_pcps +
                        "/" + mes + "/" + archivo)
        if fecha == '202210':
            mes = '10.OCTUBRE'
            shutil.move(ruta_pcps+archivo, ruta_pcps +
                        "/" + mes + "/" + archivo)
        if fecha == '202211':
            mes = '11.NOVIEMBRE'
            shutil.move(ruta_pcps+archivo, ruta_pcps +
                        "/" + mes + "/" + archivo)
        if fecha == '202212':
            mes = '12.DICIEMBRE'
            shutil.move(ruta_pcps+archivo, ruta_pcps +
                        "/" + mes + "/" + archivo)


buscaMes()
