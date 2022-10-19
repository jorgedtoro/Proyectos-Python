import pandas as pd
import numpy as np
import os
from datetime import datetime, date, timedelta
import locale

#CARGA HOJA DE SEGUIMIENTO
#****************************************************************************************************************************************************************
hoja = pd.ExcelFile("C:/Users/67075622/OneDrive - El Corte Inglés, S.A/Python/152-HOJA DE SEGUIMIENTO VISTEX.xlsx")
hoja.sheet_names
df1 = pd.read_excel(hoja, 'Seguimiento', na_values=['NA'], usecols="B:Z",skiprows=3)

# print(df1.dtypes)

#VARIABLES PARA FILTRO DE FECHA
#****************************************************************************************************************************************************************
#VARIABLES PARA FILTRO DE FECHA
#****************************************************************************************************************************************************************
weekday = datetime.today().weekday()
day = datetime.today()
curr_date = date.today()
month = datetime.now().month
last_month = month -1
year = datetime.now().year

#hay que introducir el último día que queremos que tenga en cuenta
#last_day = "2021-10-01 00:00:00"
last_day = datetime(year,month,1)
print(last_day)
#****************************************************************************************************************************************************************

df2 = df1.loc[(df1['FI'] < last_day) & (df1['FF'] < last_day) & (df1['LIQUIDADO'] == "NO") & (df1['PERIODIFICAR'] > 0)]
# df2['PERIODIFICAR'] == df2['PERIODIFICAR'] * -1

df3 = df2[['PROVEEDOR', 'PROMOCIÓN', 'PERIODIFICAR']]
print(df2.head())
df3.head()

totalP = df3['PERIODIFICAR'].sum(axis=0)
#
#'{:20,.2f}'.format(totalPeriodificar)


totalP=abs(totalP)
totalP=round(totalP,2)
locale.setlocale(locale.LC_ALL, '')
locale.currency(totalP)
locale.currency(totalP, grouping=True)
print("*************************************************")
print("La cifra total a periodificar es:", totalP)
#print(totalP)

writer = pd.ExcelWriter("C:/Users/67075622/OneDrive - El Corte Inglés, S.A/Python/PERIODIFICACION.xlsx", engine='xlsxwriter')

df2.to_excel(writer,sheet_name='datos')
df3.to_excel(writer,sheet_name='periodificacion')

writer.save()