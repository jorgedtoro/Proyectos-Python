import pandas as pd 
import os


path_1 = "C:/Users/67075622/OneDrive - El Corte Inglés, S.A/pricing/Apple/"
path = "C:/Users/67075622/El Corte Inglés, S.A/División 21 - Documentos/PRICING/Pricing/Jorge y Noelia/Ficheros en excel/"
file1 = "Portfolio Apple.xlsx"

ficheros = os.listdir(path)

apple= pd.read_excel(path_1 + file1)

lista=[]

for archivo in ficheros:
    lista.append(archivo)



for archivo in lista:

    csv2 = pd.read_excel(path + archivo)
    #csv2[["My id","Competitor's Name","Competitor's price", "Fecha"]] = csv2[["My id","Competitor's Name","Competitor's price", "Fecha"]].astype(str)
    
    #csv3 = csv2[["My id","Competitor's Name","Competitor's price", "Fecha"]]
     
    all_data = pd.merge(apple, csv2, on='My id', how='left')


print(all_data.head(10))

all_data.to_excel(path_1 + 'output.xlsx')

#print(lista)

# for fich in lista:

#     csv2 = pd.read_csv(path + archivo, sep=';', error_bad_lines=False)
#     csv3 = csv2[["My id","Competitor's Name","Competitor's price", 'Fecha']]
#     #writer = pd.ExcelWriter(path + archivo, engine='xlsxwriter')
#     csv3.to_excel(path + fich +'.xlsx')
#     #writer.save()
