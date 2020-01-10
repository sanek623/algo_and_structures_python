"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.
"""

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


print(f'Цикл: ', numb_cycle(NUMB))
print(f'Рекурсия: ', numb_rec(NUMB, 0, LEN_NUMB))
