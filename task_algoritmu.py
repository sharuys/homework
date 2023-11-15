import random

def matrixsort(M):
    matrix = [[random.randint(1, 50) for _ in range(M)] for _ in range(M)]
    column_sums = [sum(column) for column in zip(*matrix)]

    n = len(column_sums)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if column_sums[j] > column_sums[j + 1]:
                column_sums[j], column_sums[j + 1] = column_sums[j + 1], column_sums[j]
                for k in range(M):
                    matrix[k][j], matrix[k][j + 1] = matrix[k][j + 1], matrix[k][j]

    for i in range(0, len(matrix), 2):
        matrix[i] = sorted(matrix[i])

    return matrix

def main(matrix):
    for row in matrix:
        print(' '.join(map(str, row)))

M = int(input("Введіть розмір матриці (M > 5): "))

if M <= 5:
    print("Розмір матриці повинен бути більше 5.")
else:
    sorted_matrix = matrixsort(M)

    print("\nВідсортована матриця:")
    main(sorted_matrix)
