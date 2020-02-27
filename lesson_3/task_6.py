# 6.В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

max_num = 0
min_num = 0
N = 1
print('Генерируем список')
b = [random.randint(1, 20) for num in range(10)]
print(b)
for i in range(10):
    if b[i] < b[min_num]:
        min_num = i
    elif b[i] > b[max_num]:
        max_num = i
print('min = %d, max = %d' % (b[min_num], b[max_num]))
if max_num > min_num:
    sum_num = b[min_num + 1:max_num]
else:
    sum_num = b[max_num + 1:min_num]
print(f'Между ними {sum_num}')
sum = 0
for x in sum_num:
    sum = sum + x
print(f'Их сумма = {sum}')
