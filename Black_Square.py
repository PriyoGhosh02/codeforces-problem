a,b,c,d=map(int,input().split())
s=input()
cal=0

for i in s:
    if i == '1':
        cal += a
    elif i == '2':
        cal += b
    elif i == '3':
        cal += c
    elif i == '4':
        cal += d
        
print(cal)