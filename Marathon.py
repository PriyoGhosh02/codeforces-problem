n=int(input())
arr=[]
for i in range(n):
    a=list(map(int,input().split()))
    arr.append(a)

for i in range(n):
    count=0
    for j in range(1,4):
        temp=arr[i][0]
        if arr[i][j]>temp:
            count+=1
        else:
            continue
    print(count)