n=int(input())
arr=[]
for i in range(n):
    a=list(map(int,input().split()))
    arr.append(a)

for i in range(n):
    a=arr[i][0]
    b=arr[i][1]
    c=arr[i][2]
    if a+b>=10 or a+c>=10 or b+c>=10:
        print("YES")
    else:
        print("NO")

