from math import sqrt

def perfect(n):
    if type(n) != int:
        raise TypeError("Некорректный ввод")
    if n <= 0:
        raise Exception("Некорректный ввод")
    if n == 1: return False
    ans = []
    for (i) in range(1, int(sqrt(n)) + 1):
            if (n) % i == 0:
             ans.append(i)
             ans.append(int(n / i))
    return sum(ans) == n+n

from unittest import (TestCase, main)
class Tester(TestCase):
    def test_true_1(self):
        self.assertTrue(perfect(6))
    def test_true_2(self):
        self.assertTrue(perfect(28))
    def test_true_3(self):
        self.assertTrue(perfect(496))
    def test_true_4(self):
        self.assertTrue(perfect(8128))
    def test_false_1(self):
        self.assertFalse(perfect(1))
    def test_false_2(self):
        self.assertFalse(perfect(89964))
    def test_zero(self):
        self.assertRaises(Exception, perfect, 0)
    def test_exception(self):
        self.assertRaises(Exception, perfect,-1)
    def test_exception1(self):
        self.assertRaises(TypeError, perfect,"Hello")
    def test_exception2(self):
        self.assertRaises(TypeError, perfect, [])
    def test_exception3(self):
        self.assertRaises(TypeError, perfect, 1.3)
main()
