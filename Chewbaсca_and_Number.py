s=int(input())
n_str=str(s)
val=''

for i in range(len(n_str)):
    n=int(n_str[i])
    if i==0 and n==9:
        val+='9'
    elif n<(9-n):
        val+=str(n)
    else:
        val+=str(9-n)

print(int(val))  