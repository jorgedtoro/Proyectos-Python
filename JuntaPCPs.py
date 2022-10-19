import pandas as pd
#import numpy as np
import os
#import sys
#import shutil
#import time
##from random import randint
#import xlrd
#import openpyxl
# copyright Jorge de Toro de Murga #

#ruta de las pcps
ruta_pcps= "C:/Users/67075622/El Corte Inglés, S.A/DEPARTAMENTO 152 - Documentos/CONTROL DE REBAJAS/promos macro/"
#ruta_pcps = "C:/Users/67075622/Desktop/Carpetas/PCPS/"
#os.listdir(ruta_pcps)

df = pd.DataFrame()

#junta todas las pcps del directorio

    
for archivo in os.listdir(ruta_pcps):
    df = df.append(pd.read_excel(ruta_pcps+archivo, sheet_name='DETALLE'),ignore_index=True)
    
       
    
ruta_salida = "C:/Users/67075622/El Corte Inglés, S.A/DEPARTAMENTO 152 - Documentos/CONTROL DE REBAJAS/"
writer = pd.ExcelWriter(ruta_salida + "Total Escenarios.xlsx", engine='xlsxwriter')
df.to_excel(writer,sheet_name='Promociones')
writer.save()