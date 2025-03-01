str=input()
flag=0

if len(str) >=7:
    for i in range(len(str)-6):
        if str[i:i+7] == "1111111"or str[i:i+7] == "0000000":
            flag += 1
            break
        
if flag >= 1:
    print("YES")
else:
    print("NO")
    
    