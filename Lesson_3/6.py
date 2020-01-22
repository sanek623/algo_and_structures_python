"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import numpy as np

MASS = np.random.randint(0, 100, 10)
MASS = MASS.tolist()
print(MASS)

max_i = MASS.index(max(MASS))
min_i = MASS.index(min(MASS))
arg = sorted((max_i, min_i))

print(f'max_i - {max_i}')
print(f'min_i - {min_i}')
print(f'Сумма {sum(MASS[arg[0]+1:arg[1]])}')
