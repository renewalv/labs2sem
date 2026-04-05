def get_max(a, b):
    if a > b:
        return a
    return b

def parse_input(raw_text):
    raw_text += " "
    char_to_num = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

    n = 0
    w = 0
    h = 0
    current_number = 0
    number_index = 0
    is_reading_number = False

    for char in raw_text:
        if char in char_to_num:
            current_number = current_number * 10 + char_to_num[char]
            is_reading_number = True    
        elif is_reading_number:
            if number_index == 0:
                n = current_number
            elif number_index == 1:
                w = current_number
            elif number_index == 2:
                h = current_number

            current_number = 0
            number_index += 1
            is_reading_number = False

    return n, w, h

def solve(n, w, h):
    left = get_max(w, h) - 1
    right = get_max(w, h) * n 
    iterations = 0

    while right - left > 1:
        iterations += 1
        middle = (left + right) // 2 

        if (middle // w) * (middle // h) >= n:
            right = middle
        else:
            left = middle
            
    print(f"Ітерацій: {iterations}")
    return right