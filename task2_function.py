import random
def list2d(rows, cols):
    return [[random.randint(0, 200) for _ in range(cols)]
            for _ in range(rows)]
def symmetric_list(matrix):
    if not all(len(row) == len(matrix[0]) for
               row in matrix):
        print("Неможливо вивести")
        return

    max_widths = [max(len(str(matrix[i][j]))
                for j in range(len(matrix[0]))) for i in range(len(matrix))]

    for row in matrix:
        for j, value in enumerate(row):
            print(f"{value:>{max_widths[j]}}", end="")

rows = 3
cols = 3
table1 = list2d(rows, cols)
print(table1)
symmetric_list(table1)

table2 = list2d(4, 4)
print(table2)
symmetric_list(table2)

table3 = list2d(rows, cols)
print(table3)
symmetric_list(table3)


