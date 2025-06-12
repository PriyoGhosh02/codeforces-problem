str=input().strip()
digit=''

i=0
while i<len(str):
    if str[i]=='.':
        digit+='0'
        i+=1
    elif str[i]=='-':
        if i+1<len(str) and str[i+1]=='-':
            digit+='2'
        else:
            digit+='1'
        i+=2
print(digit)