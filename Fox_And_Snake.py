r, c = map(int, input().split())

for i in range(r):
    if i % 2 == 0:
        print("#" * c)  # Print an entire row of '#'
    else:
        if (i // 2) % 2 == 0:
            print("." * (c - 1) + "#")  # Snake tail on the right
        else:
            print("#" + "." * (c - 1))  # Snake tail on the left