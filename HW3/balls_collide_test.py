from unittest import TestCase, main
from HW3.balls_collide import balls_collide


class Tester(TestCase):
    def test_true_1(self):
        self.assertTrue(balls_collide((5.5, 2.4, 8.0), (5.0, 5.7, 2.0)))

    def test_true_2(self):
        self.assertTrue(balls_collide((0.0, 0.0, 0.0), (5.0, 5.7, 20.0)))

    def test_true_3(self):
        self.assertTrue(balls_collide((1.0, 1.0, 1.0), (1.0, 1.0, 1.0)))

    def test_true_4(self):
        self.assertTrue(balls_collide((2.0, 0.0, 1.0), (0.0, 0.0, 1.0)))

    def test_false_1(self):
        self.assertFalse(balls_collide((-8.5, -7.4, 2.0), (5.0, 5.7, 1.0)))

    def test_false_2(self):
        self.assertFalse(balls_collide((1.5, 1.5, 2.0), (7.0, 5.7, 2.0)))

    def test_exception1(self):
        self.assertRaises(Exception, balls_collide, ((-8.5, -7.4, -2.0), (5.0, 5.7, 2.0)))

    def test_exception2(self):
        self.assertRaises(Exception, balls_collide, ((-8.5, -7.4, 2.0), (5.0, 5.7, -2.0)))


main()
