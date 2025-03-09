n= int(input())
arr=list(map(int, input().split()))[:n]
res=[]

for i in range(1,n+1):
    pos=arr.index(i)
    res.append(pos+1)

print(' '.join(map(str, res)))