"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""

NUMB = int(input("Введите число итераций: "))


def count_recur(numb, i, sum):
    """Функция"""
    if numb == 1:
        sum = sum + 1
        return sum

    i = i / 2 * -1
    sum = sum + i
    print('i', i)
    print('sum', sum)
    return count_recur(numb-1, i, sum)


print(count_recur(NUMB, 1, 0))
