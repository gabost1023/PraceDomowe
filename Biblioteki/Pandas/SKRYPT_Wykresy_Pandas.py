import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#WYKRES LINIOWY NA PODSTAWIE SERII DANYCH
ts = pd.Series(np.random.randn(1000))
#funkcja biblioteki pandas generująca skumulowaną sumę kolejnych elementów
ts = ts.cumsum()
print(ts)
ts.plot()
plt.show()

# WYKRES KOLUMNOWY Z PANDAS DATAFRAME
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia', 'Polska'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia', 'Warszawa'],
        'Kontynent': ['Europa', 'Azja', 'Ameryka Południowa', 'Europa'],
        'Populacja': [11190846, 1303171035, 207847528, 38675467]}

df = pd.DataFrame(data)
print(df)

grupa = df.groupby(['Kontynent']).agg({'Populacja': ['sum']})
print(grupa)

wykres = grupa.plot.bar()
wykres.set_ylabel('Mld')
wykres.set_xlabel('Kontynent')
wykres.tick_params(axis='x', labelrotation=0)
wykres.legend()
wykres.set_title('Populacja z podzialem na kontynenty')
#zmiana kierunku tekstu etykiet słupków plt.xticks(rotation=0)
plt.savefig('Wykresy.png')
plt.show()

#WCZYTANIE DANYCH Z PLIKU I ZGRUPOWANIE WARTOSCI, WYKRES KOLOWY
df = pd.read_csv('dane.csv', header=0, sep=";", decimal=".")
print(df)
grupa = df.groupby(['Imię i nazwisko']).agg({'Wartość zamówienia':["sum"]})

#wykres kolowy z wartościami procentowymi sformatowanymi z dokładnością do 2 miejsc po przecinku
# #figsize ustawia wielkość wykresu w calach, domyślnie [6.4, 4.8]

grupa.plot(kind='pie', subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6,6), colors=['red', 'green'])
plt.legend(loc='lower right')
plt.title('Suma zamowienia dla sprzedawcy')
plt.show()

#WYKRES 1 Z DODATKOWA SREDNIA KROCZACA
ts = pd.Series(np.random.randn(1000))
ts = ts.cumsum()
#rzutowanie Series na DataFrame
df = pd.DataFrame(ts, columns=['wartości'])
print(df)
# dodanie nowej kolumny i wykorzystanie funkcji rolling do stworzenia kolejnych wartości średniej kroczącej
df['Średnia krocząca'] = df.rolling(window=50).mean()
df.plot()
plt.legend()
plt.show()