from unittest import TestCase, main
import HW4.task3.trades_logic as logic

transactions, market_list = logic.initarr('test_trade.csv')
transactions2, market_list2 = logic.initarr('test2_trade.csv')
transactions3, market_list3 = logic.initarr('test3_trade.csv')


class Tester(TestCase):
    def test_longest_window(self):
        self.assertEqual(logic.longest_window(transactions),
                         (3, 2, 60808.5, '10:00:30.015000'))

    def test_longest_window2(self):
        self.assertEqual(logic.longest_window(transactions2),
                         (0, 0, 0, 0))

    def test_longest_window3(self):
        self.assertEqual(logic.longest_window(transactions3),
                         (0, 1, 13513.999999999998, '10:00:00.009000'))


main()
