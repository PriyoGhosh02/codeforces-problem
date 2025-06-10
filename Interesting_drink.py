def count_less_equal(arr, x):
    left = 0
    right = len(arr)

    while left < right:
        mid = (left + right) // 2
        if arr[mid] <= x:
            left = mid + 1
        else:
            right = mid

    return left  

n = int(input())                            
prices = list(map(int, input().split()))  
prices.sort()                             

q = int(input())                           
days = [int(input()) for _ in range(q)]    

for m in days:
    affordable = count_less_equal(prices, m)
    print(affordable)
