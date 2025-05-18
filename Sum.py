n=int(input())
arr=[]

for i in range(n):
    sec=list(map(int, input().split()))
    arr.append(sec)
   
for i in range(n):
    sum=0
    arr[i].sort()
    sum=arr[i][0]+arr[i][1]
    if sum==arr[i][2]:
        print("YES")
    else:
        print("NO")
    