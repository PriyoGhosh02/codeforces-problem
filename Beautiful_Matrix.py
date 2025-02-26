array = []
pos = (-1, -1)  

for i in range(5):
    sub_array = list(map(int, input().split()))
    
    if len(sub_array) != 5 or any(x not in [0, 1] for x in sub_array):
        exit()

    if 1 in sub_array:  
        pos = (i, sub_array.index(1))  # Get row index `i` and column index `index(1)`

    array.append(sub_array)

if pos == (-1, -1):
    exit()  # Exit if no '1' is found

# print(f"Position of 1: Row {pos[0] + 1}, Column {pos[1] + 1}")  # Convert to 1-based index

res= ((abs((pos[0]+1)-3))+(abs((pos[1]+1)-3))) 

print(res)

