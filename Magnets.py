n = int(input())
arr = []
count = 1

for i in range(n):
    arr.append(int(input()))

for i in range(n - 1):
    if arr[i] != arr[i + 1]:
        count += 1

print(count)
