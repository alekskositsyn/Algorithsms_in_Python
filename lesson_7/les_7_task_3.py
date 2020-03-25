# 3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы,
# в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).
import random

m = 4
random_list = [random.randint(1, 100) for i in range(2 * m + 1)]
print(random_list)


def heapify(nums, heap_size, root_index):
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2
    if left_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        # heap_size(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)
    for i in range(n, -1, -1):
        heapify(nums, n, i)
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)


heap_sort(random_list)
print(random_list)
median = random_list[int(len(random_list) / 2 + 0.5) - 1]
print(f'Медианой списка, является число - {median}')
