n=int(input())
coins=list(map(int, input().split()))[:n]
coins.sort()
coins.reverse()
count=0

for i in range(n+1):
    sum_bro=0
    sum_me=0
    for j in range(i):    
        sum_me+=coins[j]
    for j in range(i, n):
        sum_bro+=coins[j]
    count+=1
    if sum_me>sum_bro:
        break
        
print(count-1)