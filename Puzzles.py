n, m = map(int, input().split())             
arr = list(map(int, input().split()))  
sub = []
dest = []     

arr.sort()
for i in range((m-n)+1):
    for j in range(i,n+i):
        sub.append(arr[j])
    dest.append(max(sub)-min(sub))
    sub = []
    
dest.sort()
print(dest[0])
