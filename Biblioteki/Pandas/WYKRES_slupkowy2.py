#Wyświetl na pomocą wykresu słupkowego ilość złożonych zamówień przez poszczególnych sprzedawców (zbiór danych zamówienia.csv).
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('zamowienia.csv', header=0, sep=";", decimal=".")
df = pd.DataFrame(data)
print(df)

sprzedawcy = df['Sprzedawca'].value_counts()
print(sprzedawcy)

wykres = sprzedawcy.plot(kind='bar', fontsize='6', color=['red', 'green', 'blue'])
wykres.set_title('Sprzedawcy i ilosc zamowien')
wykres.set_ylabel('Ilosc zamowien')
plt.legend(['Ilosc zamowien'])
plt.show()