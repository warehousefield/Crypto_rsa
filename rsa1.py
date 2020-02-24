from random import randint, choice

# Решето Эратосфена. Поиск простых чисел
n = int(1500000)    # число, до которого хотим найти простые числа 
numbers = list(range(2, n + 1))
for number in numbers:
    if number != 0:
        for candidate in range(2 * number, n+1, number):
            numbers[candidate-2] = 0

# Выводим простые числа > 1000:
mylist = list(filter(lambda x: x > 1499000, numbers))

# Поиск p и q:
for j in range(1):
    p = choice(mylist)
    q = choice(mylist)
    



