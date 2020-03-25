# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать
from _collections import deque
import random
import sys


def show(obj):
    #print(f'type={type(obj)}, size={sys.getsizeof(obj)}, {obj=}')
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                show(key)
                show(value)
        elif not isinstance(obj, str):
            for item in obj:
                show(item)
    return sys.getsizeof(obj)


def list_random(size):
    min_item = 1
    max_item = 100
    array = [random.randint(min_item, max_item) for _ in range(size)]
    return array


array = deque(list_random(1000))
# print(array)
idx_min = 0
idx_max = 0
for i in range(1, len(array)):
    if array[i] < array[idx_min]:
        idx_min = i
    elif array[i] > array[idx_max]:
        idx_max = i

if idx_min > idx_max:
    idx_min, idx_max = idx_max, idx_min

print(f'Левая граница: {array[idx_min]}\n'
      f'Правая граница: {array[idx_max]}')

summ = 0
for j in range(idx_min + 1, idx_max):
    summ += array[j]
print(f'Сумма = {summ}')

res = [show(array), show(idx_min), show(idx_max), show(i), show(summ), show(j)]
# show(array)
# show(idx_min)
# show(idx_max)
# show(i)
# show(summ)
# show(j)
print(f'Bytes sum = {sum(res)}')  # Bytes sum = 4342
