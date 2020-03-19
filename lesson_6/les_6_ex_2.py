import random
import sys


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


array = tuple(list_random(1000))
# print(array)
min_num = min(array)
max_num = max(array)
idx_min = array.index(min_num)
idx_max = array.index(max_num)
print(f'Min number = {min_num}, MAX number = {max_num}')
if idx_min < idx_max:
    new_array = array[idx_min + 1:idx_max]
else:
    new_array = array[idx_max + 1:idx_min]
sum_num = sum(new_array)
print(f'Summa = {sum_num}')

res = [show(array), show(min_num), show(max_num), show(idx_min), show(idx_max), show(sum_num)]
print(f'Bytes sum = {sum(res)}')  # Bytes sum = 4090


