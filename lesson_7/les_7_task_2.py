# 2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.
import random


def list_random():
    size = 10
    min_item = 0.0
    max_item = 49.9
    array = [round(random.uniform(min_item, max_item), 2) for _ in range(size)]
    return array


def merge(left: list, right: list):
    spam = [0] * (len(left) + len(right))
    i = k = n = 0
    while i < len(left) and k < len(right):
        if left[i] < right[k]:
            spam[n] = left[i]
            i += 1
            n += 1
        else:
            spam[n] = right[k]
            k += 1
            n += 1
    while i < len(left):
        spam[n] = left[i]
        i += 1
        n += 1
    while k < len(right):
        spam[n] = right[k]
        k += 1
        n += 1
    return spam


def merge_sort(lst):
    if len(lst) <= 1:
        return
    middle = len(lst) // 2
    left = lst[:middle]
    right = lst[middle:]
    merge_sort(left)
    merge_sort(right)
    egg = merge(left, right)
    for i in range(len(lst)):
        lst[i] = egg[i]
    return lst


bad_list = list_random()
print(f'Неотсортированный список: {bad_list}\nОтсортированный список: {merge_sort(bad_list)}')
