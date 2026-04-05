class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def print_tree(self):
        canvas = [[" "] * 100 for _ in range(40)]
        
        def draw(node, r, c, dir_x, h_step, v_step):
            if not node: return
            
            for i, char in enumerate(str(node.value)):
                canvas[r][c + i] = char
            
            if node.left:
                canvas[r - max(1, v_step // 2)][c + (dir_x * h_step) // 2] = "\\" if dir_x == -1 else "/"
                draw(node.left, r - v_step, c + dir_x * h_step, dir_x, max(2, h_step - 2), max(2, v_step // 2))
                
            if node.right:
                canvas[r + max(1, v_step // 2)][c + (dir_x * h_step) // 2] = "/" if dir_x == -1 else "\\"
                draw(node.right, r + v_step, c + dir_x * h_step, dir_x, max(2, h_step - 2), max(2, v_step // 2))

        root_r = 18
        canvas[root_r][40:42] = list(str(self.value))
        
        if self.left:
            canvas[root_r][36:39] = ["-", "-", "-"]
            draw(self.left, root_r, 34, -1, 6, 8)
            
        if self.right:
            canvas[root_r][43:46] = ["-", "-", "-"]
            draw(self.right, root_r, 47, 1, 6, 8)

        for row in canvas:
            line = "".join(row).rstrip()
            if line: print(line)

def build_from_list(arr):
    if not arr or arr[0] in ("N", None):
        return None
    
    root = BinaryTree(int(arr[0]))
    queue = [root]
    
    i = 1
    
    while queue and i < len(arr):
        current = queue.pop(0)
        
        if i < len(arr) and arr[i] not in ("N", None):
            current.left = BinaryTree(int(arr[i]))
            queue.append(current.left)
        i += 1
        
        if i < len(arr) and arr[i] not in ("N", None):
            current.right = BinaryTree(int(arr[i]))
            queue.append(current.right)
        i += 1

    return root

def read_list_from_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read().split()
            if not content:
                return []
            return [int(num) for num in content]
    except FileNotFoundError:
        print(f"Помилка: Файл '{filename}' не знайдено.")
        return []
    except ValueError:
        print("Помилка: У файлі є символи, які не є числами.")
        return []

def main():
    file_name = 'derevonegra.txt'
    
    tree_list = read_list_from_file(file_name)
    
    if not tree_list:
        print("Не вдалося отримати дані для побудови дерева.")
        return

    print(f"Дані для дерева з файлу '{file_name}': {tree_list}\n")
    
    root = build_from_list(tree_list)
    
    if root:
        root.print_tree()
    else:
        print("Дерево порожнє")

if __name__ == "__main__":
    main()