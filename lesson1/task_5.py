# 5.Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
#  https://drive.google.com/file/d/12fJPEO0ijZLsImTOq8CxS4EHqo-x5Ln5/view?usp=sharing
print('Введите две буквы')
letter_1 = input()
letter_2 = input()
FIRST_LETTER = 96  # Constant
num_l1 = int(ord(letter_1.lower())) - FIRST_LETTER
num_l2 = int(ord(letter_2.lower())) - FIRST_LETTER

if num_l1 > num_l2:
    num = num_l1 - num_l2 - 1
else:
    num = num_l2 - num_l1 - 1

print(num_l1)
print(num_l2)
print(num)
