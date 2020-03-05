# 3.В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
max_num = 0
min_num = 0
N = 1
print('Генерируем список')
print(array)
for i in range(10):
    if array[i] < array[min_num]:
        min_num = i
    elif array[i] > array[max_num]:
        max_num = i
print('min b[%d]=%d, max b[%d]=%d' % (min_num, array[min_num], max_num, array[max_num]))
print('Меняем местами')
a = array[min_num]
array[min_num] = array[max_num]
array[max_num] = a
print(array)
