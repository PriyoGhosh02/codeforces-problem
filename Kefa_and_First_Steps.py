n=int(input())
arr=list(map(int, input().split()))
frame=[]
count=1

if n==1:
    print(1)
    exit()
for i in range(n-1):
    if arr[i]<=arr[i+1]:
        count+=1
    else:
        count=1
    frame.append(count)

max=max(frame)
print(max)