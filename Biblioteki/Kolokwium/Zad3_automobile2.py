import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('automobile.csv', header=0, sep=';', decimal='.')
df = pd.DataFrame(data)
print(df)
grupa = df.groupby('Fuel-type').size()
print(grupa)
wykres = grupa.plot(kind='pie', autopct='%.2f%%', figsize=(7, 7), fontsize='14')
plt.legend()
plt.title('Rodzaj silnika procentowo')
plt.show()

