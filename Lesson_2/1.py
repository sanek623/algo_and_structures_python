"""
1.	Написать программу, которая будет складывать, вычитать, умножать или делить
два числа. Числа и знак операции вводятся пользователем. После выполнения
вычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений. Завершение программы должно выполняться при вводе символа '0'
в качестве знака операции. Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.
Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
"""
import sys

while True:
    try:
        NUM_1 = int(input('Введите первое число: '))
        NUM_2 = int(input('Введите второе число: '))
        SIGN = input('Введите знак "+", "-", "*", "/": ')

        if SIGN == '+':
            print(NUM_1 + NUM_2)
        elif SIGN == '-':
            print(NUM_1 - NUM_2)
        elif SIGN == '*':
            print(NUM_1 * NUM_2)
        elif SIGN == '/':
            print(NUM_1 / NUM_2)
        elif SIGN == '0':
            print('Досвидания')
            sys.exit(1)
        else:
            print('Данные не корректны!')
    except ZeroDivisionError:
        print('На 0 делить нельзя!')
