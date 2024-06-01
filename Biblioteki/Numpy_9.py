import numpy as np

# Funkcja do generowania liczb Fibonacciego
def fibonacci(n):
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Liczba elementów, których potrzebujemy
n_elements = 5 * 5

# Generowanie liczb Fibonacciego
fib_sequence = fibonacci(n_elements)

# Tworzenie macierzy 5x5
macierz = np.zeros((5, 5), dtype='int64')

# Wypełnianie macierzy liczbami z ciągu Fibonacciego
index = 0
for i in range(5):
    for j in range(5):
        macierz[i, j] = fib_sequence[index]
        index += 1

print("Macierz wypełniona liczbami Fibonacciego:")
print(macierz)

