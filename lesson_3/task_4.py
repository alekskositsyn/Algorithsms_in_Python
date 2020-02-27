# 4.Определить, какое число в массиве встречается чаще всего.
import random

print('Генерируем список')
list = [random.randint(1,20) for num in range(20)]
print(list)

num = list[0]
max_num = 1
for i in range(len(list) - 1):
    count = 1
    for k in range(i + 1, len(list)):
        if list[i] == list[k]:
            count += 1
    if count > max_num:
        max_num = count
        num = list[i]

if max_num > 1:
    print(max_num, 'раз(а) встречается число', num)
else:
    print('Все элементы уникальны')