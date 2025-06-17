n = int(input())
arr = list(map(int, input().split()))
sereja = 0
dima = 0

for i in range(n):
    if i % 2 == 0:
        s_max= max(arr[0], arr[-1])
        sereja += s_max
        arr.remove(s_max)
    else:
        d_max = max(arr[0], arr[-1])
        dima += d_max
        arr.remove(d_max)

print(sereja, dima)
