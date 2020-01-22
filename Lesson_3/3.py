"""3.	В массиве случайных целых чисел поменять местами минимальный
и максимальный элементы. """

import numpy as np

MASS = np.random.randint(0,10, 10)
MASS = MASS.tolist()
print(f'{MASS} - исходный массив')

i = MASS[0]
a = MASS[0]

for row in MASS:
    row = int(row)
    if row > i:
        i = row
    if a > row:
        a = row
in_i = MASS.index(i)
in_a = MASS.index(a)

MASS[in_i], MASS[in_a] = MASS[in_a], MASS[in_i]
print(f'{MASS} - откорректированный массив')
