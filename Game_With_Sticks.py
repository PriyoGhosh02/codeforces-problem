n,m=map(int,input().split())

if n<m:
    min=n
else:
    min=m
if min%2==0:
    print("Malvika")
else:
    print("Akshat")