import math
x, y= map(int, input().split())
maximum=max(x, y)
gap=(6-maximum) + 1
g=math.gcd(gap, 6)
print(f"{gap//g}/{6//g}")