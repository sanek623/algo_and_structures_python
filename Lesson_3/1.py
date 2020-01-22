""" 1.	В диапазоне натуральных чисел от 2 до 99 определить,
 сколько из них кратны каждому из чисел в диапазоне от 2 до 9. """

for number in range(2, 10):
    i = 0
    for number2 in range(2, 100):
        if number2 % number == 0:
            i += 1

    print(f'number - {number}')
    print(f'i - {i}')
