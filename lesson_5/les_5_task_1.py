# 1.Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.
from _collections import defaultdict

count_company = int(input('Введите количество предприятий: '))

d = defaultdict(lambda: int())
s = 0

for a in range(count_company):
    name_company = input('Введите название предприятия: ')
    year_profit = 0
    for n in range(4):
        profit = int(input(f'Введите прибыль {name_company} за {n + 1} квартал: '))
        year_profit += profit
    d[name_company] = year_profit
    s += year_profit / count_company
print(d)

a = [name for name in d if d[name] >= s]
print(f'Компании чья прибыль выше среднего: {",".join(a)}')

b = [name for name in d if d[name] < s]
print(f'Компании чья прибыль ниже среднего: {", ".join(b)}')
