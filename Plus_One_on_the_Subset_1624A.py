t= int(input())
arr=[]

for _ in range(t):
    n=int(input())
    a= list(map(int, input().split()))
    arr.append((n, a))

for n, a in arr:
    min_val= min(a)
    max_val= max(a)
    print(max_val - min_val)  