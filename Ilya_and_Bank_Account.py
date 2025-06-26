n=int(input())
if n>=0:
    print(n)
else:
    n=str(n)
    if int(n[-1])>int(n[-2]):
        print(n[:-1])
    else:
        s= n[:-2]+n[-1]
        if s=='-0' or s=='0':
            print(0)
        else:
            print(s)
        