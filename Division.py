n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

for i in range(n):
    val=arr[i]
    if val<=1399:
        print("Division 4")
    elif 1400<= val<=1599:
        print("Division 3")
    elif 1600 <= val<=1899:
        print("Division 2")
    else:
        print("Division 1")

