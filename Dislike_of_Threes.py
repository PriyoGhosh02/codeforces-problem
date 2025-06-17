def find_ith_valid(i):
    count = 0
    num = 1
    while True:
        if num % 3 != 0 and num % 10 != 3:
            count += 1
            if count == i:
                return num
        num += 1


n = int(input())
arr=[]
for i in range(n):
    arr.append(find_ith_valid(int(input())))

print("\n".join(map(str, arr)))

