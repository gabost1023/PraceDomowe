import numpy as np

def dziel_tablice (array, direction):
    if direction == 'poziomy':
        half_index = array.shape[0] // 2
        print(array.shape[0])
        array1 = array[:half_index, :]
        array2 = array[half_index:, :]
        print(array1)
        print(array2)

    elif direction == 'pionowy':
        half_index = array.shape[1] // 2
        print(array.shape[0])
        array1 = array[:, :half_index]
        array2 = array[:, half_index:]
        print(array1)
        print(array2)


tablica = np.array([[1,2],[3,4]])
dziel_tablice(tablica, 'pionowy')