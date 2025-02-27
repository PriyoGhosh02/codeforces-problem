n=int(input())
str=input()
count=0

if 1<=n<=50:
    for i in range(n-1):
        if str[i]==str[i+1]:
            count+=1

print(count)