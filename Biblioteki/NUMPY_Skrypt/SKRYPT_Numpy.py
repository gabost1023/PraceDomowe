import numpy as np

#inicjalizacja tablicy
a = np.array([0, 1])
print(a)
#drugi sposob
a = np.arange(2)
print(a)

#wypisanie typu zmiennej tablicy (nie jej elementów) - ndarray
print(type(a))
#sprawdzenie typu danych tablicy
print(a.dtype)

#inicjalizacja tablicy z konkertnym typem danych
a = np.arange(2, dtype='float64')
print(a)

#zapisywanie kopii tablicy jako tablicy z innym typem
b = a.astype(int)
print(b)

#wypisanie rozmiaru tablicy
print(b.shape)

# można też sprawdzić ilość wymiarów tablicy
print(a.ndim)

#stworzenie tablicy wielowymiarowej może wyglądać tak
# #parametrem przekazywanym do funkcji array jest obiekt, który zostanie skonwertowany na tablicę
# #może to być Pythonowa lista
a = np.array([np.arange(2), np.arange(2)])
print(a)

#tworzenie macierzy wypelnionej zerami
zera = np.zeros((5,5))
print(zera)
#tworzenie macierzy wypelnionej jedynkami
jedynki = np.ones((3,3))
print(jedynki)
#tworzenie macierzy wypelnionej losowymi wartosciami
pusta = np.empty((4,4))
print(pusta)
#tworzenie macierzy diagonalnej
diag = np.diag([1,2,3])
print(diag)
diag = np.diag([a for a in range(5)])
print(diag)
#możemy podać drugi parametr funkcji diag, który określa indeks przekątnej względem głównej przekątnej
##która zostanie wypełniona wartościami podanego wektora
diag = np.diag([a for a in range(5)],-1)

#do elementow tablicy mozemy sie odwolac tak jak do elementow listy podajac indeksy
poz1 = pusta[1,1]
print(poz1)
poz2 = pusta[2,3]
print(poz2)

#tworzenie macierzy z uzupelnieniem
macierz = np.array([[1,2],[3,4]])
print(macierz)

#funkcja arange potrafi takze tworzyć ciągi liczb zmiennoprzecinkowych
ciag = np.arange(1,2,0.1)
print(ciag)
#w funkcji linspace dzielimu na num liczb
lin = np.linspace(1,2,5)
print(lin)

#a teraz możemy utworzyć dwie macierze, najpierw wartości interowane są w kolumnie a następnie w wierszu
z = np.indices((5,3))
print(z)

#wielowymiarowe macierze możemy również generować funkcją mgrid
x, y = np.mgrid[0:5, 0:5]
print(x)
print(y)

#Numpy jest wstanie stworzyć tablicę jednowymiarową z dowolnego obiektu iterowalnego (iterable)
z = np.fromiter(range(5), dtype='int32')
print(z)

#tablice znakow
marcin = 'Marcin'
mar_1 = np.array(list(marcin)) #['M' 'a' 'r' 'c' 'i' 'n']
print(mar_1)
mar_2 = np.array(list(marcin), dtype='S1') #[b'M' b'a' b'r' b'c' b'i' b'n']
print(mar_2)
mar_3 = np.array(list(b'Marcin')) #[ 77  97 114  99 105 110]
print(mar_3)
mar_4 = np.fromiter(marcin,dtype='S1') #[b'M' b'a' b'r' b'c' b'i' b'n']
print(mar_4)
mar_5 = np.fromiter(marcin,dtype='U1') #['M' 'a' 'r' 'c' 'i' 'n']
print(mar_5)

#talice w Numpy możemy w prosty sposób do siebie dodawać, odejmować, mnożyć, dzielić
mat = np.ones((2,2))
mat_1 = np.ones((2,2))
print(mat)
mats = mat/mat_1
print(mats)

#mozemy ciac tablice jak listy (metoda slice w pliku skrypt z zajec w folderze Numpy)
tablica = np.arange(10)
print(tablica) #[0 1 2 3 4 5 6 7 8 9]
print(tablica[2:7:2]) #[2 4 6] start:stop:step
print(tablica[2:]) #[2 3 4 5 6 7 8 9]
print(tablica[2:5])

#w podobny sposob postepujemy w przypadku tablic wielowymiarowych
tablica = np.arange(25)
print(tablica)
tablica = tablica.reshape((5,5))
print(tablica)
# [[ 0  1  2  3  4]
#  [ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]
#  [20 21 22 23 24]]
print(tablica[1:])
# [[ 5  6  7  8  9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]
#  [20 21 22 23 24]]
print(tablica[:,0]) #pierwsza kolumna jako wektor
#[ 0  5 10 15 20]
print(tablica[:,1:3])
# [[ 1  2]
#  [ 6  7]
#  [11 12]
#  [16 17]
#  [21 22]]
print(tablica[2:5, 1:3]) #3,4,5 wiersz dla 2 i 3 kolumny (gora sie nie liczy (3 i 5) sa to 4 kolumna i 6 wiersz
# [[11 12]
#  [16 17]
#  [21 22]]

#y będzie tablicą zawierającą wierzchołki macierzy x
x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print(x)
# [[ 0  1  2]
#  [ 3  4  5]
#  [ 6  7  8]
#  [ 9 10 11]]
rows = np.array([[0, 0], [3, 3]])
print(rows)
# [[0 0]
#  [3 3]]
cols = np.array([[0, 2], [0, 2]])
print(cols)
# [[0 2]
#  [0 2]]
y = x[rows,cols]
print(y)
# [[ 0  2]
#  [ 9 11]]