# 2.Посчитать четные и нечетные цифры введенного натурального числа.
#   Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
#   https://drive.google.com/file/d/1D5Reu7Ejm95nxWNXAItA0IlN09mVsqtL/view?usp=sharing

num = input('Введите число: ')
num = str(num)
even = 0
odd = 0
for n in num:
    n = int(n)
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
print(f'Четных: {even}, нечетных: {odd}')
