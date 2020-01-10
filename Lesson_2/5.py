"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""


NUMBER = 32
while NUMBER < 128:
    print(f'{chr(NUMBER):3}{chr(NUMBER+1):3}{chr(NUMBER+2):3}{chr(NUMBER+3):3}{chr(NUMBER+4):3}'
          f'{chr(NUMBER+5):3}{chr(NUMBER+6):3}{chr(NUMBER+7):3}{chr(NUMBER+8):3}{chr(NUMBER+9):3}')
    NUMBER += 10
