n=int(input())
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))

for i in range(n):
    print(arr[i][1]-arr[i][0])

