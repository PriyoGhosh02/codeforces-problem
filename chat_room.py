str = input()
j = 0
msg = "hello"

if len(str) >= 1 and len(str) <= 100:
    for i in range(len(str)):
        if str[i] == msg[j]:
            j += 1
            if j == 5:
                print("YES")
                break
    if j != 5:
        print("NO")
