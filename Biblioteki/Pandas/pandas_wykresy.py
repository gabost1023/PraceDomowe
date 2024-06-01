import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ts = pd.Series(np.random.randn(1000))
# ts = ts.cumsum()
# print(ts)
# ts.plot()
# plt.show()

# data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
#         'Stolica': ['Bruksela','New Delhi', 'Brasilia'],
#         'Populacja': [1134234, 421243574, 56363375]}
# df=pd.DataFrame(data)
# df.loc[4] = ['Polska','Warszawa',38675467]
# df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']
# grupa = df.groupby(['Kontynent']).agg({'Populacja':['sum']})
# print(grupa)
# grupa.plot(kind='bar', xlabel = 'Kontynent', ylabel = 'Mld', rot=0, legend=True,title='Populacja z podzialem na kontynenty')
# #plt.xticks(rotation=0)
# plt.savefig('wykres.png')
# plt.show()

# df = pd.read_csv('dane.csv', header=0, sep=";", decimal=".")
# print(df)
# grupa = (df.groupby(["Imie i nazwisko"]).agg({"Wartosc zamowienia":["sum"]}))
# grupa.plot(kind='pie', subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6,6), colors=['red','green'])
# #wykres = grupa.plot.pie(subplots=True, autopct='%.2f %%', fontsize=20, figsize=(6,6))
# plt.legend(loc='lower right')
# plt.title('Suma zamowienia dla sprzedawcy')
# plt.show()

ts = pd.Series(np.random.randn(1000))
ts = ts.cumsum()
df = pd.DataFrame(ts, columns=['wartosci'])
print(df)
df['Srednia kroczaca'] = df.rolling(window=20).mean()
df.plot()
plt.legend()
plt.show()
