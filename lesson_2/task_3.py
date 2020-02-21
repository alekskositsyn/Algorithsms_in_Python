# 3.Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
#   Например, если введено число 3486, надо вывести 6843.
#   https://drive.google.com/file/d/1D5Reu7Ejm95nxWNXAItA0IlN09mVsqtL/view?usp=sharing

num1 = int(input("Введите целое число: "))
num2 = 0

while num1 > 0:
    num3 = num1 % 10
    num1 = num1 // 10
    num2 = num2 * 10
    num2 = num2 + num3

print(f'"Обратное" ему число: {num2}')


def recursion(num):
    num = str(num)
    b = ''
    for i in num:
        b = i + b
    print(b)


recursion(100)
