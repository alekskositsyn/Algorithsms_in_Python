# 4.Написать программу, которая генерирует в указанных пользователем границах:
#  ● случайное целое число,
#  ● случайное вещественное число,
#  ● случайный символ.
#  Для каждого из трех случаев пользователь задает свои границы диапазона.
#  Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
#  Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
#  https://drive.google.com/file/d/12fJPEO0ijZLsImTOq8CxS4EHqo-x5Ln5/view?usp=sharing
import random

print('Введите границы целых чисел')

num_start = int(input('от: '))
num_end = int(input('до: '))
# result = int(random.random() * (num_end - num_start + 1)) + num_start
result = random.randint(num_start, num_end)
print(result)

print('Введите границы вещественных чисел')
num_start = float(input('от: '))
num_end = float(input('до: '))
result = random.uniform(num_start, num_end)
print(round(result, 3))

print('Введите границы случайных символов')
num_start = ord(input('от символа: '))
num_end = ord(input('до символа: '))
result = random.randint(num_start, num_end)
print(chr(result))
