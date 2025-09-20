t=int(input())
arr=[]
for i in range(t):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    arr.append((n,k,a))

for i in range(t):
    n, k, a = arr[i]
    st_arr=sorted(a)
    if st_arr==a:
        print("YES")
        continue
    if k>=2:
        print("YES")
    else:
        print("NO")