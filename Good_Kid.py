t=int(input())
arr=[]
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    arr.append((n,a))

for i in range(t):
    n,a=arr[i]
    min_val=min(a)
    a.remove(min_val)
    res=1
    for num in a:
        res*=num
    
    print(res*(min_val+1))
