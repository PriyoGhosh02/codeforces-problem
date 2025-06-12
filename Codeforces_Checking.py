n= int(input())
arr = []

for i in range(n):
    c=input()
    if c in "codeforces":
        arr.append("YES")   
    else:
        arr.append("NO")

print("\n".join(arr))