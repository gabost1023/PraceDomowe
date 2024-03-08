lista = []

i = 0
while i < 10:
    i += 1
    liczba = int(input("Podaj liczbe: "))
    if liczba % 2 == 0:
        lista.append(liczba)


print(lista)