napis = input("Podaj napis: ").lower()
napis_bez_spacji = napis.replace(" ", "")
odwrocony = napis_bez_spacji[::-1]
czy_palindrom = True

for i in range(0, len(napis_bez_spacji)):
    if napis_bez_spacji[i] != odwrocony[i]:
        czy_palindrom = False
        break

if czy_palindrom:
    print("To jest palindrom")
else:
    print("To nie jest palindrom")

