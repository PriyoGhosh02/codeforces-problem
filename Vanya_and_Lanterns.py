n,l=map(int, input().split())
arr=list(map(int, input().split()))
arr.sort()

sub=[]
for i in range(n-1):
    s = (arr[i+1] - arr[i])/2
    sub.append(s)

if arr[0] != 0:
    sub.append(arr[0])
if arr[n-1] != l:
    sub.append(l - arr[n-1])

print(max(sub))