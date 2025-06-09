import math
n=int(input())
arr=[]
for i in range(n):
    a=list(map(int, input().split()))
    arr.append(a)

for i in range(n):
    dis=abs(arr[i][0] - arr[i][1])
    val=math.ceil(dis / 10)
    print(val)

