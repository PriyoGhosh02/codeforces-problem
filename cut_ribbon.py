n,a,b,c=map(int, input().split())
arr = list(set([a, b, c]))
count=[0]+ [-10**9]*n

for i in range(1, n + 1):
    if i>=a:
        count[i] = max(count[i], count[i - a] + 1)
    if i>=b:
        count[i] = max(count[i], count[i - b] + 1)  
    if i>=c:
        count[i] = max(count[i], count[i - c] + 1)
        
print(count[n])