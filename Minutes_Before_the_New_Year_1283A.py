t=int(input())
arr = []
day_min=1440

for _ in range(t):
    h, m= map(int, input().split())
    arr.append((h, m))

for h, m in arr:
    curr= h * 60 + m
    print(day_min - curr)  # Calculate minutes before the new year