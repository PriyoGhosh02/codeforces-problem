n, k = map(int, input().split())

if 1 <= k <= 50:
    for i in range(k):
        if n % 10 == 0:
            n = n // 10
        else:
            n = n - 1

print(n)
