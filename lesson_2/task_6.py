# 6.В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться,
# больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести правильный ответ.

import random

number = random.randint(1, 100)

count = 0
max_count = 10
winner = False
while not winner:
    count += 1
    if max_count < count:
        print(number)
        break
    print('Попытка №: ' + str(count))
    user_number = int(input('Введите число: '))
    if number == user_number:
        print('Победа!!!')
        winner = True
        break
    elif number > user_number:
        print('Вы не угадали, ваше число меньше загаданного')
    else:
        print('Вы не угадали, ваше число больше загаданного')


