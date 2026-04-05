from collections import deque

def find_shortest_path(N, start_x, start_y, end_x, end_y):
    row = [2, 2, -2, -2, 1, 1, -1, -1]
    col = [-1, 1, 1, -1, 2, -2, 2, -2]
    
    queue = deque([(start_x, start_y, 0)])
    
    visited = set()
    visited.add((start_x, start_y))

    while queue:
        curr_x, curr_y, dist = queue.popleft()
        
        if curr_x == end_x and curr_y == end_y:
            return dist
            
        for i in range(8):
            next_x = curr_x + row[i]
            next_y = curr_y + col[i]
            
            if 0 <= next_x < N and 0 <= next_y < N and (next_x, next_y) not in visited:
                visited.add((next_x, next_y))
                queue.append((next_x, next_y, dist + 1))
                
    return -1

with open('negrolaba.txt', 'r', encoding='utf-8') as file:
    first_line = file.readline()
    n_text = first_line.split('#')[0]
    N = int(n_text.strip())
    
    second_line = file.readline()
    start_text = second_line.split('#')[0]
    start_parts = start_text.split(',')
    start_x = int(start_parts[0].strip())
    start_y = int(start_parts[1].strip())
    
    third_line = file.readline()
    end_text = third_line.split('#')[0]
    end_parts = end_text.split(',')
    end_x = int(end_parts[0].strip())
    end_y = int(end_parts[1].strip())

min_steps = find_shortest_path(N, start_x, start_y, end_x, end_y)

with open('output.txt', 'w', encoding='utf-8') as out_file:
    out_file.write(str(min_steps))
    
print(f"Розмір дошки: {N}")
print(f"Старт: ({start_x}, {start_y})")
print(f"Фініш: ({end_x}, {end_y})")
print(f"Мінімальна кількість кроків: {min_steps}")