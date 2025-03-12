n = int(input())

arr1 = list(map(int, input().split()))[1:]
arr2 = list(map(int, input().split()))[1:]

arr = list(set(arr1).union(arr2))
level = list(range(1, n + 1))

if level == arr:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
