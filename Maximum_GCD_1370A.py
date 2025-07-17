t=int(input())
arr=[]

for _ in range(t):
    n=int(input())
    arr.append(n)

for i in range(t):
    n=arr[i]
    print(n//2)