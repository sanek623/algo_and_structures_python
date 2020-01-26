"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""

from memory_profiler import profile
import numpy as np
import sys

NUMB = int(input("Введите число: "))
LEN_NUMB = len(str(NUMB))
print(sys.getrefcount(NUMB))
print(sys.getrefcount(LEN_NUMB))

@profile
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

@profile
def numb_rec(x, y, i):
    """Рекурсия"""
    if i == 0:
        return y
    if i > 0:
        digit = x % 10
        x = x // 10
        y = y * 10 + digit
        return numb_rec(x, y, i-1)


print(f'Цикл: ', numb_cycle(NUMB))
print(f'Рекурсия: ', numb_rec(NUMB, 0, LEN_NUMB))
print(sys.getrefcount(NUMB))
print(sys.getrefcount(LEN_NUMB))
del(NUMB)
del(LEN_NUMB)


"""python3.7, Windows 10/64,
Введите число: 123
6
260
Filename: D:/GeekBrains/Python/HomeWork/algo_and_structures_python/Lesson_6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
    20     21.8 MiB     21.8 MiB   @profile
    21                             def numb_cycle(x):
    22                                 '''Цикл'''
    23     21.8 MiB      0.0 MiB       len_x = len(str(x))
    24     21.8 MiB      0.0 MiB       res_x = ''
    25     21.8 MiB      0.0 MiB       x = str(x)
    26     21.8 MiB      0.0 MiB       i = len_x - 1
    27     21.8 MiB      0.0 MiB       while i >= 0:
    28     21.8 MiB      0.0 MiB           res_x = res_x + x[i]
    29     21.8 MiB      0.0 MiB           i -= 1
    30     21.8 MiB      0.0 MiB       return res_x


Цикл:  321
Filename: D:/GeekBrains/Python/HomeWork/algo_and_structures_python/Lesson_6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
    32     21.9 MiB     21.9 MiB   @profile
    33                             def numb_rec(x, y, i):
    34                                 '''Рекурсия'''
    35     21.9 MiB      0.0 MiB       if i == 0:
    36     21.9 MiB      0.0 MiB           return y
    37                                 if i > 0:
    38                                     digit = x % 10
    39                                     x = x // 10
    40                                     y = y * 10 + digit
    41                                     return numb_rec(x, y, i-1)


Filename: D:/GeekBrains/Python/HomeWork/algo_and_structures_python/Lesson_6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
    32     21.9 MiB     21.9 MiB   @profile
    33                             def numb_rec(x, y, i):
    34                                 '''Рекурсия'''
    35     21.9 MiB      0.0 MiB       if i == 0:
    36     21.9 MiB      0.0 MiB           return y
    37     21.9 MiB      0.0 MiB       if i > 0:
    38     21.9 MiB      0.0 MiB           digit = x % 10
    39     21.9 MiB      0.0 MiB           x = x // 10
    40     21.9 MiB      0.0 MiB           y = y * 10 + digit
    41     21.9 MiB      0.0 MiB           return numb_rec(x, y, i-1)


Filename: D:/GeekBrains/Python/HomeWork/algo_and_structures_python/Lesson_6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
    32     21.9 MiB     21.9 MiB   @profile
    33                             def numb_rec(x, y, i):
    34                                 '''Рекурсия'''
    35     21.9 MiB      0.0 MiB       if i == 0:
    36     21.9 MiB      0.0 MiB           return y
    37     21.9 MiB      0.0 MiB       if i > 0:
    38     21.9 MiB      0.0 MiB           digit = x % 10
    39     21.9 MiB      0.0 MiB           x = x // 10
    40     21.9 MiB      0.0 MiB           y = y * 10 + digit
    41     21.9 MiB      0.0 MiB           return numb_rec(x, y, i-1)


Filename: D:/GeekBrains/Python/HomeWork/algo_and_structures_python/Lesson_6/1.py

Line #    Mem usage    Increment   Line Contents
================================================
    32     21.9 MiB     21.9 MiB   @profile
    33                             def numb_rec(x, y, i):
    34                                 '''Рекурсия'''
    35     21.9 MiB      0.0 MiB       if i == 0:
    36     21.9 MiB      0.0 MiB           return y
    37     21.9 MiB      0.0 MiB       if i > 0:
    38     21.9 MiB      0.0 MiB           digit = x % 10
    39     21.9 MiB      0.0 MiB           x = x // 10
    40     21.9 MiB      0.0 MiB           y = y * 10 + digit
    41     21.9 MiB      0.0 MiB           return numb_rec(x, y, i-1)


Рекурсия:  321
6
260  
"""