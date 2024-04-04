#Zad1
# tekst = input("Podaj zdanie: ")
# print(tekst.split())
# print(len(tekst.split()))

#Zad2
# import sys as system
#
# a = int(system.stdin.readline())
# b = int(system.stdin.readline())
# c = int(system.stdin.readline())
#
# wynik = str(pow(a,b) +c)
# system.stdout.write(wynik)

#Zad3
# def czyPalindrom(tekst):
#
#     tekst = tekst.replace(" ", "")
#     pomocnicza = tekst[::-1]
#     if pomocnicza == tekst:
#         return True
#     else:
#         return False
#
# tekst = input("Podaj tekst: ")
# print(czyPalindrom(tekst))

#Zad4
# def czypierwsza(n):
#     if n < 2:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True
#
# a = int(input("Podaj liczbe: "))
# print(czypierwsza(a))

#Zad5
# def czydoskonala(n):
#     suma = 0
#     for i in range(1, n):
#         if n%i == 0:
#             suma = suma + i
#
#     if suma == n:
#         return True
#     else:
#         return False
#
#
# liczba = int(input("Podaj liczbe: "))
# print(czydoskonala(liczba))

#Zad6
# lista = [1, 2, 3, 4, 5, 6, 7.12, 8, 9.57]
# lista1 = [x**2 for x in lista]
#
# print(lista1)

#Zad7
# i = 1
# lista = []
# while i <= 10:
#     liczba = int(input("Podaj liczbe: "))
#     if liczba % 2 == 0:
#         lista.append(liczba)
#     i += 1
#
# print(lista)

#Zad8
lista = ["papuga", "papuga", "papuga", "brat", "brat", "smialek"]
slownik = {}

for i in lista:
    if i in slownik:
        slownik[i] += 1
    else:
        slownik[i] = 1

print(slownik)

for i in list(slownik.keys()):
    if not isinstance(i, (float, int)):
        slownik.pop(i)

print(slownik)




