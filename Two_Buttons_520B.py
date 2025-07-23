def min_steps(start, target):
    steps = 0
    while target > start:
        if target % 2 == 0:
            target //= 2
        else:
            target += 1
        steps += 1
    return steps + (start - target)

s,t= map(int, input().split())
print(min_steps(s, t))