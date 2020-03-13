# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».
import timeit
import cProfile


def sieve(a):
    n = a * 20
    sieve = [i for i in range(n)]
    sieve[1] = 0
    for i in range(2, n):
        if sieve[i] != 0:
            j = i + i
            while j < n:
                sieve[j] = 0
                j += i
    res = [i for i in sieve if i != 0]
    return res[a - 1]

# print(sieve(15))

# print(timeit.timeit('sieve(10)', number=500,globals=globals())) # 0.14552843698766083
# print(timeit.timeit('sieve(100)', number=500,globals=globals())) # 1.7685901169897988
# print(timeit.timeit('sieve(1000)', number=500,globals=globals())) # 20.448801379010547
# print(timeit.timeit('sieve(10000)', number=500,globals=globals())) # 228.00093832495622

# cProfile.run('sieve(100)')   # 1    1    0.003    0.003    0.004    0.004 les_4_task_2.py:14(sieve)
# cProfile.run('sieve(200)')  #  1    0.009    0.009    0.012    0.012 les_4_task_2.py:14(sieve)
# cProfile.run('sieve(300)') # 1    0.015    0.015    0.019    0.019 les_4_task_2.py:14(sieve)

def prime(a):
    num_pos = 0
    n = 2
    res = []
    while num_pos != a:
        d = 2
        while n % d != 0:
            d += 1
        if d == n:
            num_pos += 1
            res.append(d)
        n += 1
    return res[-1]

# print(prime(15))


print(timeit.timeit('prime(10)', number=500,globals=globals())) # 0.04406219901284203
print(timeit.timeit('prime(100)', number=500,globals=globals())) # 5.182473672030028
print(timeit.timeit('prime(1000)', number=500,globals=globals())) # 920.922182912007
print(timeit.timeit('prime(10000)', number=500,globals=globals())) # очень долго

#
# cProfile.run('prime(100)')   # 1    0.011    0.011    0.011    0.011 les_4_task_2.py:39(prime)
# cProfile.run('prime(200)')  # 1    0.069    0.069    0.070    0.070 les_4_task_2.py:39(prime)
# cProfile.run('prime(300)') # 1    0.165    0.165    0.167    0.167 les_4_task_2.py:39(prime)

# Решето(при построеннии графика выглядит как O(n))  работает явно быстрее prime(O(n**2)).