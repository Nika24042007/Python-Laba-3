from src.function_error.error_function_list import decorate_error_list_only_int_index

@decorate_error_list_only_int_index(0)
def counting_sort(a:list[int])->list[int]:
    """
    Сортировака списка а подсчетам
    :param a: список, состоящий из целых неотрицательных чисел
    :return: отсортированный по возрастанию список
    """
    if all(i > 0 for i in a) != True:
        raise TypeError
    count = [0]*(max(a)+1)
    b = []
    for i in a:
        count[i] += 1
    for i in range(len(count)):
        if count[i] > 0:
            b = b + [i]*count[i]
    return b
