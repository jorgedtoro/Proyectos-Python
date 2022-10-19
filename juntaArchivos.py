import os
import sys
import shutil
import time
from random import randint
import pandas as pd

#ruta_pcps= "C:/Users/67075622/El Corte Inglés, S.A/División 21 - Documentos/PRICING/Pricing/Jorge y Noelia/Noviembre 2020/"
ruta_pcps= "C:/Users/67075622/El Corte Inglés, S.A/División 21 - Documentos/PRICING/Pricing/Jorge y Noelia/Ficheros tratados/"
ruta_salida = "C:/Users/67075622/Desktop/Ficheros tratados/"

lista = ["amazon.es", "mediamarkt.es", "elcorteingles_es"]

df = pd.DataFrame()

# -----------------------Introduce la fecha del fichero:-----------------------------------------------------

for archivo in os.listdir(ruta_pcps):
    Inicio = archivo.find("2020")
    endLoc = Inicio ++ 10
    fecha = archivo[Inicio:endLoc]

    csv_input = pd.read_csv(ruta_pcps+archivo, sep=";")
    csv_input['Fecha'] = fecha
    csv_input.to_csv(ruta_pcps + archivo, index=False)

archivo = "back_2020_12_01_08_44_Default_Export.csv"
df = pd.read_csv(ruta_pcps + archivo,sep=",")

#-------------------------Quito los competidores que no interesan------------------------------------------

for archivo in os.listdir(ruta_pcps):
    df = pd.read_csv(ruta_pcps + archivo,sep=",")
    df = df[df["Competitor's Name"].isin(lista)]
    df.to_csv(ruta_salida+archivo, sep=",")
    
#------------------------Junta los archivos -------------------------------------------------------------------------

for archivo in os.listdir(ruta_pcps):
    
    df = df.append(pd.read_csv(ruta_pcps + archivo, sep=",", error_bad_lines=False),ignore_index=True)
          
df.to_csv(ruta_salida + archivo, index=False)


print(df)        

#ruta_salida = "C:/Users/67075622/El Corte Inglés, S.A/División 21 - Documentos/PRICING/Pricing/Jorge y Noelia/Diciembre 2020/"
#writer = pd.ExcelWriter(ruta_salida + "Total precios.xlsx", engine='xlsxwriter')
#df.to_excel(ruta_salida,engine='xlsxwriter')
#writer.save()