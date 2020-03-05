# 6.В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 30

max_num = 0
min_num = 0
N = 1
print('Генерируем список')
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
for i in range(10):
    if array[i] < array[min_num]:
        min_num = i
    elif array[i] > array[max_num]:
        max_num = i
print('min = %d, max = %d' % (array[min_num], array[max_num]))
if max_num > min_num:
    sum_num = array[min_num + 1:max_num]
else:
    sum_num = array[max_num + 1:min_num]
print(f'Между ними {sum_num}')
sum = 0
for x in sum_num:
    sum = sum + x
print(f'Их сумма = {sum}')
