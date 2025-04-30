import math
arr= list(map(int, input().split()))

sum=arr[0]+arr[1]+arr[2]
avg=sum/3
cill=0
flor=0
meet=0
dis=0

if '.'in str(avg):
    for i in range(3):
        if arr[i] >= avg:
            cill+=1
        else:
            flor+=1
    if flor>cill:
        meet= math.floor(avg)
    else:
        meet= math.ceil(avg)
else:
    meet=avg
    
for i in range(3):
    dis+=abs(arr[i]-meet)

print(dis)