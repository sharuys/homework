# Task1
import random

hypotenuse = lambda x, y=1: (x**2 + y**2)**0.5
result1 = list(map(hypotenuse, [3, 4, 5]))
result2 = list(map(hypotenuse, [3, 4, 5], [4, 3, 5]))
print("Тест 1:", result1)
print("Тест 2:", result2)
# Task2
def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def generator(n, z):
    for num in range(n, z + 1):
        if prime(num):
            yield num

n = random.randint(1, 50)
z = random.randint(n + 1, 100)
numbers = list(generator(n, z))

print(f"Prime numbers in the range {n} to {z}: ", numbers)