"""
 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
"""

NUMB = int(input('Введите трёхзначное число: '))
if len(str(NUMB)) != 3:
    print('Введено не трёхзначное число, выходим.')
else:
    FIRST_NUM = NUMB // 100
    SECOND_NUM = (NUMB // 10) % 10
    THIRD_NUM = NUMB % 10

    print('Первая цифра: ' + str(FIRST_NUM) + ', вторая цифра: ' + str(SECOND_NUM) + ', третья цифра: ' + str(THIRD_NUM))
    print('Сумма всех цифр числа равна ', FIRST_NUM + SECOND_NUM + THIRD_NUM)
    print('Произведение всех цифр числа равно ', FIRST_NUM * SECOND_NUM * THIRD_NUM)
