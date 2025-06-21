n=int(input())
arr=[]
for i in range(n):
    arr.append(input())
count1=0 
count2=0
temp1=arr[0]
temp2=0
for i in range(n):
    if arr[i]==temp1:
        count1+=1
    else:
        count2+=1
        temp2=arr[i]

if count1>count2:
    print(temp1)
else:
    print(temp2)
    