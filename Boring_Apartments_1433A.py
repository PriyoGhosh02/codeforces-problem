n = int(input())
arr = []

for _ in range(n):
    x = input()
    arr.append(x)

for v in arr:
    dif=(int(v[0])-1)*10
    for i in range(1,len(v)+1):
        dif+=i
    print(dif)        