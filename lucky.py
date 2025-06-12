n=int(input())
arr=[]
for i in range(n):
    arr.append(input())

for i in range(n):
    val=arr[i]
    str1=int(val[0])+int(val[1])+int(val[2])
    str2=int(val[3])+int(val[4])+int(val[5])

    if str1==str2:
        print("Yes")
    else:
        print("No")

