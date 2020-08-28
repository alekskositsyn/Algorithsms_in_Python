# 9.Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)] for _ in range(SIZE)]
print(*matrix, sep='\n')
min_in_column = [MAX_ITEM] * len(matrix[0])

for line in matrix:
    sum_line = 0
    for i, item in enumerate(line):
        if min_in_column[i] > item:
            min_in_column[i] = item
for p, m in enumerate(min_in_column):
    print(f'{m:>4} минимальный эллемент в {p + 1} столбце')
max_item = 0
for i in min_in_column:
    if max_item < i:
        max_item = i
print(f'\n Максимальный элемент среди минимальных = {max_item}')
