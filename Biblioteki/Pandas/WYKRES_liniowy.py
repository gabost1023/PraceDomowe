#Stwórz wykres liniowy, który wyświetli liczbę urodzonych dzieci dla każdego roku.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import danych z excela
xlsx = pd.ExcelFile('imiona.xlsx')
data = pd.read_excel(xlsx, header=0)
df = pd.DataFrame(data)
print(df)


grupa = df.groupby('Rok')['Liczba'].sum()
wykres = grupa.plot()
wykres.set_ylabel('Liczba dzieci')
wykres.set_xlabel('Rok')
wykres.tick_params(axis='x', labelrotation=0)
years = grupa.index
wykres.set_xticks(years[::2])
wykres.set_xticklabels(years[::2])
wykres.legend()
wykres.set_title('Liczba dzieci w kolejnych latach')
plt.show()

