"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""

from random import random

B1 = int(input('Введите цифру нижней границы: '))
B2 = int(input('Введите цифру верхней границы: '))
S1 = ord(input('Введите первый символ: '))
S2 = ord(input('Введите второй символ: '))
UNIT = int(random() * (B2 - B1 + 1)) + B1
B1 = float(B1)
B2 = float(B2)
REAL = round(random() * (B2 - B1) + B1, 3)
SYMBOL = int(random() * (S2 - S1 + 1)) + S1
print(f'Случайное целое число: {UNIT}')
print(f'Случайное вещественное число: {REAL}')
print(f'Случайный символ: {chr(SYMBOL)}')
