from src.function_error.error_function_list import decorate_error_list_all_index

@decorate_error_list_all_index(0)
def bubble_sort(a:list[int|float|str])->list[int|float|str]:
    """
    Сортировка списка пузырьком
    :param a: список, состоящий из чисел (целых, отрицательных, вещественных) или из строк
    :return: список, отсортированный по убыванию элементов
    """
    for i in range(len(a)-1):
        for j in range(len(a)-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a
