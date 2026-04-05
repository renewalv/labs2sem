class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def get_height(self) -> int:
        left_height = self.left.get_height() if self.left is not None else 0
        if left_height == -1:  
            return -1

        right_height = self.right.get_height() if self.right is not None else 0
        if right_height == -1:  
            return -1

        diff = left_height - right_height
        if diff > 1 or diff < -1:
            return -1

        if left_height > right_height:
            return left_height + 1
        else:
            return right_height + 1

    def is_balanced(self) -> bool:
        return self.get_height() != -1

    def insert(self, new_value):
        if new_value < self.value:
            if self.left is None:
                self.left = BinaryTree(new_value)
            else:
                self.left.insert(new_value)
        else:
            if self.right is None:
                self.right = BinaryTree(new_value)
            else:
                self.right.insert(new_value)