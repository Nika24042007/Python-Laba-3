from src.funcion_math.factorial import factorial
from src.funcion_math.factorial_recursive import factorial_recursive
from src.funcion_math.fibo import fibo
from src.funcion_math.fibo_recursive import fibo_recursive
from src.funcion_sort.bubble_sort import bubble_sort
from src.funcion_sort.bucket_sort import bucket_sort
from src.funcion_sort.counting_sort import counting_sort
from src.funcion_sort.heap_sort import heap_sort
from src.funcion_sort.quick_sort import quick_sort
from src.funcion_sort.radix_sort import radix_sort
from src.queue import Queue



COMMANDS: dict = {"factorial":factorial, "factorial_recursive":factorial_recursive, 
                  "fibo":fibo, "fibo_recursive":fibo_recursive,"bubble_sort":bubble_sort, 
                  "bucket_sort":bucket_sort, "counting_sort":counting_sort, 
                  "heap_sort":heap_sort, "quick_sort":quick_sort, "radix_sort":radix_sort}

COMMANDS_QUEUE: dict = {"len":Queue.__len__, "front":Queue.front, "enqueue": Queue.enqueue, 
                        "is_empty": Queue.is_empty, "dequeue":Queue.dequeue, "creat": Queue}