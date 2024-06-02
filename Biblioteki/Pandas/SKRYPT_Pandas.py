import numpy as np
import pandas as pd

#####TWORZENIE SERIES I DATAFRAMES######

#SERIES#
s = pd.Series([1,2, np.nan,4])
print(s)
s = pd.Series([10,12,8,14], index=['a','b','c','d'])
print(s)

#DATAFRAME#
#Tworzenie dataframe na podstawie slownika
data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'], 'Populacja': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data)
print(df)

#DataFrame przechowuje typ dla każdej kolumny co możemy sprwadzić wpisując:
print(df.dtypes)

#możemy również w prosty sposób stworzyć serię danych - czyli próbki dla kolejnych #dat, pomiarów czasu
daty = pd.date_range('20210324', periods=5)
print(daty)
df = pd.DataFrame(np.random.randn(5, 4), index=daty, columns=list('ABCD'))
print(df)

#biblioteka Pandas umożliwia również tworzenie DataFrame'ów z zewnętrznych źródeł danych #CSV, odczyt i zapis
df = pd.read_csv('dane.csv', header=0, sep=';', decimal='.')
print(df)
df.to_csv('plik.csv', index=False)

#EXCEL – wymagana jest biblioteka openpyxl#
#trzeba ją zainstalować
xlsx = pd.ExcelFile('dane.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)
df.to_excel('wyniki.xlsx', sheet_name='arkusz pierwszy')


########## POBIERANIE DANYCH ZE STRUKTUR ###############

s = pd.Series([1,2,8,4], index=['a','b','c','d'])
print(s)

data = {'Kraj': ['Belgia', 'Indie','Brazylia'],
        'Stolica':['Bruksela', 'New Delhi', 'Brasilia'],
        'Populacja': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data)
print(df)

# pojedynczy element serii, odnosimy się do nazwy indeksu
print(s['c'])
# możemy również dostać się do wartości serii jak do pola klasy
print(s.c)

# pojedynczy elemenet ramki danych, tak jak przy cięciu tablic, oparte na indeksach
print(df[0:1])
print("")
#kolumna po etykiecie
print(df['Populacja'])
# pobieranie pojedynczej wartości po indeksie wiersza i kolumny
print(df.iloc[1,0])
# pobieranie wartości po indeksie wiersza i etykiecie kolumny
print(df.loc[0, 'Kraj'])

# podobnie jak w przypadku serii można odwoływać się do kolumn jak do pól klasy
# dodatkowo print jest wywoływany jak w pętli dla każdego elementu danej kolumny
print('kraj: ' + df.Kraj)

# Pandas posiada również funkcje pozwalające na losowe pobieranie elementów lub
# w odniesieniu do procentowej wielkości całego zbioru

#jeden losowy element
print(df.sample())
#dwa losowe elementy
print(df.sample(2))
#ilosc elementow procentowo, uwaga na zaokraglanie
print('\n',df.sample(frac=0.5))
# jeżeli potrzeba nam więcej próbek niż znajduje się w zbiorze i dopuszczamy duplikaty
# to możemy użyć parametru replace, który będzie losował z powtórzeniami
print(df.sample(n=10, replace=True))

# zamiast wyświetlać całą kolekcje możemy wyświetlić określoną ilość elementów od początku kolekcji
# lub od jej końca
print('\n',df.head(1))
print('\n',df.head(2))
print('\n',df.tail(1))

#Pandas jest też w stanie wyświetlić statystykę dla wartości, które dana kolekcja zawiera, o ile są jakieś kolumny
# z danymi numerycznymi
print(df.describe())
# transpozycja to zmienna T kolekcji, podobnie jak w Numpy
print(df.T)

####### LISTING GRUPOWANIE I AGREGOWANIE DANYCH #######
s = pd.Series([1,2,3,4,5], index=['a','b','c','d','e'])
print(s)

data = {'Kraj': ['Belgia', 'Indie', 'Brazylia'],
        'Stolica': ['Bruksela', 'New Delhi', 'Brasilia'], 'Populacja': [11190846, 1303171035, 207847528]}
df = pd.DataFrame(data)
print(df)

#wyświetla dane z serii gdzie wartość większa od 1
print(s[(s>1)])

# nieco inny efekt można osiągnąć wykorzystując funkcję where,
#która zwraca kolekcję w oryginalnej wielkości
# (liczebności) elementów, ale wartości nie spełniające warunku uzupełnia wartością NaN
print(s.where(s>10))

#możemy też podać wartość, która zostanie podstawiona zamiast NaN
print(s.where(s>10), 'za duze')
# jeszcze inna własność where pozwala na modyfikowanie oryginalnego zbioru (domyślnie zwaracana jest kopia)
seria = s.copy()
seria.where(seria>10, 'za duze', inplace=True)
print("########")
print(seria)

#wyświetla dane z serii gdzie wartość nie jest większa od 10
print(s[~(s > 10)])
#warunki możemy też łączyć
print(s[(s < 13) & (s > 8)])

#warunki dla pobierania DataFrame
print(df[df['Populacja']>120000000])
#bardziej skomplikowane warunki
print(df[(df.Populacja > 1000000) & (df.index.isin([0, 2]))])

#inny przykład z listą dopuszczalnych wartości oraz isin zwracająca wartości boolowskie
print('#########')
szukaj = ['Belgia', 'Brasilia']
print(df.isin(szukaj))

###### ZMIANA, USUWANIE I DODAWANIE DANYCH #########

#w przypadku serii możemy dodać/zmienić wartość poprzez odwołanie się do elementu serii przez klucz (indeks)
s['e'] = 15
print(s.e)
s['f'] = 16
print(s)

# podobna operacja dla DataFrame ma nieco inny efekt - wartość ustawiona dla wszystkich kolumn
df.loc[3] = 'dodane'
print(df)
# ale można dodać wiersz w postaci listy
df.loc[4] = ['Polska', 'Warszawa', 38675467]
print(df)

# usuwanie danych można wykonać przez funkcję drop, ale pamiętajmy, że operacja nie wykonuje się in-place więc
# zwracana jest kopia DataFrame z usuniętymi wartościami
new_df = df.drop([3]) 
print(new_df)
# więc jeżeli chcemy zmienić pierwotny zbiór dodajemy parametr inplace=True
df.drop([3], inplace=True) 
print(df)

# do DataFrame możemy dodawać również kolumny zamiast wierszy
df['Kontynent'] = ['Europa', 'Azja', 'Ameryka Południowa', 'Europa']
print(df)

# Pandas ma również własne funkcje sortowania danych
print(df.sort_values(by='Kraj'))

#Grupowania
grouped = df.groupby(['Kontynent'])
print(grouped.get_group('Europa'))
# można też jak w SQL czy Excelu uruchomić funkcje agregujące na danej kolumnie
print(df.groupby(['Kontynent']).agg({'Populacja':['sum']}))

# można usuwać również całe kolumny po nazwie indeksu
df.drop('Kraj', axis=1, inplace=True)
print(df)

