# 9.Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
#  https://drive.google.com/file/d/12fJPEO0ijZLsImTOq8CxS4EHqo-x5Ln5/view?usp=sharing
print('Введите три целых числа: ')
a = int(input('1-e: '))
b = int(input('2-e: '))
c = int(input('3-e: '))

if b < a < c or c < a < b:
    print("Среднее:", a)
elif a < b < c or c < b < a:
    print("Среднее:", b)
else:
    print("Среднее:", c)
