import unittest
from src.funcion_math.factorial_recursive import factorial_recursive

class TestFactorialRecursive(unittest.TestCase):
    def test_normal_res_1(self):
        res = factorial_recursive(5)
        self.assertEqual(res, 120)

    def test_normal_res_2(self):
        res = factorial_recursive(6)
        self.assertEqual(res, 720)
        
    def test_left_than_zero_num(self):
        self.assertRaises(Exception, factorial_recursive, -1)

    def test_string_arg(self):
        self.assertRaises(TypeError, factorial_recursive, "asd")

    def test_too_many_args(self):
        self.assertRaises(TypeError, factorial_recursive, 7, "a")