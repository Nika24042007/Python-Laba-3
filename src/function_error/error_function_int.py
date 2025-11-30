from functools import wraps

def decorater_error_int_index(index):
    def decorater_error_int(func):
        @wraps(func)
        def error_function_int(*n, **k):
            if len(n) < index+1:
                return func(*n, **k)
            if n[index] == None:
                return func(*n, **k)
            if not isinstance(n[index], int):
                raise TypeError("Несоответствие типов переменной")
            if n[index] < 0:
                raise Exception('Число не может быть отрицательным')
            else:
                return func(*n, **k)
            
        return error_function_int
    return decorater_error_int
