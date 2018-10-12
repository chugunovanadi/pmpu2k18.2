def pascal_triangle(line):
    if line <= 0: return ("Tакой строки не существует",)
    if line == 1: return [[1]]
    initial_triangle = [[1], [1, 1]] 
    rows = [1, 1] 
    for i in range(2, line):
        rows = [1] + [sum(column) for column in zip(rows[1:], rows)] + [1]
        initial_triangle.append(rows)
    return initial_triangle

line = int(input())
for rows in pascal_triangle(line):
   print(rows)


from unittest import (TestCase, main)

class Tester(TestCase):
    def test_true_1(self):
        self.assertEqual(pascal_triangle(1), [[1]])
    def test_true_2(self):
        self.assertEqual(pascal_triangle(3), [[1], [1, 1], [1, 2, 1]])
main()



