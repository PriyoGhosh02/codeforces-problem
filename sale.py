n, m = map(int, input().split())
arr = list(map(int, input().split()))
sum = 0
i = 0
arr.sort()
while i < n and i < m and arr[i] < 0:
    sum += arr[i]
    i += 1

print(abs(sum))