from operator import index
from textwrap import indent
import pandas as pd
import numpy as np
import os
import sys
import shutil
import time
from random import randint
import xlrd
import openpyxl
# copyright Jorge de Toro de Murga #

# ruta de las pcps
ruta_pcps = "C:/Users/67075622/El Corte Inglés, S.A/DEPARTAMENTO 152 - Documentos/CONTROL DE REBAJAS/promos macro/"

ventas = pd.read_excel(
    "C:/Users/67075622/El Corte Inglés, S.A/DEPARTAMENTO 152 - Documentos/CONTROL DE REBAJAS/Ventas.xlsx")
# ruta_pcps = "C:/Users/67075622/Desktop/Carpetas/PCPS/"
# os.listdir(ruta_pcps)
ventas['REFERENCIA'] = ""

for f in ventas.index:
    ventas['REFERENCIA'][f] = str(
        ventas['Uneco'][f]) + str(ventas['Familia de Mercancías'][f]) + str(ventas['barra'][f])

print(ventas['REFERENCIA'])

df = pd.DataFrame()

# junta todas las pcps del directorio


for archivo in os.listdir(ruta_pcps):
    df = df.append(pd.read_excel(ruta_pcps+archivo,
                   sheet_name='PLANTILLA VISTEX'), ignore_index=True)

df['REFERENCIA'] = ""

for f in df.index:
    df['REFERENCIA'][f] = str(df['UNECO'][f]) + \
        str(df['FAMILIA'][f]) + str(df['REFDES'][f])
    fechaI = df['FCHAINI'][f]
    fechaf = df['FCHAFIN'][f]
    fechaIv = ventas['Fecha Venta']
    if fechaIv >= fechaI and fechaIv <= fechaf:
        df3 = pd.merge(df['REFERENCIA'][f], ventas['Unidades Estándar Terminada'],
                       left_on=df['REFERENCIA'][f], right_on=ventas['REFERENCIA'])

# df3 = pd.merge(df, ventas['Unidades Estándar Terminada'],
#                left_on=df['REFERENCIA'], right_on=ventas['REFERENCIA'])


ruta_salida = "C:/Users/67075622/El Corte Inglés, S.A/DEPARTAMENTO 152 - Documentos/CONTROL DE REBAJAS/"
writer = pd.ExcelWriter(
    ruta_salida + "Total Escenarios.xlsx", engine='xlsxwriter')
df3.to_excel(writer, sheet_name='Promociones')
writer.save()
