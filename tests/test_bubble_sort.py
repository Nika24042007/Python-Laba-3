import unittest
from src.funcion_sort.bubble_sort import bubble_sort

class TestBubble(unittest.TestCase):
    def test_normal_res_num_int(self):
        a = [1,2,37,4,78,342,60,11,45,774]
        res = bubble_sort(a)
        self.assertEqual(res, sorted(a))

    def test_normal_res_num_float(self):
        a = [0.12,0.76,0.78,1.67,89.678,373.738,737.838]
        res = bubble_sort(a)
        self.assertEqual(res, sorted(a))

    def test_normal_res_num_str(self):
        a = ["asd","nfjf","dkdk","dkk","dmd","gnmv","gdhs"]
        res = bubble_sort(a)
        self.assertEqual(res, sorted(a))

    def test_normal_res_num_int_and_float(self):
        a = [1,3,4748.399,3883,838.98,948,838,67,87.98]
        res = bubble_sort(a)
        self.assertEqual(res, sorted(a))

    def test_num_and_str(self):
        a = [1,3,4748.399,3883,838.98,948,838,67,87.98, "sds", "sdsd"]
        self.assertRaises(TypeError, bubble_sort, a)

    def test_too_many_args(self):
        a = [1,3,4748.399,3883,838.98,948,838,67,87.98]
        self.assertRaises(TypeError, bubble_sort, a, 9)

    def test_minus_num_in_list(self):
        a = [1,-3,4748.399,-3883,-838.98,948,838,67,87.98]
        res = bubble_sort(a)
        self.assertEqual(res, sorted(a))

    def test_without_args(self):
        a = [1,3,4748.399,3883,838.98,948,838,67,87.98]
        self.assertRaises(IndexError, bubble_sort)
    
    def test_arg_not_list(self):
        self.assertRaises(TypeError, bubble_sort, "a")