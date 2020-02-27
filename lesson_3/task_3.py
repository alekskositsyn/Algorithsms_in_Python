# 3.В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

max_num= 0
min_num = 0
N = 1
print('Генерируем список')
b = [random.randint(1,20) for num in range(10)]
print(b)
for i in range(10):
    if b[i] < b[min_num]:
        min_num = i
    elif b[i] > b[max_num]:
        max_num = i
print('min b[%d]=%d, max b[%d]=%d' % (min_num, b[min_num], max_num, b[max_num]))
print('Меняем местами')
a = b[min_num]
b[min_num] = b[max_num]
b[max_num] = a
print(b)