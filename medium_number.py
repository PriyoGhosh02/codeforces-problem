n=int(input())
arr = []
for i in range(n):
    a=list(map(int, input().split()))
    arr.append(a)

for i in range(n):
    a=arr[i]
    a.sort()
    print(a[1])