n=int(input())
arr_ind=[]
arr_val=[]
for i in range(n):
    arr_ind.append(int(input()))
    arr_val.append(list(map(int, input().split())))

for i in range(n):
    count=0
    max_cun=0
    for j in range(arr_ind[i]):
        if arr_val[i][j]==0:
            count+=1
        else:
            count=0
        if count>max_cun:
            max_cun=count
    print(max_cun)
            