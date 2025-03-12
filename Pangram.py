n=int(input())
str=input()

if len(str)==n:
    str=str.lower()
    unq = sorted(set(str))
    if len(unq)==26:
        print("YES")
    else:
        print("NO")