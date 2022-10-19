



#%% [markdown]
# import data
import numpy as np
import pandas as pd

dia = "Epromo_200415.csv"
#ata = pd.read_csv("Epromo_200414.csv", header= 0, encoding= 'unicode_escape')
data = pd.read_csv("Epromo_200414.csv", delimiter=';', header=0)
data.info()
data.head()

# %%
