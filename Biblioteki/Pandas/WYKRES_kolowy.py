#Wykres kołowy z wartościami % ukazującymi ilość urodzonych chłopców i dziewczynek w ostatnich 5 latach z datasetu.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('imiona.xlsx')
data = pd.read_excel(xlsx, header=0)
df = pd.DataFrame(data)
print(df)

ostatnie_5_lat = dziewczynki = df[(df['Rok'] <= 2017) & (df['Rok'] >= 2012)]
print(ostatnie_5_lat)
grupa = ostatnie_5_lat.groupby(['Plec'])['Liczba'].sum()
print(grupa)

grupa.index = ['Dziewczynki', 'Chłopcy']
wykres = grupa.plot(kind='pie', subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6,6), colors=['red', 'green'])
plt.title('Liczba dziewczynek i chlopcow')
plt.legend(loc='lower right')
plt.show()