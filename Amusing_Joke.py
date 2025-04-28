str1=input()
str2=input()
str3=input()

temp=len(str1)+len(str2)
if temp!=len(str3):
    print("NO")
else:
    str1 = ''.join(sorted(str1 + str2))  
    str3 = ''.join(sorted(str3))  
    print(str1,str3)     
    if str1 == str3:
        print("YES")
    else:
        print("NO")


