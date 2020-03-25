# 1) Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
#
# func("papa")
# 6
# func("sova")
# 9
import hashlib


def count_subs(string):
    if len(string) == 0 or len(string) == 1:
        return len(string)
    hash_set = set()
    step = 1
    while step < len(string):
        for i in range(len(string)):
            hash_tmp = hashlib.sha1(string[i:i + step].encode('utf-8')).hexdigest()
            hash_set.add(hash_tmp)
        step += 1
    return len(hash_set)


input_str = input('Введите строку: ')
count_subst = count_subs(input_str)
print(f'Число подстрок в строке: {count_subst}')
