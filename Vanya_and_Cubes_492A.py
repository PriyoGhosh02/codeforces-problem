n= int(input())
res=0
limit=0
i=0

while limit <=n:
    i+=1
    limit = i * (i + 1) // 2
    if limit > n:
        break
    res+=1
    n -= limit

print(res)
    