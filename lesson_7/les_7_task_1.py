# 1). Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
import random


def list_random():
    size = 10
    min_item = -100
    max_item = 99
    array = [random.randint(min_item, max_item) for _ in range(size)]
    return array


def bubble_sort(arr):
    n = 1
    while n == 1:
        n = 0
        for i in range(len(arr) - 1):
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                n = 1
    return arr


bad_list = list_random()
print(f'Неотсортированный список: {bad_list}\nОтсортированный список: {bubble_sort(bad_list)}')
