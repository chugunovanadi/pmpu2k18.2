import sys
def factorial_re(x):
    if type(x) != int:
        raise TypeError("Некорректный ввод")
    if x < 0:
        raise Exception("Некорректный ввод")
    return 1 if x == 0 else x * factorial_re(x-1)
sys.setrecursionlimit(1000000)

from unittest import (TestCase, main)
class Tester(TestCase):
      def test_true_1(self):
          self.assertEqual(factorial_re(5), 120)
      def test_true_2(self):
          self.assertEqual(factorial_re(0), 1)
      def test_true_3(self):
          self.assertEqual(factorial_re(1), 1)
      def test_true_4(self):
          self.assertEqual(factorial_re(20), 2432902008176640000)
      def test_exception(self):
          self.assertRaises(Exception, factorial_re, -1)
      def test_exception1(self):
          self.assertRaises(TypeError, factorial_re, "Hello")
      def test_exception2(self):
          self.assertRaises(TypeError, factorial_re, [])
      def test_exception3(self):
          self.assertRaises(TypeError, factorial_re, 1.3)
main()


