t=int(input())
arr=[]

for _ in range(t):
    n,k=map(int, input().split())
    a=list(map(int, input().split()))
    arr.append((n,k,a))

for i in range(t):
    n,k,a=arr[i]
    if k in a:
        print("YES")
    else:
        print("NO")