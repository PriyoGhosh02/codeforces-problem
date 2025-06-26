n=int(input())
arr=[]
for i in range(n):
    arr.append(input())

for i in range(n):
    if arr[i][0]=='a' or arr[i][1]=='b' or arr[i][2]=='c':
        print("YES")
    else:
        print("NO")