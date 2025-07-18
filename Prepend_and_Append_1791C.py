t = int(input())
arr = []

for _ in range(t):
    n = int(input())
    a = input()
    arr.append((n, a))

for n, a in arr:
    res = n
    i = 0
    j = n - 1

    while i < j and a[i] != a[j]:
        res -= 2
        i += 1
        j -= 1

    print(res)
