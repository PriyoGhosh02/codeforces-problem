t=int(input())
arr=[]

for _ in range(t):
    n=int(input())
    s=input()
    arr.append((n,s))

for i in range(t):
    n,s=arr[i]
    if n == 5 and sorted(s) == sorted("Timur"):
        print("YES")
    else:
        print("NO")