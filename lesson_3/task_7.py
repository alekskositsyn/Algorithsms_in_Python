# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 15
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)
if array[0] > array[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0
for i in range(2, 10):
    if array[i] < array[min1]:
        n = min1
        min1 = i
        if array[n] < array[min2]:
            min2 = n
    elif array[i] < array[min2]:
        min2 = i
print(f'1 минимальное число = {array[min1]} с индексом {min1}')
print(f'2 минимальное число = {array[min2]} с индексом {min2}')
