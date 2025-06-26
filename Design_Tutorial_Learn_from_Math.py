n=int(input())
low=0
high=0

def not_prime(n):
    if n <= 1:
        return False  # 0 and 1 are neither prime nor composite
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True  # Composite
    return False  # Prime

if n%2==0:
    low=n//2
    high=n//2
else:
    low=n//2
    high=n//2+1

while low>0 or high>0:
    if low+high==n and low>=4 and high>=4 and not_prime(low) and not_prime(high):
        print(low, high)
        break
    else:
        low-=1
        high+=1