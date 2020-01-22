"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

import timeit

NUMB = int(input("Введите число: "))
LEN_NUMB = len(str(NUMB))


def numb_cycle(x):
    """Цикл"""
    len_x = len(str(x))
    res_x = ''
    x = str(x)
    i = len_x - 1
    while i >= 0:
        res_x = res_x + x[i]
        i -= 1
    return res_x


def numb_rec(x, y, i):
    """Рекурсия"""
    if i == 0:
        return y
    if i > 0:
        digit = x % 10
        x = x // 10
        y = y * 10 + digit
        return numb_rec(x, y, i-1)


def memorize(func):
    def g(n, memory={}):
        r = memory.get(n)
        if r is None:
            r = func(n)
            memory[n] = r
        return r
    return g


""" Думаю тут что-то не верно сделал """
def memorize2(func):
    def g(x, y, i, memory={}):
        r = memory.get(x)
        if r is None:
            r = func(x, y, i)
            memory[x, y, i] = r
        return r
    return g


@memorize
def f(n):
    """Рекурсия"""
    if n < 2:
        return n
    return f(n-1) + f(n-2)


@memorize2
def numb_rec2(x, y, i):
    """Рекурсия"""
    if i == 0:
        return y
    if i > 0:
        digit = x % 10
        x = x // 10
        y = y * 10 + digit
        return numb_rec2(x, y, i-1)


print(f'Цикл: {timeit.timeit(numb_cycle(NUMB))}')
print(f'Рекурсия: {timeit.timeit("numb_rec(NUMB, 0, LEN_NUMB)", "from __main__ import numb_rec, NUMB, LEN_NUMB")}')
print(f'Рекурсия из урока: {timeit.timeit("f(NUMB)", "from __main__ import f, NUMB")}')
print(f'Рекурсия с memorize: {timeit.timeit("numb_rec2(NUMB, 0, LEN_NUMB)", "from __main__ import numb_rec2, NUMB, LEN_NUMB")}')
