t=int(input())
arr=[]
for i in range(t):
    arr.append(list(map(int, input().split())))

for i in range(t):
    x=arr[i][0]
    y=arr[i][1]
    n=arr[i][2]
    print(n - (n - y) % x)
    
    # for m in range((n//x),0,-1):
    #     k=(m*x)+y
    #     if k<=n:
    #         print(k)
    #         break
