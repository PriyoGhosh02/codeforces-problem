n, k = map(int, input().split())

arr = []
values = input().split()

for i in range(n):
    arr.append(int(values[i]))

high = arr[k - 1]
count = 0

for i in range(n):
    if arr[i] >= high and arr[i] > 0:
        count += 1

print(count)
