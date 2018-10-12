import sys
def factorial_re(x):
    if x < 0:  return ("Not correct input")
    return 1 if x == 0 else x * factorial_re(x-1)
sys.setrecursionlimit(1000000)

x = int(input())
print(factorial_re(x))

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
      def test_true_5(self):
          self.assertEqual(factorial_re(-1), "Not correct input")
main()


