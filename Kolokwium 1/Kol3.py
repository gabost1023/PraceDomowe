def draw_pyramid(height):
    if height > 10:
        print("Wysokość piramidy nie może być większa niż 10.")
    else:
        for i in range(1, height + 1):
            print(" " * (height - i) + "A" * (2 * i - 1))

1
height = int(input("Podaj wysokość piramidy (maksymalnie 10): "))
draw_pyramid(height)
