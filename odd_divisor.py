n = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

for num in arr:
    if num & (num - 1) == 0:
        print("NO")
    else:
        print("YES")    

    # if num ==1 or num == 2:
    #     print("NO")
    # elif num%2!= 0:
    #     print("YES")
    # else:
    #     num_copy = num/2
    #     if num_copy % 2 != 0:
    #         print("YES")
    #     else:
    #         print("NO")

