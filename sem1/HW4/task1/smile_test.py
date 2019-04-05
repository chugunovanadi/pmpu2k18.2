from HW4.task1.smile_logic import smile
from unittest import TestCase, main


class Tester(TestCase):
    def test_true_1(self):
        self.assertTrue(smile('((()))'))

    def test_true_2(self):
        self.assertTrue(smile('{({})[][]}'))

    def test_true_3(self):
        self.assertTrue(smile('[ya] {fanat} (flake8)'))

    def test_true_4(self):
        self.assertTrue(smile(''))

    def test_false_1(self):
        self.assertFalse(smile('))))0000)))'))

    def test_false_2(self):
        self.assertFalse(smile('[[festival sveta otstoy}}'))

    def test_false_3(self):
        self.assertFalse(smile('{[}[](])'))


main()
