# 5.Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно.
#   Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
#   https://drive.google.com/file/d/1D5Reu7Ejm95nxWNXAItA0IlN09mVsqtL/view?usp=sharing


def rec(m, n):
    if m < n:
        for i in range(m, m + 10):
            if i <= n:
                print(f'{i} - {chr(i)}  ', end=' ')
        print('')
        return rec(m + 10, n)


rec(32, 127)
