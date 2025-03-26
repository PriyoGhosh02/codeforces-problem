n=int(input())
arr=list(map(int, input().split()))
count_even=0
count_odd=0

for i in range(3):
    if arr[i]%2==0:
        count_even+=1
    else:
        count_odd+=1

if count_even>count_odd:
    for i in range(n):
        if arr[i]%2!=0:
            print(i+1)
            break
else:
    for i in range(n):
        if arr[i]%2==0:
            print(i+1)
            break

