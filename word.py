str=input()
c=0
s=0

if len(str)>=1 and len(str)<=100:
    for i in range (len(str)):
        if str[i].isupper():
            c+=1
        else:
            s+=1

if c>s:
    print(str.upper())
else:
    print(str.lower())            
        