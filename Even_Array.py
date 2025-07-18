t=int(input())
arr=[]

for _ in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    arr.append((n,a))
    
for i in range(t):
    n=arr[i][0]
    a=arr[i][1]
    e_count=0
    o_count=0
    for j in range(n):        
        val=a[j]
        if val%2!=j%2:
            if j%2==0:
                e_count+=1
            else:
                o_count+=1
        
    if e_count==o_count:
        print(e_count)
    else:
        print(-1)
    
            