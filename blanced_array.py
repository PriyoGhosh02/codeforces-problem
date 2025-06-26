n=int(input())
arr=[]

def number_sum_and_list(n, start):
    numbers = []
    total_sum = 0
    current = start
    for _ in range(n):
        numbers.append(current)
        total_sum += current
        current += 2
    return total_sum, numbers

for i in range(n):
    arr.append(int(input()))

        
for i in range(n):
    if arr[i] % 4 == 0:
        print("YES")
        e_sum, e_a = number_sum_and_list(arr[i] // 2, 2)
        o_sum, o_a = number_sum_and_list(arr[i] // 2 - 1, 1)
        o_a.append(e_sum - o_sum)  
        print(' '.join(map(str, e_a + o_a)))
    else:
        print("NO")