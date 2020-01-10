"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).
"""


def even(numb):
    ''' Функция опеределения чётности числа '''
    if numb != 0 and numb % 2 > 0:
        #print('Число не чётное')
        return 0
    return 1
    #print("Число чётное")

try:
    NUMB = int(input("Введите число: "))
    LEN_NUMB = len(str(NUMB))
    print('Длинна числа: ', LEN_NUMB)
    if int(LEN_NUMB) > 1:
        A = 0
        B = 0
        for row in str(NUMB):
            if even(int(row)) > 0:
                A += 1
            else:
                B += 1
        print('Чётных - ', A)
        print('Не чётных - ', B)
    else:
        print(even(NUMB))
except:
    print('Данные не корректны!')
