n=int(input())
arr = []

for i in range(n):
    val= input()
    sum=int(val[0])+int(val[1])
    arr.append(sum)

print("\n".join(map(str, arr)))
