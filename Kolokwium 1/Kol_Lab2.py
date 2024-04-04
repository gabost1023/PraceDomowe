import math
#Zad1

# lista = ["pilka nozna", "jazda konna", "koszykowka", "szachy", "siatkowka"]
# print(lista)
#
# lista.reverse()
# print(lista)
#
# lista.extend(["plywanie", "boks"])
# print(lista)

#Zad2

# slownik = {
#     "Wiedźmin 3: Dziki Gon": 2015,
#     "Grand Theft Auto V": 2013,
#     "The Elder Scrolls V: Skyrim": 2011,
#     "Minecraft": 2011,
#     "The Witcher 2: Zabójcy Królów": 2011,
#     "Dark Souls III": 2016,
#     "Red Dead Redemption 2": 2018,
#     "Counter-Strike: Global Offensive": 2012,
#     "League of Legends": 2009,
#     "Overwatch": 2016
# }
#
# print(len(slownik))
# print(len(slownik.keys()))
# print(len(slownik.values()))
#
# del slownik["Red Dead Redemption 2"]
#
# print(slownik)
# print(len(slownik))

#Zad4

# tekst = input("Enter text: ")
#
# print(tekst.count('a'))

#Zad6

# a = int(input("Enter a: "))
# b = int(input("Enter b: "))
# c = int(input("Enter c: "))
#
# if a > b and a > c:
#     print("{:d} jest najwieksza liczba".format(a))
# elif b > a and b > c:
#     print("{:d} jest najwieksza liczba".format(b))
# elif c > a and c > b:
#     print("{:d} jest najwieksza liczba".format(c))
# elif a == b == c:
#     print("{:d} jest najwieksza liczba".format(a))
# elif a == b and a > c:
#     print("{:d} jest najwieksza liczba".format(a))
# elif b == c and b > a:
#     print("{:d} jest najwieksza liczba".format(b))

#Zad7

# list1=[1,2,3.26,4,5.45,6,7,8.69]
#
# lista = [x**2 for x in list1]
# print(lista)

#Zad8
# lista = []
# i = 0
# while i < 10:
#     liczba = int(input("Podaj liczbe: "))
#     if liczba % 2 == 0:
#         lista.append(liczba)
#     i += 1
#
# print(lista)

#Zad9

liczba = int(input("Podaj liczbe: "))

if liczba < 0:
    print("Podales liczbe ujemna")
else:
    print("Pierwiastek z twojej liczby to: ", math.sqrt(liczba))