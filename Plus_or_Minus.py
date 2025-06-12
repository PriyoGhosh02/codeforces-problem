n=int(input())
arr=[]
for i in range(n):
    a=list(map(int, input().split()))
    arr.append(a)

for i in range(n):
    if arr[i][0] + arr[i][1]==arr[i][2]:
        print('+')
    elif arr[i][0] - arr[i][1]==arr[i][2]:
        print('-')