n = int(input())
arr = list(map(int, input().split()))

max_val = max(arr)
min_val = min(arr)

if max_val == arr[0] and min_val == arr[n - 1]:
    print(0)
    exit()
else:
    ind_min = len(arr) - 1 - arr[::-1].index(min_val)  # it find the last index in array
    temp = ind_min
    ind_max = arr.index(max_val)
    ind_min = abs(ind_min - (n - 1))
    swap = ind_min + ind_max

if temp < ind_max:
    print(swap-1)
    exit()   
print(swap)

