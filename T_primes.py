import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    # Check from 5 to sqrt(n) with step of 6
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    sq = int(math.sqrt(arr[i]))  
    if sq * sq == arr[i] and is_prime(sq): 
        print("YES")
    else:
        print("NO")