t=int(input())
arr=[]
for _ in range(t):
    s=input()
    arr.append(s)
    
for word in arr:
    len_s=len(word)
    
    if len_s%2==0:
        mid = len(word) // 2
        first_half = word[:mid]
        second_half = word[mid:]
        if first_half == second_half:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")