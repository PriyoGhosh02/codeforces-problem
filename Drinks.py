n= int(input())
sum=0

arr=list(map(int, input().split()))[:n]

for i in range(n):
    sum+=arr[i]

print(f"{sum/n:.12f}")