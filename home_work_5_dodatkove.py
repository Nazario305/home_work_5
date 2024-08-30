
# створити матрицю 10 на 10, заповнити рандомними значеннями від 10 до 99

# - вивести суму чисел головної діагоналі матриці


import random

matrix = []

for i in range(10):
    row = []
    for j in range(10):
        row.append(random.randint(10, 99))
    matrix.append(row)
# print(matrix)

for row in matrix:
    print(row)

diagonal_sum = 0
for i in range(10):
    diagonal_sum += matrix[i][i]
    j = j - 1

print("Сума чисел головної діагоналі:", diagonal_sum)

# - вивести мінімальне та максимальне значення побічної діагоналі матриці

matrix_1 = []
for i in range(10):

        matrix_1.append(matrix[i][j])
        j = j - 1
    # matrix_1.append(row_1)
    # matrix_1 = [matrix[i][j]]
    # i = i - 1
# print(matrix_1)

print('Мінімальне значення побічної діагоналі матриці: ', min(matrix_1))
print('Максимальне значення побічної діагоналі матриці: ', max(matrix_1))
