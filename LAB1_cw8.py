lista = [1, "ela", 4.5, 4.5, "jablko", "ela"]
slownik = {}

for element in lista:
    if element in slownik:
        slownik[element] += 1
    else:
        slownik[element] = 1

print(slownik)

for klucz, wartosc in list(slownik.items()):
    if not isinstance(klucz, (float, int)):
        slownik.pop(klucz)

print(slownik)
