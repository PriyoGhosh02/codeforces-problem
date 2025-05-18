n = int(input())
arr = list(map(int, input().split()))
count = 0

if n == 1:
    print(0)
    exit()
elif n == 2:
    if arr[0] < arr[1]:
        print(2)
        exit()
    else:
        print(1)
        exit()
else:
    temp = arr[0]
    for i in range(1, n):
        if arr[i] > temp:
            count += 1
            temp = arr[i]
        else:
            continue
    if count==0:
        print(2)
    elif count>0:
        print(count+1)
