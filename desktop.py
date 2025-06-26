def number_sum_and_list(n, start):
    numbers = []
    total_sum = 0
    current = start
    for _ in range(n):
        numbers.append(current)
        total_sum += current
        current += 2
    return total_sum, numbers

# Example usage
n = 200000
start = 2  # You can change this to 1, 4, etc.
total_sum, numbers = number_sum_and_list(n, start)
print(f"First {n} numbers starting from {start} with diff 2: {numbers}")
print(f"Sum: {total_sum}")
