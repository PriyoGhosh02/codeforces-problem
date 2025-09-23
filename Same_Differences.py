t = int(input())
arr = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    arr.append((n, a))

for n, a in arr:
    freq = {}   # normal dict
    count = 0
    
    for i in range(n):
        key = a[i] - i
        if key in freq:
            count += freq[key]   # all earlier indices with same key form valid pairs
            freq[key] += 1
        else:
            freq[key] = 1
    
    print(count)
