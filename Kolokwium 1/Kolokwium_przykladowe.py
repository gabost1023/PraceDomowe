#Zad 5 WEKTOR
# import random
# random.seed()
# def fwektor(n):
#     wektor = [[random.randint(1, 100) for i in range(1, n+1)] for j in range(1, n+1)]
#     return wektor
#
# print(fwektor(3))

#Zad 3 PIRAMIDA
n = int(input("Podaj wysokosc wiezy: "))

for i in range(1, n+1):
    print((" "*(n-i))+("A"*(i-1))+("A"*i))
