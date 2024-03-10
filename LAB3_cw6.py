def iloczyn_ciagu(a=1, b=4, ile=10):
    wynik = a
    for i in range(1, ile):
        wynik *= b
    return wynik

wynik_1 = iloczyn_ciagu()
print("Iloczyn ciągu:", wynik_1)

wynik_2 = iloczyn_ciagu(2, 3, 5)
print("Iloczyn ciągu:", wynik_2)
