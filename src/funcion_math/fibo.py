from src.function_error.error_function_int import decorater_error_int_index

@decorater_error_int_index(0)
def fibo(n: int) -> int:
    """
    Реализация вычисления n-ого элементе последовательности фибоначи без реккурсии
    :param n: n не отрицательное, не нулевое целое число
    :return: n-ый член последовательности фибоначи
    """
    list_fact = [0, 1]
    if n <= 0:
        raise Exception('Число не может быть ноль')
    for i in range(n):
        list_fact.append(list_fact[-1] + list_fact[-2])
    return list_fact[n-1]
