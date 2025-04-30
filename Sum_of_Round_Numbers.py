n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

for i in range(n):
    count = 0
    mod = []
    val = arr[i]

    # keep subtracting the largest round component
    while val > 0:
        if val % 10 != 0:
            count += 1
            mod.append(val % 10)
            val -= val % 10
        elif val % 100 != 0:
            count += 1
            mod.append(val % 100)
            val -= val % 100
        elif val % 1000 != 0:
            count += 1
            mod.append(val % 1000)
            val -= val % 1000
        elif val % 10000 != 0:
            count += 1
            mod.append(val % 10000)
            val -= val % 10000
        elif val % 100000 != 0:
            count += 1
            mod.append(val % 100000)
            val -= val % 100000
        elif val % 1000000 != 0:
            count += 1
            mod.append(val % 1000000)
            val -= val % 1000000

    print(count)
    print(*mod)
