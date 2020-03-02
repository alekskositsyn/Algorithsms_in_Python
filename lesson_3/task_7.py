# В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.
import random

list = [random.randint(1, 20) for num in range(10)]
print(list)
if list[0] > list[1]:
    min1 = 0
    min2 = 1
else:
    min1 = 1
    min2 = 0
print(f'min1 -{min1} min2 -{min2}')
for i in range(2, 10):
    if list[i] < list[min1]:
        n = min1
        min1 = i
        if list[n] < list[min2]:
            min2 = n
    elif list[i] < list[min2]:
        min2 = i
print(f'1 минимальное число = {list[min1]} с индексом {min1}')
print(f'2 минимальное число = {list[min2]} с индексом {min2}')
