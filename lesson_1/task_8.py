# 8.Определить, является ли год, который ввел пользователь, високосным или не високосным.
#  https://drive.google.com/file/d/12fJPEO0ijZLsImTOq8CxS4EHqo-x5Ln5/view?usp=sharing
year = int(input('Введите год: '))

if year % 4 != 0:
    print('Год не високосный')
elif year % 100 == 0:
    if year % 400 == 0:
        print('Год високосный')
    else:
        print('Год не високосный')
else:
    print('Год високосный')