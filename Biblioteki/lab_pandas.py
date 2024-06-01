import pandas as pd
import numpy as np

s = pd.Series([1,2,3,4, np.nan,6,7,8]) #nan -pusty wiersz
print(s)
s = pd.Series([1,2,3,4,np.nan,6], index=['A', 'B', 'C', 'D', 'E', 'F'])
print(s)
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela','New Delhi', 'Brasilia'],
        'Populacja': [1134234, 42124, 56363]}
df=pd.DataFrame(data)
print(df)
print(df.dtypes)
#df = pd.read_csv('dane.csv', header=0, sep=";", decimal='.')
print(df)
#df.to_csv('plik.csv', index=False)

print(s['B'])
print(s.C)
print(df[0:1]) #wycinanie danych z ramki danych tak samo jak w lisice
print("")
print(df['Populacja'])
print(df.iloc[0,0])
print(df.loc[0,"Kraj"])
print(df.at[0,"Kraj"])
print(df[0:1])
print("")
print(df['Populacja'])
print(df.iloc[0, 0])
print(df.loc[0, 'Kraj'])
print('kraj: ' + df.Kraj)
print(df.sample())

print(df.sample(2))
print(df.sample(frac=0.5))
print(df.sample(n=10, replace=True))
print(df.head())
print(df.head(2))
print(df.tail(1))
print(df.describe())
print(df.T)

print(s[(s>9)])
print(s.where(s>10))
print(s.where(s>10, 'za duże'))
seria = s.copy()
seria.where(seria > 10, 'za duże', inplace=True)
print('########')
print(seria)

print(s[~(s>10)])
print(s[(s<13) & (s>8)])

print(df[(df.Populacja > 1000000) & (df.index.isin([0,2]))])

print('#########')
szukaj = ['Belgia','Brasilia']
print(df.isin(szukaj))

s['e'] = 15
print(s.e)
s['f'] = 16
print(s)

df.loc[3] = 'dodane'
print(df)
df.loc[4] = ['Polska','Warszawa',38675467]
print(df)

new_df = df.drop([3])
print(new_df)

df.drop([3], inplace=True)
print(df)

# df.drop('Kraj', axis=1, inplace=True)
df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']
print(df)

print(df.sort_values(by='Kraj'))
grouped = df.groupby(['Kontynent'])
print(grouped.get_group('Europa'))
print(df.groupby(['Kontynent']).agg({'Populacja':['sum']}))
