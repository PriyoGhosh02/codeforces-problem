k, l, m, n,d = (int(input()) for _ in range(5))
count=0

for i in range(1,d+1):
    if i%k==0:
        count+=1
        continue
    if i%l==0:
        count+=1
        continue
    if i%m==0:
        count+=1
        continue
    if i%n==0:
        count+=1
        continue
    

print(count)
