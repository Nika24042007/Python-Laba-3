from src.function_error.error_function_int import decorater_error_int_index

@decorater_error_int_index(0)
def fibo_recursive(n:int) -> int:
    """
    Реализация вычисления n-ого элементе последовательности фибоначи с реккурсией
    :param n: n не отрицательное, не нулевое целое число
    :return: n-ый член последовательности фибоначи
    """
    if n <= 0:
        raise Exception('Число не может быть ноль')
    if n == 1:
        return 0
    if n == 2:
        return 1
    else:
        return fibo_recursive(n-1)+fibo_recursive(n-2)
    