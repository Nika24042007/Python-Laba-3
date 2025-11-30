import unittest
from src.parser import parser

class TestParser(unittest.TestCase):
    def test_command_with_func_list_with_int_str_float_num(self):
        res = parser('func_sort [1,2,3,"ghjk",0.567,9.98,   123,  "hjk"] 20')
        self.assertEqual(res, ['func_sort', [1, 2, 3, 'ghjk', 0.567, 9.98, 123, 'hjk'], 20])
    
    def test_command_with_func_list_with_int_str_float_string(self):
        res = parser('func_sort [1,2,3,"ghjk",0.567,9.98,   123,  "hjk"] "hbj"')
        self.assertEqual(res, ['func_sort', [1, 2, 3, 'ghjk', 0.567, 9.98, 123, 'hjk'], 'hbj'])

    def test_command_with_func_list_with_int_str_float(self):
        res = parser('func_sort [1,2,3,"ghjk",0.567,9.98,   123,  "hjk"]')
        self.assertEqual(res, ['func_sort', [1, 2, 3, 'ghjk', 0.567, 9.98, 123, 'hjk']])

    def test_command_with_func_string(self):
        res = parser('func_sort "hbj"')
        self.assertEqual(res, ['func_sort', 'hbj'])

    def test_command_with_func_num_int(self):
        res = parser('func_sort 34')
        self.assertEqual(res, ['func_sort', 34])

    def test_command_with_func_num_float(self):
        res = parser('func_sort 20.85')
        self.assertEqual(res, ['func_sort', 20.85])

    def test_command_with_omly_func(self):
        res = parser('func_sort')
        self.assertEqual(res, ['func_sort'])