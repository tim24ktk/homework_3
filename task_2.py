#     Напишите программу, которая найдёт произведение пар чисел списка.
#     Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
#     Пример:
#
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
import math

first_list = [2, 3, 4, 5, 6]
second_list = [2, 3, 5, 6]


def get_product(lst):
    results = []

    for i in range(math.ceil(len(lst) / 2)):
        result = lst[i] * lst[len(lst) - i - 1]
        results.append(result)

    return results


while True:
    value = int(input('Введите номер списка который хотите проверить (1 или 2): '))

    if value == 1 or value == 2:
        if value == 1:
            print(get_product(first_list))
            break
        else:
            print(get_product(second_list))
            break
    else:
        print(f'Списка с номером {value} нет! Попробуйте снова!')
