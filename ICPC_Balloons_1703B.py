t=int(input())
arr=[]

for _ in range(t):
    n=int(input())
    s=input()
    arr.append((n,s))

for n,s in arr:
    set_s=set(s)
    print((len(set_s)*2)+(len(s)-len(set_s)))