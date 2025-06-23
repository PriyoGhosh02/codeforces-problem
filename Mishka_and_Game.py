r=int(input())
arr=[]
for i in range(r):
    m, c = map(int, input().split())
    arr.append((m, c))
mishka = 0
chris = 0
for m, c in arr:
    if m > c:
        mishka += 1
    elif c > m:
        chris += 1

if mishka > chris:
    print("Mishka")
elif chris > mishka:
    print("Chris")
else:
    print("Friendship is magic!^^")
