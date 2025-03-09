n = int(input())
arr = []
count = 0

for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

for i in range(n):
    sum = abs(arr[i][0] - arr[i][1])
    if sum >= 2:
        count += 1

print(count)