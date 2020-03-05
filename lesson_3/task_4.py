# 4.Определить, какое число в массиве встречается чаще всего.
import random

SIZE = 10
MIN_ITEM = 1
MAX_ITEM = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print('Генерируем список')
print(array)

num = array[0]
max_num = 1
for i in range(len(array) - 1):
    count = 1
    for k in range(i + 1, len(array)):
        if array[i] == array[k]:
            count += 1
    if count > max_num:
        max_num = count
        num = array[i]

if max_num > 1:
    print(max_num, 'раз(а) встречается число', num)
else:
    print('Все элементы уникальны')
