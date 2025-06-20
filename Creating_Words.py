n=int(input())
arr=[]
for i in range(n):
    a=list(map(str,input().split()))
    arr.append(a)

for i in range(n):
    a=arr[i][0][0]
    a_ex=arr[i][0][1:]
    b=arr[i][1][0]
    b_ex=arr[i][1][1:]
    
    print(b+a_ex,a+b_ex)