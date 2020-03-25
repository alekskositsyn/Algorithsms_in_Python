# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.
import timeit
import cProfile
import random


def list_random(size):
    min_item = 1
    max_item = 150
    array = [random.randint(min_item, max_item) for _ in range(size)]
    return array


# вариант 1
def one_tour(n):
    array = list_random(n)
    min_first, min_second = (0, 1) if array[0] < array[1] else (1, 0)
    for i in range(2, len(array)):
        if array[i] < array[min_first]:
            spam = min_first
            min_first = i
            if array[spam] < array[min_second]:
                min_second = spam

        elif array[i] < array[min_second]:
            min_second = i

    return array[min_first], array[min_second]


# print(f'1 вариант - "{one_tour(20)}"')

# print(timeit.timeit('one_tour(100)', number=500, globals=globals()))  # 0.45277073699980974
# print(timeit.timeit('one_tour(200)', number=500, globals=globals()))  # 0.7815276589826681
# print(timeit.timeit('one_tour(300)', number=500, globals=globals()))  # 1.1545972480089404
# print(timeit.timeit('one_tour(400)', number=500, globals=globals()))  # 1.5645179420243949
# print(timeit.timeit('one_tour(500)', number=500, globals=globals()))  # 1.9585297610028647
# print(timeit.timeit('one_tour(600)', number=500, globals=globals()))  # 2.3522842110251077
# print(timeit.timeit('one_tour(700)', number=500, globals=globals()))  # 2.7605983199900948
# print(timeit.timeit('one_tour(800)', number=500, globals=globals()))  # 3.145127690047957
# print(timeit.timeit('one_tour(900)', number=500, globals=globals()))  # 3.5301640370162204
# print(timeit.timeit('one_tour(1000)', number=500, globals=globals())) # 3.9563733710092492

#
# cProfile.run('one_tour(10)')  # 1    0.000    0.000    0.000    0.000 les_4_task_1.py:23(one_tour)
# cProfile.run('one_tour(50)')  # 1    0.000    0.000    0.002    0.002 les_4_task_1.py:23(one_tour)
# cProfile.run('one_tour(100)')  # 1    0.000    0.000    0.004    0.004 les_4_task_1.py:23(one_tour)


# вариант 2
def min_max_func(n):
    array = list_random(n)
    min_1 = min(array)
    array.remove(min_1)
    min_2 = min(array)
    return min_1, min_2


# print(f'2 вариант {min_max_func(20)}')

# print(timeit.timeit('min_max_func(100)', number=500,globals=globals())) # 0.4286479629809037
# print(timeit.timeit('min_max_func(200)', number=500,globals=globals())) # 0.7138868719921447
# print(timeit.timeit('min_max_func(300)', number=500,globals=globals())) # 1.0443164500175044
# print(timeit.timeit('min_max_func(400)', number=500,globals=globals())) # 1.4170414010295644
# print(timeit.timeit('min_max_func(500)', number=500,globals=globals())) # 1.7709416400175542
# print(timeit.timeit('min_max_func(600)', number=500,globals=globals())) # 2.1398395220167004
# print(timeit.timeit('min_max_func(700)', number=500,globals=globals())) # 2.488940351991914
# print(timeit.timeit('min_max_func(800)', number=500,globals=globals())) # 2.8481213210034184
# print(timeit.timeit('min_max_func(900)', number=500,globals=globals())) # 3.1898570930352435
# print(timeit.timeit('min_max_func(1000)', number=500,globals=globals())) # 3.540099954989273


# cProfile.run('min_max_func(10)')   # 1    0.000    0.000    0.000    0.000 les_4_task_1.py:53(min_max_func)
# cProfile.run('min_max_func(50)')  # 1    0.000    0.000    0.002    0.002 les_4_task_1.py:53(min_max_func)
# cProfile.run('min_max_func(100)') # 1    0.000    0.000    0.003    0.003 les_4_task_1.py:53(min_max_func)

# 3 вариант

def search_in_sorted(n):
    array = list_random(n)
    for j in range(len(array)):
        for i in range(len(array) - j - 1):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
    return array[0], array[1]

# print(f'3 вариант {search_in_sorted(20)}')

# print(timeit.timeit('search_in_sorted(100)', number=500,globals=globals())) # 3.531196045980323
# print(timeit.timeit('search_in_sorted(200)', number=500,globals=globals())) # 9.073869519052096
# print(timeit.timeit('search_in_sorted(300)', number=500,globals=globals())) # 19.85747468000045
# print(timeit.timeit('search_in_sorted(400)', number=500,globals=globals())) # 36.15320599696133
# print(timeit.timeit('search_in_sorted(500)', number=500,globals=globals())) # 58.693356643023435

# cProfile.run('search_in_sorted(10)')   # 1    0.000    0.000    0.001    0.001 les_4_task_1.py:75(search_in_sorted)
# cProfile.run('search_in_sorted(50)')  # 1    0.001    0.001    0.004    0.004 les_4_task_1.py:75(search_in_sorted)
# cProfile.run('search_in_sorted(100)') # 1    0.011    0.011    0.015    0.015 les_4_task_1.py:75(search_in_sorted)

# 4 вариант

def func_sort(n):
    array = list_random(n)
    array.sort()
    return array[0], array[1]

#print(f'4 вариант {search_in_sorted(20)}')

# print(timeit.timeit('func_sort(100)', number=500,globals=globals())) # 0.45664652599953115
# print(timeit.timeit('func_sort(200)', number=500,globals=globals())) # 0.8039695030311123
# print(timeit.timeit('func_sort(300)', number=500,globals=globals())) # 1.1170258449856192
# print(timeit.timeit('func_sort(400)', number=500,globals=globals())) # 1.4805585510330275
# print(timeit.timeit('func_sort(500)', number=500,globals=globals())) # 1.8439383740187623
# print(timeit.timeit('func_sort(600)', number=500,globals=globals())) # 2.2107052439823747
# print(timeit.timeit('func_sort(700)', number=500,globals=globals())) # 2.5898384479805827
# print(timeit.timeit('func_sort(800)', number=500,globals=globals())) # 2.9546807580045424
# print(timeit.timeit('func_sort(900)', number=500,globals=globals())) # 3.326262731978204
# print(timeit.timeit('func_sort(1000)', number=500,globals=globals())) # 3.8029150280053727
#
#
#
# cProfile.run('func_sort(10)')   # 1    0.000    0.000    0.001    0.001 les_4_task_1.py:75(search_in_sorted)
# cProfile.run('func_sort(50)')  # 1    0.001    0.001    0.004    0.004 les_4_task_1.py:75(search_in_sorted)
# cProfile.run('func_sort(100)') # 1    0.011    0.011    0.015    0.015 les_4_task_1.py:75(search_in_sorted)


# Задача Функций найти два самых маленьких числа. Функция list_random генерирует список в котором будет поиск.
# Подставляя разные значения аргумента в функциях, изменял количество элементов в генерируемом списке.
# Первые два варианта работают практически одинаково, в отличии от третьего.
# В третьем варианте при использовании сортировки пузырьком, хоть мы и выводим прям из списка результат,
# но нам приходится очень много тратить времени на сортировку.
# После того как попробовал с помощью сортировки пузырьком решил ещё попробовать метод sort.
# как оказалось он работает не хуже первых двух вариантов.