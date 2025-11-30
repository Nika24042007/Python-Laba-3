import unittest
from src.funcion_math.factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_normal_res_1(self):
        res = factorial(5)
        self.assertEqual(res, 120)

    def test_normal_res_2(self):
        res = factorial(6)
        self.assertEqual(res, 720)
        
    def test_left_than_zero_num(self):
        self.assertRaises(Exception, factorial, -1)

    def test_string_arg(self):
        self.assertRaises(TypeError, factorial, "asd")

    def test_too_many_args(self):
        self.assertRaises(TypeError, factorial, 7, "a")