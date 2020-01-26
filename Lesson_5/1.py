"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

from collections import namedtuple

n = int(input("Введите кол-во пердприятий: "))
firms = namedtuple('Firm', 'name quarter_1 quarter_2 quarter_3 quarter_4')
profit = {}

for i in range(n):
    firm = firms(name=input("Введите название фирмы: "),
                 quarter_1=int(input("Введите прибыль за 1 квартал: ")),
                 quarter_2=int(input("Введите прибыль за 2 квартал: ")),
                 quarter_3=int(input("Введите прибыль за 3 квартал: ")),
                 quarter_4=int(input("Введите прибыль за 4 квартал: ")))
    profit[firm.name] = (firm.quarter_1 + firm.quarter_2 + firm.quarter_3 + firm.quarter_4) / 4


total = 0
for value in profit.values():
    total += value
total = total / n

for key, value in profit.items():
    if value > total:
        print(f'{key} - прибыль выше среднего!')
    elif value < total:
        print(f'{key} - прибыль ниже среднего!')
    elif value == total:
        print(f'{key} - средняя прибыль!')
