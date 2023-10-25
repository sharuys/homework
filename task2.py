import random

n = int(input("Введіть розмір матриці: "))

matrix = [[random.randint(1, 100) for _ in range(n)] for _ in range(n)]

for row in matrix:
    print(row)

sum_dmat = sum(matrix[i][i] for i in range(n))
print("Сума чисел по діагоналі: ", sum_dmat)

lastsum = sum(matrix[i][-1] for i in range(n))
print("Сума останнього стовпця: ", lastsum)
