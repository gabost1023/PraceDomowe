import numpy as np

def generuj(podstawa, ilosc):
    potegi = np.logspace(1, ilosc, num=ilosc, base=podstawa)
    return potegi

podstawa = float(input("Podstawa potęgi: "))
ilosc = int(input("Ilość potęg do wygenerowania: "))
print(generuj(podstawa, ilosc))
