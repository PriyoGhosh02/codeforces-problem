n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
    
for i in range(n):
    if arr[i] % 3 == 0:
        print("Second")
    else:
        print("First")