n=int(input())
arr = []
for i in range(n):
    arr.append(input())

for i in range(n):
    arr[i]=arr[i].lower()
    if arr[i] == 'yes':
        print('YES')
    else:
        print("NO")
