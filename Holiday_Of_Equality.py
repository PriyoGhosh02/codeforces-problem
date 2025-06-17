n=int(input())
arr=list(map(int, input().split()))
arr.sort()
sum=0
for i in range(n-1):
    sum+=(arr[-1]-arr[i])
print(sum)