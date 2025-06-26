n, t = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
total = 0
max_books = 0

for right in range(n):
    total += arr[right]

    while total > t:
        total -= arr[left]
        left += 1

    max_books = max(max_books, right - left + 1)

print(max_books)
