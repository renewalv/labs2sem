def find_broken_conveyor_section(serial_numbers):
    n = len(serial_numbers)

    if n <= 1:
        return (-1, -1)
    
    left = 0
    while left < n - 1 and serial_numbers[left] <= serial_numbers[left + 1]:
        left += 1
        
    if left == n - 1:
        return (-1, -1)
        
    right = n - 1 
    while right > 0 and serial_numbers[right] >= serial_numbers[right - 1]:
        right -= 1 

    broken_min = serial_numbers[left]
    broken_max = serial_numbers[left]
    
    for i in range(left + 1, right + 1):
        if serial_numbers[i] < broken_min:
            broken_min = serial_numbers[i]
        if serial_numbers[i] > broken_max:
            broken_max = serial_numbers[i]
            
    while left > 0 and serial_numbers[left - 1] > broken_min:
        left -= 1
    
    while right < n - 1 and serial_numbers[right + 1] < broken_max:
        right += 1
        
    return (left, right)


print("--- СИСТЕМА ДІАГНОСТИКИ КОНВЄЄРА ---")
print("Введіть сер ноиери ")
print("-" * 36)

user_input = input("масив: ")

try:
    conveyor_line = [int(x) for x in user_input.split()]
    
    broken_start, broken_end = find_broken_conveyor_section(conveyor_line)

    print("\n--- РЕЗУЛЬТАТ ДІАГНОСТИКИ ---")
    if broken_start == -1:
        print("Лінія працює ідеально")
    else:
        print(f"Знайдено злам порядку.")
        print(f"Індекси проблемної ділянки: ({broken_start}, {broken_end})")
        print(f"Деталі, які потрібно пересортувати: {conveyor_line[broken_start:broken_end + 1]}")

except ValueError:
    print("\nПомилка: Ви ввели недопустимі символи")