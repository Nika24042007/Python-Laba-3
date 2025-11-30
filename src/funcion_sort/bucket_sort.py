from src.function_error.error_function_list import decorate_error_list_only_float_index
from src.function_error.error_function_int import decorater_error_int_index

def quick_sort(a):
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

@decorater_error_int_index(1)
@decorate_error_list_only_float_index(0)
def bucket_sort(a: list[float], buckets: int = 10) -> list[float]:
    """
    Оспновная функция карманной сортировки
    :param a: список вещественных неотрицательных чисел
    :param buckets: количество ячеек в создаваемом списке
    :return: отсортированный по возрастанию список а
    """
    if all(i < 1 for i in a) != True:
        raise TypeError
    if all(i > 0 for i in a) != True:
        raise TypeError
    bucket = [[] for _ in range(buckets)]
    for num in a:
        b = int(buckets*num)
        bucket[b].append(num)

    for i in range(len(bucket)):
        if len(bucket[i]) > 1:
            bucket[i] = quick_sort(bucket[i])
    
    return [n for i in bucket for n in i]
            
