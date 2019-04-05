def pascal_triangle(line):
    if type(line) != int:
        raise TypeError("Некорректный ввод")
    if line <= 0:
        raise Exception("Некорректный ввод")
    if line == 1: return [[1]]
    initial_triangle = [[1], [1, 1]] 
    rows = [1, 1] 
    for i in range(2, line):
        rows = [1] + [sum(column) for column in zip(rows[1:], rows)] + [1]
        initial_triangle.append(rows)
    return initial_triangle

from unittest import (TestCase, main)

class Tester(TestCase):
    def test_true_1(self):
        self.assertEqual(pascal_triangle(1), [[1]])
    def test_true_2(self):
        self.assertEqual(pascal_triangle(3), [[1], [1, 1], [1, 2, 1]])
    def test_zero(self):
        self.assertRaises(Exception, pascal_triangle, 0)
    def test_exception(self):
        self.assertRaises(Exception, pascal_triangle, -1)
    def test_exception1(self):
        self.assertRaises(TypeError, pascal_triangle, "Hello")
    def test_exception2(self):
        self.assertRaises(TypeError, pascal_triangle, [])
    def test_exception3(self):
        self.assertRaises(TypeError, pascal_triangle, 1.3)
main()



