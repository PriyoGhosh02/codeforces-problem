n=int(input())
str=[]

for i in range(n):
    s=input()
    str.append(s)

for i in range(n):
    ans=""
    ans+=str[i][0]
    for j in range(1,len(str[i])):
        if j%2!=0:
            ans+=str[i][j]
    print(ans)  