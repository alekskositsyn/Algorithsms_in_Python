import random, sys


def show(obj):
    # print(f'{obj=}, type={type(obj)}, size={sys.getsizeof(obj)}')
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


array = list_random(1000)
# print(array)
min_num = 0
max_num = 0
for i in range(len(array)):
    if array[i] < array[min_num]:
        min_num = i
    elif array[i] > array[max_num]:
        max_num = i
print('min = %d, max = %d' % (array[min_num], array[max_num]))
if max_num > min_num:
    sum_num = array[min_num + 1:max_num]
else:
    sum_num = array[max_num + 1:min_num]
# print(f'Между ними {sum_num}')
s = 0
for x in sum_num:
    s += x
print(f'Их сумма = {s}')

res = [show(array), show(min_num), show(max_num), show(i), show(s), show(x)]
print(f'Bytes sum = {sum(res)}')  # Bytes sum = 4578

# Python 3.8-32
# Windows 10-64
# Вывод: по моим результатам я понял,
# что большое знчение имеет в какой коллекции находяться необходимые нам данные для обработки,
# в моем ДЗ лучший вариант оказался №2 с использованием кортежа Bytes sum = 4090,
# средний вариант с использованием очереди Bytes sum = 4342 №1,
# самый худщий с списком №3 Bytes sum = 4578
