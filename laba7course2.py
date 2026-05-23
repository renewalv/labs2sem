import pandas as pd

class DSU:
    """Disjoint Set Union"""
    def __init__(self, nodes):
        self.parent = {node: node for node in nodes}
        self.num_components = len(nodes)

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_i] = root_j
            self.num_components -= 1
            return True
        return False

def calculate_min_cable(file_path):
    try:
        df = pd.read_csv(file_path, header=None, names=['K1', 'K2', 'Distance'])
        
        wells = set(df['K1']).union(set(df['K2']))
        if not wells:
            return 0
        
        edges = []
        for _, row in df.iterrows():
            edges.append((row['Distance'], row['K1'], row['K2']))
        edges.sort() 
        
        dsu = DSU(wells)
        total_length = 0
        
        for length, u, v in edges:
            if dsu.union(u, v):
                total_length += length
        
        if dsu.num_components == 1:
            return int(total_length)
        else:
            return -1

    except FileNotFoundError:
        return "Файл не знайдено"
    except Exception as e:
        return f"Помилка: {e}"

result = calculate_min_cable('communication_wells.csv')
print(f"Мінімальна довжина кабелю: {result}")