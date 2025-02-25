col = 3
row = int(input())  

array = []

for i in range(row):
    sub_array = list(map(int, input().split()))
    
    if len(sub_array) != col or any(x not in [0, 1] for x in sub_array):
        exit()  
    array.append(sub_array)

res = 0 

for i in range(row):
    c = array[i].count(1)  
    if c >= 2:
        res += 1  

print(res)
