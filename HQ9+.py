str=input()
code="HQ9"
flag=0

for i in str:
    if i in code:
        print("YES")
        flag=1
        break

if flag==0:
    print("NO")