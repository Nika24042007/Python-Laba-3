from src.function_error.error_function_list import decorate_error_list_all_index

@decorate_error_list_all_index(0)
def quick_sort(a:list[int|float|str])->list[int|float|str]:
    """
    Быстрая сортировка списка а
    :param a: список, состоящий из чисел (целых, отрицательных, вещественных) или из строк
    :return: список, отсортированный по убыванию элементов
    """
    if len(a) <= 1:
        return a
    left = []
    right = []
    pivot = a[len(a)// 2]
    for i in range(len(a)):
        if a[i] < pivot:
            left.append(a[i])
        if a[i] >= pivot and i != len(a)//2:
            right.append(a[i])
    return quick_sort(left)+[pivot]+ quick_sort(right)


