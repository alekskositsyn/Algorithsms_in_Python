# 8.Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
#  Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
#  В конце следует вывести полученную матрицу.


matrix = [[int(input("Tape number:")) for num in range(4)] for num in range(4)]
for i in matrix:
    i.append(None)
print(*matrix, sep='\n')

for line in matrix:
    sum_line = 0
    for item in range(len(line) - 1):
        sum_line += line[item]
        print(f'{line[item]:>4}', end='')
    line[4] = sum_line
    print(f'\t{sum_line}')

