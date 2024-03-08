a = int(input("Podaj liczbe a: "))
b = int(input("Podaj liczbe b: "))
c = int(input("Podaj liczbe c: "))

if a > b:
    if a > c:
        print("Liczba {} jest największa.".format(a))
    else:
        print("Liczba {} jest największa.".format(c))
elif b > c:
    print("Liczba {} jest największa.".format(b))
else:
    print("Liczba {} jest największa.".format(c))
