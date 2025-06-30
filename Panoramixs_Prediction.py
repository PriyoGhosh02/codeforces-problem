x, y = map(int, input().split())

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if is_prime(x) and is_prime(y):
    if x>y:
        print("NO")
    else:
        flag=0
        prime=x
        if prime ==1:
            prime = 2
        while flag==0:
            prime += 1
            if is_prime(prime):
                flag=1
        if prime == y:
            print("YES")
        else:
            print("NO")
else:
    print("NO")