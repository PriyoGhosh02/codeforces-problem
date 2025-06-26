n=int(input())
code=[]
math=[]
phys=[]
arr=list(map(int, input().split()))

for i in range(n):
    a=arr[i]
    if a==1:
        code.append(i+1)
    elif a==2:
        math.append(i+1)
    elif a==3:
        phys.append(i+1)
        
min_length = min(len(code), len(math), len(phys))
if min_length == 0:
    print(0)
else:
    print(min_length)
    for i in range(min_length):
        print(code[i], math[i], phys[i])