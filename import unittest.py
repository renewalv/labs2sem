import unittest
from lab2courcse2 import get_max, parse_input, solve

class TestLab2(unittest.TestCase):
    def test_get_max(self):
        self.assertEqual(get_max(5, 3), 5)
        self.assertEqual(get_max(10, 100), 100)
        self.assertEqual(get_max(7, 7), 7)

    def test_parse_input(self):
        self.assertEqual(parse_input("10 2 3"), (10, 2, 3))
        self.assertEqual(parse_input("4 1 1"), (4, 1, 1))
        self.assertEqual(parse_input("  10   2    3  "), (10, 2, 3))

    def test_solve(self):
        self.assertEqual(solve(10, 2, 3), 9)
        self.assertEqual(solve(2, 1000000000, 999999999), 1999999998)
        self.assertEqual(solve(4, 1, 1), 2)

if __name__ == '__main__':
    unittest.main()