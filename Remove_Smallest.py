t=int(input())
arr=[]
for i in range(t):
    n=int(input())
    a=list(map(int, input().split()))
    a.sort()
    arr.append([n, a])

for i in range(t):
    a=arr[i][1]
    n=arr[i][0]
    if n== 1:
        print("YES")
    elif len(set(a)) == 1:
        print("YES")
    else:
        for j in range(1, n):
            if a[j] - a[j - 1] > 1:
                print("NO")
                break
        else:
            print("YES")


