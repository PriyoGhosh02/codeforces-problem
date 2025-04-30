n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

for i in range(n):
    if arr[i]==1 or arr[i]==2:
        print(0)
    elif arr[i]%2!=0:
        print(int(arr[i]/2))
    elif arr[i]%2==0:
        print(int(arr[i]/2)-1)
