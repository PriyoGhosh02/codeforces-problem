str=input()
st=0
for i in range(len(str)):
    if i==0:
        st=str[i].upper()
    else:
        st+=str[i]
print(st)
