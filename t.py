import  math
n=int(input())
arr=list(map(int, input().split()))

taxi=0
count4=0
count3=0
count2=0
count1=0
for i in arr:
    if i==4:
        count4+=1
    elif i==3:
        count3+=1
    elif i==2:
        count2+=1
    elif i==1:
        count1+=1

taxi=count4

if count3>=count1:
    taxi+=count3
    count1=0
else:
    taxi+=count3
    count1-=count3
if count2%2==0:
    taxi+=count2//2
    count2=0
else:
    taxi+=count2//2
    count2=1
if count2==1:
    taxi+=1
    count1-=2
if count1>0:
    taxi+=math.ceil(count1/4)

print(taxi)
