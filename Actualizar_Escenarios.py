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


rutaEscenarios = "C:/Users/67075622/El Corte Inglés, S.A/División 21 - Documentos/0.PLANIFICACION/0.COLABORACIONES/152/Pdte Hoja Seguimiento/"
proveedores = pd.read_excel(
    "C:/Users/67075622/El Corte Inglés, S.A/DEPARTAMENTO 152 - Documentos/JT/Proveedores.xlsx")

# print(proveedores)

df = pd.DataFrame()

for archivo in os.listdir(rutaEscenarios):
    df = df.append(pd.read_excel(rutaEscenarios+archivo,
                   sheet_name='RESUMEN'), ignore_index=True)

df1 = pd.DataFrame()
df = df[df['PROMOCIÓN'].notna()]
# df1['VACIO'] = ""
df2 = df.append(df1)

df2 = df2[['PROMOCIÓN', 'FECHA INICIO', 'FECHA FIN', 'MOTIVO', 'PROVEEDOR',
          'FAMILIA', 'MARCA', 'COSTE ECI', 'CARGO ESTIMADO AL PROVEEDOR']]
# print(df2)
df2["MOTIVO"] = "OFERTA"

df3 = pd.merge(df2, proveedores)

df3 = df3[['PROMOCIÓN', 'FECHA INICIO', 'FECHA FIN', 'MOTIVO', 'PROVEEDOR', 'NOMPROV',
          'FAMILIA', 'MARCA', 'COSTE ECI', 'CARGO ESTIMADO AL PROVEEDOR']]
df3 = df3.sort_values("PROMOCIÓN")

df3['PROVEEDOR'] = df3['PROVEEDOR'].astype('str')
for i in df3.index:
    largo = len(df3['PROVEEDOR'][i])
    if largo == 6:
        df3['PROVEEDOR'][i] = "0" + df3['PROVEEDOR'][i]
    if largo == 5:
        df3['PROVEEDOR'][i] = "00" + df3['PROVEEDOR'][i]
    if largo == 4:
        df3['PROVEEDOR'][i] = "000" + df3['PROVEEDOR'][i]
    if largo == 3:
        df3['PROVEEDOR'][i] = "0000" + df3['PROVEEDOR'][i]
    if largo == 2:
        df3['PROVEEDOR'][i] = "00000" + df3['PROVEEDOR'][i]
    if largo == 1:
        df3['PROVEEDOR'][i] = "000000" + df3['PROVEEDOR'][i]


writer = pd.ExcelWriter(
    rutaEscenarios + "Total Escenarios.xlsx", engine='xlsxwriter')
df3.to_excel(writer, sheet_name='Promociones')
writer.save()
