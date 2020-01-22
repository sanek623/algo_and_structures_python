""" 4.	Определить, какое число в массиве встречается чаще всего. """

import numpy as np

MASS = np.random.randint(0, 10, 10)
MASS.sort()
print(MASS)

a = 1
p = 0
s = 0
b = 0

for row in MASS:
    b += 1
    if b == 1:
        i = row
    else:
        if row == i:
            a += 1
            if  a > s:
                p = row
                s = a
        else:
            a = 1
        i = row

print(f'Цифра {p} встречается в массиве {s} раза')

'''Раз и раза не стал делать в данном примере. '''
