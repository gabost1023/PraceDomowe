import numpy as np

def diagonalna(n):
    wektor = np.arange(n)[::-1]
    macierz = np.diag([a for a in wektor])
    return macierz


n = int(input("Podaj n: "))
print(diagonalna(n))