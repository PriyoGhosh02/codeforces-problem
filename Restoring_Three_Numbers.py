arr=list(map(int,input().split()))
arr.sort()

a_b=arr[0]
a_c=arr[1]
b_c=arr[2]
a_b_c=arr[3]

a=a_b_c-a_b
b=a_b_c-a_c
c=a_b_c-b_c
print(a,b,c)