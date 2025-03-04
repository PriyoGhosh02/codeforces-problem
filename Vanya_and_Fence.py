from math import ceil
n,h=map(int, input().split())
a=list(map(int, input().split()))

if n==len(a):
    width=0
    for i in range(n):
        temp=ceil(a[i]/h)
        width+=temp

print(width)