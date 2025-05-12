n, k= map(int, input().split())
time=240-k
count=0

for i in range(1, n+1):
    time -= i * 5
    if time >= 0:
        count += 1
    else:
        break

print(count)
