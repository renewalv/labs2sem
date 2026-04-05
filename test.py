import unittest
from lab1course2 import find_unsorted_subarray

class TestFindUnsortedSubarray(unittest.TestCase):
    
    def test_example_case(self):
        arr = [1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19]
        self.assertEqual(find_unsorted_subarray(arr), (3, 9))

    def test_already_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(find_unsorted_subarray(arr), (-1, -1))

    def test_completely_unsorted_array(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(find_unsorted_subarray(arr), (0, 4))

    def test_single_element_array(self):
        arr = [42]
        self.assertEqual(find_unsorted_subarray(arr), (-1, -1))


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)