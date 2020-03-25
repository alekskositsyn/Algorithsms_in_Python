# 1.Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# https://drive.google.com/file/d/12fJPEO0ijZLsImTOq8CxS4EHqo-x5Ln5/view?usp=sharing

# Решение через дополнительные  пременные

num = int(input("Введите трехзначное число: "))
n1 = num // 100
n2 = num % 100 // 10
n3 = num % 10
s = n1 + n2 + n3
m = n1 * n2 * n3
print(s)
print(m)

# Решение через цикл для темы урока 2

num = str(num)
summa = 0
mult = 1
for i in num:
    summa += int(i)
    mult *= int(i)
print(f'Сумма = {summa}')
print(f'Произведение = {mult}')
