import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('automobile.csv', header=0, sep=';', decimal='.')
df = pd.DataFrame(data)
print(df)
ramka1 = df[(df['Car model'] == 'audi') | (df['Car model'] == 'dodge')]
print(ramka1)
grupa = df.groupby('Car model')['Price'].sum()
print(grupa)

wykres = grupa.plot(kind='bar', figsize=(10,16))
plt.title('Ceny samochodow')
plt.xlabel('Car model')
plt.ylabel('Cena')
plt.show()
