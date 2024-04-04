# Opercaje na plikach można podzielić na trzy etapy:
# 1. Otwarcie pliku
# 2. Działanie na pliku (odczyt lub zapis)
# 3. Zamknięcie pliku
#
# plik = open(nazwa, tryb, bufor)

# gdzie:
# plik – nazwa obiektu, którą sami nadajemy
# nazwa – nazwa pliku na dysku, jaka jest
# tryb – tryb otwarcia pliku (np. do odczytu, do zapisu itd.)
# bufor – obszar pamięci przechowujący dane w oczekiwaniu na zapis i odczyt

# Wybrane tryby otwarcia plików:
# r – tylko do odczytu. Plik musi istnieć: w – tylko do zapisu. Jeżeli pliku nie ma to zostanie utworzony a jeżeli jest to jego zawartość zostanie zastąpiona nową.
# a – do dopisywania. Dane dopisują się na końcu pliku. Jeśli plik nie istnieje to zostanie utworzony
# r+ - do odczytu i zapisu. Plik musi istnieć.
# w+ - do odczytu i zapisu. Jeśli plik nie istnieje zostanie utworzony.
# a+ - do odczytu i zapisu. Jeśli plik nie istnieje zostanie utworzony.

# Do odczytania danych z pliku można użyć komend:
# •
# • read(rozmiar) – odczytuje dane o rozmiarze, jeśli podany
# •
# • readline(rozmiar) – odczytuje wiersze lub ilości znaków jeśli podano rozmiar
# •
# • readlines() – odczytuje wiersze z pliku

# plik = open('tekst.txt', 'r', encoding='utf-8')
# #odczyt 10 znakow
# znaki = plik.read(10)
# wiersz = plik.readline()
# wiersze = plik.readlines()
# plik.close()
#
# print(znaki)
# print("\n")
# print(wiersz)
# print("\n")
# print(wiersze)
# print("\n")

# plik = open('tekst.txt', 'w+', encoding='utf-8')
# tekst = plik.readlines()
# a = 5
# plik.write(str(a))
# plik.seek(0)
# tekst2 = plik.readlines()
# plik.close()
# print(tekst)
# print("\n")
# print(tekst2)

# plik = open('tekst.txt', 'a', encoding='utf-8')
# plik.write("cos")
# plik.close()
#
# plik = open('tekst.txt', 'r', encoding='utf-8')
# tekst = plik.readlines()
# print(tekst)

