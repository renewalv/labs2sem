class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.left = None
        self.right = None


class BinaryTreePriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        new_node = Node(value, priority)
        if self.root is None:
            self.root = new_node
            return

        current = self.root
        while True:
            if priority >= current.priority:
                if current.left is None:
                    current.left = new_node
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = new_node
                    break
                else:
                    current = current.right
    
    def extract_max(self):
        if self.root is None:
            print("Черга порожня")
            return None

        if self.root.left is None:
            max_node = self.root
            self.root = self.root.right
            return max_node.value, max_node.priority

        parent = self.root
        current = self.root.left

        while current.left is not None:
            parent = current
            current = current.left

        result = (current.value, current.priority)
        parent.left = current.right

        return result
    
    def view_queue(self):
        elements = []
        
        def _inorder_traverse(node):
            if node is not None:
                _inorder_traverse(node.left)      
                elements.append(f"('{node.value}', пріоритет: {node.priority})")
                _inorder_traverse(node.right)   
        
        _inorder_traverse(self.root)
        
        if not elements:
            print("Черга порожня")
        else:
            print("Поточна черга (від найвищого):")
            print(" -> ".join(elements))


if __name__ == "__main__":
    pq = BinaryTreePriorityQueue()

    while True:
        print("1.(Insert)")
        print("2.(Extract Max)")
        print("3.(View Queue)")
        print("4.(Exit)")
        
        choice = input("Оберіть дію (1-4): ")
        
        if choice == '1':
            val = input("Введіть значення (назву завдання): ")
            try:
                prio = int(input("Введіть пріоритет (ціле число): "))
                pq.insert(val, prio)
                print(f"-> Додано: '{val}' з пріоритетом {prio}")
            except ValueError:
                print("-> Помилка: Пріоритет має бути числом!")
                
        elif choice == '2':
            res = pq.extract_max()
            if res:
                print(f"-> Видалено елемент: {res}")
                
        elif choice == '3':
            pq.view_queue()
            
        elif choice == '0':
            print("Роботу завершено.")
            break
            
        else:
            print("-> Невідома команда. Спробуйте ще раз.")