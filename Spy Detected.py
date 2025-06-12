t=int(input())
arr=[]
for i in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    arr.append([n, a])

for i in range(t):
    a= arr[i][1]
    common=0
    if a[0]==a[1]:
        common=a[0]
    else:
        common=a[2] if a[0]==a[2] else a[1]

    clone_a = a
    clone_a=list(set(clone_a)) 
    uniqe= clone_a[0] if clone_a[1]==common else clone_a[1]
    
    index = a.index(uniqe)
    print(index+1)

