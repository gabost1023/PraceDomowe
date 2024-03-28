import math
import random

n = int(input("Podaj n: "))
wektor = [[random.randint(1, 10) for i in range(1, n+1)] for i in range(1, n+1)]

print(wektor)

sums = []

for row in wektor:
    row_sum = sum(row)
    sums.append(row_sum)

print("\n", sums)