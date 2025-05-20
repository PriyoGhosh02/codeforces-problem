n,m=map(int,input().split())
arr=list(map(int,input().split()))
present=1
total=0

for i in range(m):
    if arr[i]>present:
        total+=arr[i]-present
        present=arr[i]
    elif arr[i]<present:
        total+=((n-present)+arr[i])
        present=arr[i]
    else:
        present=arr[i]
        continue
    
print(total)
        
    