import numpy as np

def generate_diagonal_matrix(n):
    matrix = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(n):
            if i == j:
                matrix[i, j] = 2
            elif abs(i - j) % 2 == 0:
                matrix[i, j] = 6
            else:
                matrix[i, j] = 4
    return matrix

n = 3
result_matrix = generate_diagonal_matrix(n)
print(result_matrix)
