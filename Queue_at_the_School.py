p,l=map(int, input().split())
str=input()

if len(str)==p:
    for i in range(l):
        str=str.replace("BG", "GB")
    print(str)
