import pandas as pd
import numpy as np

#Pandas series
group = pd.Series([198.34,56.89,74.34,45.97,43.34,75.34,64.56])
group.name="The population"
group.dtype
group.values
group.index
"""
print("The series of 7 groups is : \n", group)
# assigning indices the values
ct = group.index = [
    'Kenya',
    'Uganda',
    'Tanzania',
    'Ethiopia',
    'Somalia',
    'Rwanda',
    'Sudan',
]
print("Countries with their population :\n",ct)

#Assigning index a value in a pandas.Series
groupIndexed = pd.Series([198.34,56.89,74.34,45.97,43.34,75.34,64.56],
                  index = [
    'Kenya',
    'Uganda',
    'Tanzania',
    'Ethiopia',
    'Somalia',
    'Rwanda',
    'Sudan',
])
print("\n",groupIndexed)
# u can use i loc function to access values in a series
print(group.iloc[0]) # printing the first value in the series
print(group.iloc[-1]) # printing the las valuein the series
# slicing also work in pandas
#print(groupIndexed['Kenya':'Tanzania'])
print("The mean is: \n",group.mean())
print("The standard deviation is :\n",group.std())
#conditional selection

print(group[[0,2]].mean())
print(group[(group > group.mean() - group.std() / 2) | (group > group.mean() + group.std() / 2)])
"""


# pandas with dataframes

df = pd.DataFrame({'country':
                   ['kenya',
                    'uganda',
                    'nigeria',
                    'tanzania'],
                    'GDP':[
                        1245678,
                        3456289,
                        2390675,
                        1245789],
                    'surface':[
                        670.45,
                        540.98,
                        345.45,
                        740.33
                    ],
                    'HDI':[
                        0.5645,
                        0.3345,
                        0.7835,
                        0.8956
                    ],
                    'continent':[
                        'Africa',
                        'Europe',
                        'Asia',
                        'America'
                    ]}, columns = ['country','GDP','surface','HDI','continent'])
print(df)

print(" The columns in the dataframe are :\n",df.columns)
print(" The size of the dataframe is: \n",df.size)
print(" The shape is:\n",df.shape)
print(" Describtion of the dataframe is :\n",df.describe())
print(" The information or summary of the dataframe is: \n",df.info())
print(" Getting information of a given index WE USE iloc and loc: \n",df.loc[0],"\n Using iloc \n", df.iloc[-1])
print(" Displaying a given column by identifying the column name : \n",df['GDP'])
print(" Selecting a given column with the range of indices \n",df.loc[0:2,'GDP'])#loc select rows matching the given index
print(" Selecting a given column with the range of indices \n",df.loc[1:4,['GDP','continent']])
print(" Selecting a given column with the range of indices \n",df.iloc[0:3])#iloc works with the position of the index
print(" Selecting a given column with the range of indices \n",df.iloc[0:2,2:4])

# CONDITIONAL SELECTION
#which rows are true to the condition below
print(df['GDP'] > 2000000)
#select rows that satisfies the below condition and display the colums
print(df.loc[df['GDP'] > 2000000])
# select rows that satisfies the condition below and display the values of column "surface" only
print(df.loc[df['GDP'] > 2000000, 'surface'])

#MODIFYING DATAFRAMES IN PANDAS

langs = pd.Series(['Kiswahili','English'],index=[1,2],name="Language")
df['Language'] = langs
print(df)
#Replacing values per columns
new = df.rename(columns={'GDP': 'Gross Value'},
          index={0:'Haron',1:'Mugo',2:'Cypher',3:'Okioma'})
print(new)


#Dropping columns
df.drop(columns=['Language'],inplace=True)
print(df)
#Statistical computing
print(df.head())
surface = df['surface']

print(surface.quantile(.25))
print(surface.median())