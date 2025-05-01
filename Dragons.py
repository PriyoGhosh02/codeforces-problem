s, n = map(int, input().split())
arr=[]
for i in range(n):
    x,y= map(int, input().split())
    arr.append((x,y))
  
# Kirito can fight the dragons in any order.    
arr.sort(key=lambda x: x[0])
win=0
for i in range(n):
    if s>arr[i][0]:
        s+=arr[i][1]
        win+=1

if win==n:
    print("YES")
else:
    print("NO")