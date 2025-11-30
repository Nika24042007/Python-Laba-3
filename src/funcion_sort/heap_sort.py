from src.function_error.error_function_list import decorate_error_list_all_index

def heapify(a: list[int|str|float], n:int, i: int) -> None:
    m = i  
    l = 2*i + 1 
    r = 2*i + 2 
    if l < n and a[l] > a[m]:
        m = l
    if r < n and a[r] > a[m]:
        m = r
    if m != i:
        a[i],a[m] = a[m],a[i] 
        heapify(a, n, m)

@decorate_error_list_all_index(0)
def heap_sort(a:list[int|str|float])-> list[int|str|float]:
    """
    Сортировка кучей
    :param a: список чисел или строк, который нужно отсортировать
    :return: список отсортированный по возрастанию
    """
    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)
    for i in range(n - 1, 0, -1):
        a[i],a[0] = a[0],a[i]
        heapify(a, i, 0)
    return a

