import unittest
from lab3course2 import BinaryTree

class TestBalancedTree(unittest.TestCase):
    def test_balanced_example(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2, BinaryTree(4), BinaryTree(5))
        root.right = BinaryTree(3)
        self.assertTrue(root.is_balanced())

    def test_unbalanced_example(self):
        root = BinaryTree(1)
        root.left = BinaryTree(2)
        root.left.left = BinaryTree(3)
        self.assertFalse(root.is_balanced())

    def test_empty_tree(self):
        root = None
        is_balanced = root.is_balanced() if root is not None else True
        self.assertTrue(is_balanced)

    def test_single_node(self):
        self.assertTrue(BinaryTree(10).is_balanced())

if __name__ == "__main__":
    unittest.main()