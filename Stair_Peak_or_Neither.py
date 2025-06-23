t=int(input())
arr=[]
for _ in range(t):
    a,b,c=map(int,input().split())
    arr.append((a, b, c))

for a, b, c in arr:
    if a<b and b<c:
        print("STAIR")
    elif a<b and b>c:
        print("PEAK")
    else:
        print("NONE")
    