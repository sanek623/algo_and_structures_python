"""
9. Среди натуральных чисел, которые были введены, найти
наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.
"""

NUMB_1 = int(input("Введите 1 число: "))
NUMB_2 = int(input("Введите 2 число: "))

LEN_NUMB_1 = len(str(NUMB_1))
LEN_NUMB_2 = len(str(NUMB_2))

if int(LEN_NUMB_1) > 1 and NUMB_1 >= 0:
    i = 0
    for nu_1 in str(NUMB_1):
        i = i + int(nu_1)
    print(i)
else:
    i = NUMB_1
if int(LEN_NUMB_2) > 1 and NUMB_1 >= 0:
    a = 0
    for nu_2 in str(NUMB_2):
        a = a + int(nu_2)
    print(a)
else:
    a = NUMB_2

if i > a:
    print(f'{NUMB_1} > {NUMB_2}')
else:
    print(f'{NUMB_2} > {NUMB_1}')
