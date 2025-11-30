import unittest
from src.funcion_math.fibo import fibo

class TestFibo(unittest.TestCase):
    def test_normal_res_1(self):
        res = fibo(5)
        self.assertEqual(res, 3)

    def test_normal_res_2(self):
        res = fibo(10)
        self.assertEqual(res, 34)

    def test_left_than_zero_num(self):
        self.assertRaises(Exception, fibo, -1)

    def test_string_arg(self):
        self.assertRaises(TypeError, fibo, "asd")

    def test_too_many_args(self):
        self.assertRaises(TypeError, fibo, 7, "a")

    def test_zero_(self):
        self.assertRaises(Exception, fibo, 0)
