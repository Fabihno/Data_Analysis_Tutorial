import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("data/data.csv")
df1 = pd.read_csv("data/cities.csv", header=None)
print(df.head())


#checking duplicate values using duplicated function
print(df.duplicated())
#splitting colums in a dataframe using split function
df1 = pd.DataFrame({
    'Data':['1945_M_KE_1','1969_M_TZ_1','2010_F_UG_2','2001_M_ET_1','1999_F_SM_1']
})
splitted = df1['Data'].str.split('_',expand=True)
splitted.columns='Year','Sex','Country','Children'
print(splitted)
# plotting graphs in python using csv files
df.plot(kind='hist', x='Duration', y='Calories')
df.plot(kind='scatter', x = 'Pulse', y = 'Maxpulse')
plt.show()