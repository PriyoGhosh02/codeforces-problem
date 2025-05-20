arr=list(map(int,input().split()))

if arr[0]==arr[1]:
    print(arr[0],0)
else:
    arr.sort()
    dif=arr[0]
    sme=arr[1]-arr[0]
    sme//=2
    print(dif,sme)
    