# 6.Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
#  https://drive.google.com/file/d/12fJPEO0ijZLsImTOq8CxS4EHqo-x5Ln5/view?usp=sharing
number = int(input('Введите номер буквы в алфавите: '))

FIRST_LETTER = 96  # Constant
char = chr(number + FIRST_LETTER)

print(char)