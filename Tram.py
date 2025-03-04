n= int(input())
arr=[]
sum=0
capacity=[]

for i in range(n):
    row=list(map(int, input().split()))
    arr.append(row)

if arr[0][0]==0:
    for i in range(n):
        sum-=arr[i][0]
        sum+=arr[i][1]
        capacity.append(sum)

if arr[0][0]==0 and sum==0:
    a=max(capacity)
    print(a)
    