from src.function_error.error_function_int import decorater_error_int_index

@decorater_error_int_index(0)
def factorial(n: int) -> int:
    """
    Реализация вычисление факторияла числа n без реккурсии
    :param n: n целое, не отрицательное чилсло
    :return: факториал числа n
    """
    res = 1
    for i in range(n):
        res = res*(i+1)
    if n == 0:
        return 1
    else:
        return res
