def factorial(x):
    if type(x) != int:
        raise TypeError("Некорректный ввод")
    if x < 0:
        raise Exception("Некорректный ввод")
    thing = 1
    for i in range(1, x + 1):
        thing *= i
    return thing

from unittest import (TestCase, main)
class Tester(TestCase):
      def test_true_1(self):
          self.assertEqual(factorial(5), 120)
      def test_true_2(self):
          self.assertEqual(factorial(0), 1)
      def test_true_3(self):
          self.assertEqual(factorial(1), 1)
      def test_true_4(self):
          self.assertEqual(factorial(20), 2432902008176640000)
      def test_exception(self):
          self.assertRaises(Exception, factorial, -1)
      def test_exception1(self):
          self.assertRaises(TypeError, factorial, "Hello")
      def test_exception2(self):
          self.assertRaises(TypeError, factorial, [])
      def test_exception3(self):
          self.assertRaises(TypeError, factorial, 1.3)
main()