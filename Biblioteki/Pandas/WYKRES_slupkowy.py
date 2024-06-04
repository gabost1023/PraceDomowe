# Stwórz wykres słupkowy, który wyświetli liczbę urodzonych chłopców i dziewczynek z całego zbioru.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import danych z excela
xlsx = pd.ExcelFile('imiona.xlsx')
data = pd.read_excel(xlsx, header=0)
df = pd.DataFrame(data)
print(df)

grupa = df.groupby(['Plec'])['Liczba'].sum()
print(grupa)
wykres = grupa.plot(kind='bar', color=['pink','green'])
wykres.set_title('Liczba dzieci w podziale na plec')
wykres.set_ylabel('Liczba dzieci w podziale na plec')
wykres.ticklabel_format(axis='y', style='plain')
plt.show()