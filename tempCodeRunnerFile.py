n=int(input())
arr=list(map(int, input().split()))

for i in range(n):
    divisior=[]
    for j in range(1,(arr[i]//2)+1):
        div=arr[i]/j
        if div==int(div):
            divisior.append(j)
            divisior.append(int(div))
    divisior=set(divisior)
    if len(divisior)==3:
        print("YES")
    else:
        print("NO")
