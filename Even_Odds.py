n, pos = map(int, input().split())  

odd_count = (n + 1) // 2  

if pos <= odd_count:  
    print((2 * pos) - 1)  
else:  
    print(2 * (pos - odd_count)) 
