# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Дополнительно)
#
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def get_negofibonacci(n):
    fibonacci = [1, 1]
    negofibonacci = [1, -1]

    for i in range(2, n):
        fibonacci_num = fibonacci[i - 1] + fibonacci[i - 2]
        fibonacci.append(fibonacci_num)

        negofibonacci_num = negofibonacci[i - 2] - negofibonacci[i - 1]
        negofibonacci.append(negofibonacci_num)

    negofibonacci = list(reversed(negofibonacci))
    fibonacci.insert(0, 0)

    return negofibonacci + fibonacci


n = 8
print(get_negofibonacci(n))
