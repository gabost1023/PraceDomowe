import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importowanie danych csv
data = pd.read_csv('zamowienia.csv', header=0, sep=';', decimal='.')
df = pd.DataFrame(data)
print(df)

#wyswietl listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame)
print(df['Sprzedawca'].unique())

#5 najwyższych wartości zamówień
print(df['Utarg'].sort_values(ascending=False).head(5)) #tutaj same wartosci utargu
print(df.sort_values(by='Utarg', ascending=False).head(5)) #tutaj cale wiersze

#ilość zamówień złożonych przez każdego sprzedawcę
print(df['Sprzedawca'].value_counts())

#sumę zamówień dla każdego kraju
print(df.groupby('Kraj')['Utarg'].sum())

#sumę zamówień dla roku 2005, dla sprzedawców z Polski
# Konwersja kolumny 'Data zamowienia' na typ daty
df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
filtr = df[(df['Kraj'] == 'Polska') & (df['Data zamowienia'].dt.year == 2005)]
print(filtr['Utarg'].sum())

#średnią kwotę zamówienia w 2004 roku
filtr = df[df['Data zamowienia'].dt.year == 2004]['Utarg'].mean()
print(filtr)

#zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.csv
dane_2004 = df[df['Data zamowienia'].dt.year == 2004]
dane_2005 = df[df['Data zamowienia'].dt.year == 2005]

dane_2004.to_csv('zamowienia_2004.csv', index=False)
dane_2005.to_csv('zamowienia_2005.csv', index=False)



