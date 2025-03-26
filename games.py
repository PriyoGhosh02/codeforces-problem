n=int(input())
match=[]
count=0

for i in range(n):
    sub=list(map(int, input().split()))
    match.append(sub)

for i in range(n):
    for j in range(n):
        if match[i][0]==match[j][1]:
            count+=1

print(count)