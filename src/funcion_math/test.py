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

print(radix_sort([1,2,37,4,78,342,60,11,45,774], 9))