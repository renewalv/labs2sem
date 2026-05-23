import math

def calculate_max_wire(w, heights):
    n = len(heights)
    if n < 2:
        return 0.0

    dp = [[0.0, 0.0] for _ in range(n)]

    for i in range(1, n):
        low_to_low = dp[i-1][0] + math.sqrt(w**2 + (1 - 1)**2)
        high_to_low = dp[i-1][1] + math.sqrt(w**2 + (heights[i-1] - 1)**2)
        dp[i][0] = max(low_to_low, high_to_low)

        low_to_high = dp[i-1][0] + math.sqrt(w**2 + (1 - heights[i])**2)
        high_to_high = dp[i-1][1] + math.sqrt(w**2 + (heights[i-1] - heights[i])**2)
        dp[i][1] = max(low_to_high, high_to_high)

    return max(dp[n-1][0], dp[n-1][1])

def solve():
    print("Програма розрахунку електромережі Вільшанки")
    try:
        line1 = input("Введіть відстань w: ").strip()
        if not line1: return
        w = int(line1)

        line2 = input("Введіть висоти: ").strip()
        if not line2: return
        heights = list(map(int, line2.split()))
        
        if len(heights) < 2:
            print("результат: 0.00 треба мінімум 2 стовпи для розрахунку")
            return

        result = calculate_max_wire(w, heights)
        print(f"\nМаксимально необхідна довжина дроту: {result:.2f}")

    except ValueError:
        print("error, треба цілі числа")

if __name__ == "__main__":
    solve()