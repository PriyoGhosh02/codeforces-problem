n, t = map(int, input().split())
arr = list(map(int, input().split()))

indx = 1
for i in range(t):
    if indx < t:
        indx = indx + arr[indx - 1]
    else:
        break
       
if indx == t:
    print("YES")
else:
    print("NO")
