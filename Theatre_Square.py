import math
n, m, a = map(int, (input().split()))

res = math.ceil(n / a) * math.ceil(m / a)

print(res)
