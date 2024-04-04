#Zad1
# A = {1-x: x∈<1,10>}
# A = [1-x for x in range(1, 11)]
# print(A)
# B = {1,4,16,…,4^7}
# B = [4**i for i in range(0, 8)]
# print(B)
#{x: x∈B i x jest liczbą podzielną przez 2}
# C = [x for x in B if x%2 == 0]
# print(C)

#Zad2
# import random
# random.seed()
# lista = [random.randint(1, 100) for i in range(1, 11)]
# print(lista)
# lista1 = [x for x in lista if x%2 == 0]
# print(lista1)

#Zad3
# slownik = {"maka": "kg", "bulki": "sztuki", "picie": "ml", "owoce": "sztuki", "gabki": "sztuki"}
# lista = [key for key, value in slownik.items() if value == "sztuki"]
# print(lista)
# odwrocone = {value: key for key, value in slownik.items()}
# print(odwrocone)

#Zad4
# def czyprostokatny(a,b,c):
#     if a == max(a,b,c):
#         if a**2 == b**2 + c**2:
#             return True
#         else:
#             return False
#     elif b == max(a,b,c):
#         if b**2 == a**2 + c**2:
#             return True
#         else:
#             return False
#     elif c == max(a,b,c):
#         if c**2 == b**2 + a**2:
#             return True
#         else:
#             return False
#
#
# a = int(input("Podaj a: "))
# b = int(input("Podaj b: "))
# c = int(input("Podaj c: "))
#
# print(czyprostokatny(a, b, c))

#Zad5
# def poleTrapezu(a=5, b=7, h=4):
#     pole = ((a+b)*h)/2
#     return pole
#
# print(poleTrapezu())

#Zad6
# def ciag(a=1, b=4, ile=10):
#    iloczyn = a
#    for i in range(a, ile):
#        iloczyn *=b
#        print(iloczyn)
#
# print(ciag())

#Zad7

# a = int(input("Podaj liczbe: "))
#
# if a < 0:
#     raise Exception("Nie mozesz podac liczby ujemnej")
#
# a = pow(a, 1/2)
# print(a)

