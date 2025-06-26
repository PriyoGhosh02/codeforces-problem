n=int(input())
arr=[]
c="codeforces"
for i in range(n):
    arr.append(input())

for i in range(n):
    count = 0
    for j in range(len(arr[i])):
        if arr[i][j] != c[j]:
            count += 1
    print(count)