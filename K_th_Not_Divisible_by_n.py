t=int(input())
arr=[]

def kth_not_divisible(n,k):
    low, high = 1, 2 * k 

    while low < high:
        mid = (low + high) // 2
        if mid - mid // n < k:
            low = mid + 1
        else:
            high = mid
    return low

for i in range(t):
    n, k = map(int, input().split())
    arr.append((n, k))

for n, k in arr:
    print(kth_not_divisible(n, k))