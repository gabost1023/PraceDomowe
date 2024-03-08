liczba = int(input("Podaj liczbe: "))

if liczba < 0:
    print("Podales liczbe ujemna. Blad")
else:
    print("Pierwiastek z podanej liczby: ", pow(liczba, 1/2))