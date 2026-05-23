import sys

def get_min_beers(n, b, prefs):
    beer_masks = [0] * b
    for i in range(n):
        worker_pref = prefs[i]
        for j in range(b):
            if worker_pref[j] == 'Y':
                beer_masks[j] |= (1 << i)

    target_mask = (1 << n) - 1
    result = {"min": b}

    def backtrack(current_mask, count):
        if count >= result["min"]:
            return

        if current_mask == target_mask:
            result["min"] = count
            return

        first_uncovered = 0
        while (current_mask >> first_uncovered) & 1:
            first_uncovered += 1

        for j in range(b):
            if (beer_masks[j] >> first_uncovered) & 1:
                backtrack(current_mask | beer_masks[j], count + 1)

    backtrack(0, 0)
    return result["min"]

def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n = int(input_data[0])
    b = int(input_data[1])
    prefs = input_data[2:]
    
    print(get_min_beers(n, b, prefs))

if __name__ == "__main__":
    solve()