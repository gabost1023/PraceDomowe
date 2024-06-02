import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#import danych z excela
xlsx = pd.ExcelFile('imiona.xlsx')
data = pd.read_excel(xlsx, header=0)
df = pd.DataFrame(data)
print(df)

#wyswietl tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
print(df[df['Liczba']>10000])

#tylko rekordy gdzie nadane imię jest takie jak Twoje
print(df[df['Imie']=='GABRIELA'])

#sumę wszystkich urodzonych dzieci w całym danym okresie
print(df['Liczba'].sum())

#sumę dzieci urodzonych w latach 2000-2005
lata = df[(df['Rok'] >= 2000) & (df['Rok'] <= 2005)]
print(lata['Liczba'].sum())

#sumę urodzonych chłopców i dziewczynek
chlopcy = df[(df['Plec'] == 'M')]
dziewczynki = df[(df['Plec'] == 'K')]
print('Chlopcy i dziewczynki: ', chlopcy['Liczba'].sum(), dziewczynki['Liczba'].sum())

#najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok)
popularne = df.loc[df.groupby(['Rok','Plec'])['Liczba'].idxmax()]
print(popularne)

#najbardziej popularne imię dziewczynki i chłopca w całym danym okresie
popularne = df.loc[df.groupby(['Plec'])['Liczba'].idxmax()]
print(popularne)

