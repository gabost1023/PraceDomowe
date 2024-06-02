import numpy as np
a = np.arange(2)
a1 = np.array([0, 1])
print(a)
print(a1)
print(type(a))
print(a.dtype)
a2 = np.arange(2, dtype='int64')
print(a2.dtype)
b = a.astype('float')
print(b)
print(b.dtype)
print(b.shape)

m = np.array([np.arange(2), np.arange(2)])
print(m)

zera = np.zeros((5, 5))
print(zera)
jedynki = np.ones((4, 4))
print(jedynki)
pusta = np.empty((2, 2))
print(pusta)
poz_1 = pusta[1,1]
poz_2 = pusta[0,1]
print(poz_1)
print(poz_2)

macierz = np.array([[1,2],[3,4]])
print(macierz)

ciag_liczb = np.arange(1,2,0.1)
print(ciag_liczb)

liczby_lin = np.linspace(1,2,5)
print(liczby_lin)

z = np.indices((5,3))
print(z)

x,y = np.mgrid[0:5, 0:5]
print(x)
print(y)

mat_diag = np.diag([a for a in range (5)])
print(mat_diag)

mat_diag_k = np.diag([a for a in range (5)], -2)
print(mat_diag_k)

it = np.fromiter(range(5), dtype='int32')
print(it)

marcin = 'Marcin'
mar_3 = np.array(list(marcin))
mar_4 = np.array(list(marcin), dtype='S1')
mar_5 = np.array(list(b'Marcin'))
mar_6 = np.fromiter(marcin, dtype='S1')
mar_7 = np.fromiter(marcin, dtype='U1')
print(mar_3)
print(mar_4)
print(mar_5)
print(mar_6)
print(mar_7)

mat = np.ones((2,2))
mat_1 = np.ones((2,2))
mat = mat + mat_1
print(mat)
print(mat - mat_1)
print(mat*mat_1)
print(mat/mat_1)

tab = np.arange(10)
print(tab)
s = slice(2,7,2)
print(a[s])

mat = np.arange(25)
mat = mat.reshape((5,5))
print(mat)

print(mat[1:]) #od drugiego wiersza
print(mat[:,1]) #druga kolumna jako wektor
print(mat[:,-1:]) #ostatnia kolumna
print(mat[2:6,1:3]) #2 i 3 kolumna dla 3,4,5 wierszy
print(mat[:, range(2,6,2)]) # 3 i 5 kolumna

#########

import numpy as np

a = np.array([20, 30, 40, 50]) #jak chcemy wykonywac dzialania to musza byc tej samej dlugosci
b = np.arange(4)
print(a)
print(b)

c = a - b
print(c)

print(b**2)

print(a)
a += b
print(a)
a -= b
print(a)


a = np.arange(3) #mniozenie macierzy - liczba wierszy z pierwszej musi sie zgadzac z liczba wierszy drugij
b = np.arange(3)
print(a)
print(b)
print(a.dot(b)) #dot mnozenie macierzy
print(np.dot(a,b))
c = np.array([[1,2,3],[4,5,6]])
d = np.array([[1,5], [2,6], [1,4]])
print(c)
print(d)
print(np.dot(c,d))

a = np.arange(12).reshape((3,4))
print(a)
print(a.sum())
print(a.sum(axis=0))
print(a.min(axis=1))

a = np.arange(6).reshape((3,2))
print(a)
for b in a:
    print(b) #element b to pojedynczy wiersz

for b in a:
    for i in range(len(b)):
        print(b[i],end=' ')
    print(" ")

print(a.shape)
print(type(a.shape))
for i in range(0, a.shape[0]):
    for j in range(0, a.shape[1]):
        print(a[i][j], end=' ')
    print(" ")

a = np.arange(6)
print(a)
print(a.shape)
print("")
b = a.reshape((2,3))
print(b)
print(b.shape)
print("")
c = b.reshape((3,2))
print(c)
print(c.shape)
print("")
d = c.ravel() #odtwarza wektor wejsciowy czyli splaszcza macierz do wektora
e = b.T #transpozycja czyli zamiana wierszy z kolumnami
print(e)