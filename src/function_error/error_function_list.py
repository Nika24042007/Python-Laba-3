from functools import wraps

def decorate_error_list_all_index(index):
    def decorate_error_list_all(func):
        @wraps(func)
        def error_function_list_all(*a, **k):
            if isinstance(a[index], list):
                if all(isinstance(item, str) for item in a[index]):
                    return func(*a, **k)
                elif all(isinstance(item, int) or isinstance(item, float) for item in a[index]):
                    return func(*a, **k)
                else:
                    raise TypeError("Несоответствие типов переменных")
            else:
                raise TypeError("Несоответствие типов переменных")
        return error_function_list_all
    return decorate_error_list_all

def decorate_error_list_only_numbers_index(index):
    def decorate_error_list_only_numbers(func):
        @wraps(func)
        def error_function_list_only_numbers(*a, **k):
            if isinstance(a[index], list):
                if all(isinstance(item, int) or isinstance(item, float) for item in a[index]):
                    return func(*a, **k)
                else:
                    raise TypeError("Несоответствие типов переменных")
            else:
                raise TypeError("Несоответствие типов переменных")
        return error_function_list_only_numbers
    return decorate_error_list_only_numbers

def decorate_error_list_only_int_index(index):
    def decorate_error_list_only_int(func):
        @wraps(func)
        def error_function_list_only_int(*a, **k):
            if isinstance(a[index], list):
                if all(isinstance(item, int) for item in a[index]):
                    return func(*a, **k)
                else:
                    raise TypeError("Несоответствие типов переменных")
            else:
                raise TypeError("Несоответствие типов переменных")
        return error_function_list_only_int
    return decorate_error_list_only_int

def decorate_error_list_only_float_index(index):
    def decorate_error_list_only_float(func):
        @wraps(func)
        def error_function_list_only_float(*a,**k):
            if isinstance(a[index], list):
                if all(isinstance(item, float) for item in a[index]):
                    return func(*a, **k)
                else:
                    raise TypeError("Несоответствие типов переменных")
            else:
                raise TypeError("Несоответствие типов переменных")
        return error_function_list_only_float
    return decorate_error_list_only_float

