"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

import collections
import functools

nums = collections.defaultdict(list)
for d in range(2):
    n = input(f'Введите {d+1}-е натуральное шестнадцатеричное число: ')
    nums[f'{d+1} {n}'] = list(n)
print(nums)

sum = sum([int(''.join(i), 16) for i in nums.values()])
print('Сумма: ', list('%X' % sum))

mult = functools.reduce(lambda a, b: a * b, [int(''.join(i), 16) for i in nums.values()])
print('Произведение: ', list('%X' % mult))