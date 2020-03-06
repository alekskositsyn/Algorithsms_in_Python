# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random

SIZE = 50
MIN_ITEM = 1
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

for j in range(len(array)):
    for i in range(len(array)-j-1):
        if array[i] > array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]

# array.sort()
print(array)
print(f'1 минимальное число = {array[0]}')
print(f'2 минимальное число = {array[1]}')
