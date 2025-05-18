n, q= map(int, input().split())
main=list(map(int, input().split()))
arr=[]
sum=0
for i in range(q):
    sub=list(map(int, input().split()))
    arr.append(sub)

for i in range(q):
    if arr[i][0] == 1:
        main[arr[i][1]-1] = arr[i][2]
        #sum of all elements in main
        sum=0
        for j in range(n):
            sum += main[j]
        print(sum)

    elif arr[i][0] == 2:
        #set all elements in main is equal to arr[i][1]
        for j in range(n):
            main[j] = arr[i][1]
        sum=0
        sum=arr[i][1]*n
        print(sum)
   
