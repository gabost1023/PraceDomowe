import random

a = random.randint(10,20)
print(a)

random.seed(10)
print(random.random())

#kod generujacy 5 liczb losowych:

def generate_random_numbers(n):
    random_numbers = []
    for i in range(1, n):
        random_numbers.append(random.random())
    return random_numbers

random_numbers = generate_random_numbers(5)
print("Wygenerowane liczby losowe:", random_numbers)