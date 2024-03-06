doskonale = 0

for i in range(1, 1000):
    dzielniki = 0
    for j in range(1, i):
        if i % j == 0:
            dzielniki += j

    if dzielniki == i:
        doskonale += 1

print('Wsrod 1000 liczb doskonalych jest: ', doskonale)


