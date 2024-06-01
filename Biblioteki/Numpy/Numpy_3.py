import numpy as np


def funkcja(n):
    tablica = np.arange(1,n*n+1).reshape((n,n))
    return tablica


n = int(input("Podaj n:"))
print(funkcja(n))
