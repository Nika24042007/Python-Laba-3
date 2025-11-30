from src.function_error.error_function_int import decorater_error_int_index
from src.function_error.error_function_list import decorate_error_list_only_int_index

@decorater_error_int_index(1)
@decorate_error_list_only_int_index(0)
def radix_sort(a:list[int], base: int = 10)->list[int]:
    """
    поразрядная сортировка списка а
    
    :param a: список, состоящий из целых неотрицательных чисел
    :param base: система счисления
    :return: отсортированный по возрастанию список
    """
    if all(i > 0 for i in a) != True:
        raise TypeError
    max_len = len(str(max(a)))+1
    for i in range(max_len):
        base_list = []
        base_list = [[] for _ in range(base)]
        for j in range(len(a)):
            if a[j]//base**i == 0:
                n = 0
            else:
                n = (a[j]//base**i)%base
            base_list[n].append(a[j])
        a = []
        a = [x for y in base_list for x in y]
    return a

