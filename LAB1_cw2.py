import sys as system

system.stdout.write("Podaj a:")
a = int(system.stdin.readline())
system.stdout.write("Podaj b:")
b = int(system.stdin.readline())
system.stdout.write("Podaj c:")
c = int(system.stdin.readline())
wynik = pow(a, b) + c
wynik = str(wynik)
system.stdout.write(wynik)


