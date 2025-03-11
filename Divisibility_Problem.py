n=int(input())
arr=[]
count_arr=[]

for i in range(n):
    row=list(map(int, input().split()))
    arr.append(row)
    
for i in range(n):
    ele=arr[i]
    a=ele[0]
    b=ele[1]
    if a%b == 0:
        print(0) 
    else:
        c=a//b
        c+=1
        x=b*c
        y=x-a
        print(y)         
