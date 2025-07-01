n=int(input())
a=[]
for i in range(n):
    a.append([int(input()),list(map(int, input().split()))])

for i in range(n):
    e_sum=0
    o_sum=0
    for j in a[i][1]:
        if j%2==0:
            e_sum+=j
        else:
            o_sum+=j
    
    if e_sum%2==0 and o_sum%2==0:
        print("YES")
    elif e_sum%2==1 and o_sum%2==1:
        print("YES")
    else:
        print("NO")
        

