import unittest
from laba4course2 import BinaryTreePriorityQueue

class TestPriorityQueue(unittest.TestCase):
    
    def setUp(self):
        self.pq = BinaryTreePriorityQueue()

    def test_empty_queue(self):
        result = self.pq.extract_max()
        self.assertIsNone(result)

    def test_single_element(self):
        self.pq.insert("Тест", 5)
        result = self.pq.extract_max()
        self.assertEqual(result, ("Тест", 5))

    def test_priority_order(self):
        self.pq.insert("Низький", 1)
        self.pq.insert("Високий", 10)
        self.pq.insert("Середній", 5)

        self.assertEqual(self.pq.extract_max(), ("Високий", 10))
        self.assertEqual(self.pq.extract_max(), ("Середній", 5))
        self.assertEqual(self.pq.extract_max(), ("Низький", 1))

    def test_same_priority(self):
        self.pq.insert("Перший", 10)
        self.pq.insert("Другий", 10)

        self.assertEqual(self.pq.extract_max()[1], 10)
        self.assertEqual(self.pq.extract_max()[1], 10)

if __name__ == "__main__":
    unittest.main()