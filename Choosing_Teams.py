n, k = map(int, input().split())
teams= list(map(int, input().split()))
teams.sort()
count = 0

for i in range(n):
    if teams[i]+ k <= 5:
        count += 1
    else:
        break

print(count // 3)  