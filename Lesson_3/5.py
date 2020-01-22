""" 5.	В массиве найти максимальный отрицательный элемент.
Вывести на экран его значение и позицию (индекс) в массиве. """

import numpy as np

MASS_BASE = np.random.randint(-100, 100, 10)
MASS = []

print(MASS_BASE)

for i in MASS_BASE:
    if i < 0:
        MASS.append(i)

print(MASS)
print(f'Максимальный отрицательный элемент в массиве {max(MASS)}'
      f' его индекс {MASS.index(max(MASS))}')