liczba = int(input("Podaj liczbę: "))

czy_pierwsza = True

if liczba <= 1:
    czy_pierwsza = False
else:
    for i in range(2, int(liczba ** 0.5) + 1):
        if liczba % i == 0:
            czy_pierwsza = False
            break

if czy_pierwsza:
    print("Podana liczba jest liczbą pierwszą.")
else:
    print("Podana liczba nie jest liczbą pierwszą.")
