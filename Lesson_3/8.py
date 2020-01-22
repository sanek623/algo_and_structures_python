"""
8.	Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки.
В конце следует вывести полученную матрицу.
"""

a, b = 0, 0
MASS2 = []
while a < 4:
    MASS = input("Введите массив из 4 цифр через пробел: ")
    MASS = MASS.split()
    MASS = [int(item) for item in MASS]
    sum_mass = sum(MASS)
    MASS.append(sum_mass)
    a += 1
    MASS2.append(MASS)

for i in MASS2:
    print(str(MASS2[b][:5]).strip('[]'))
    b += 1

