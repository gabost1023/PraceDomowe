def draw_tower(height):
    if height > 10:
        print("Wysokość wieży nie może być większa niż 10.")
    else:
        for i in range(1, height + 1):
            print("A" * i)


height = int(input("Podaj wysokość wieży (maksymalnie 10): "))
draw_tower(height)
