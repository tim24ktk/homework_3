# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def convert(n):
    lst = []

    while n > 0:
        ost = int(n % 2)
        n = (n - ost) / 2
        lst.append(str(ost))

    lst = list(reversed(lst))
    line = ''.join(lst)
    return line

n = int(input('Введите число десятичное число: '))
print(f'{n} -> {convert(n)}')
