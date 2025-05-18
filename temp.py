n=int(input())
arr = list(map(int, input().split()))

if n == 1:
    print(0)
elif n == 2:
    if arr[0] == arr[1]:
        print(0)
    else:
        print(1)
else:
    large_temp = 0
    small_temp = 0
    temp=0
    count=0
    large_temp = arr[0]
    small_temp = arr[0]
    for i in range(1, n):
        if arr[i] > large_temp:
            large_temp = arr[i]
            count += 1
        if arr[i] < small_temp:
            small_temp = arr[i]
            count += 1
    print(count)

