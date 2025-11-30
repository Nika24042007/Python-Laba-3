from src.function_error.error_function_int import decorater_error_int_index

@decorater_error_int_index(0)
def factorial_recursive(n: int) -> int:
    """
    Реализация вычисление факторияла числа n с реккурсией
    :param n: n целое, не отрицательное чилсло
    :return: факториал числа n
    """
    if n < 0:
        raise Exception('Число не может быть отрицательным')
    if n == 1 or n == 0:
        return 1
    else:
        return n*factorial_recursive(n-1)

