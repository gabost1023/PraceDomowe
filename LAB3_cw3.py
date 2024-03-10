slownik = {"mąka": "kg", "batonik": "sztuki", "sok": "l", "krem": "sztuki"}
slownik2 = [produkt for produkt, jednostka in slownik.items() if jednostka == "sztuki"]

print(slownik2)
