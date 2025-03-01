n= int(input())
arrX,arrY,arrZ= [],[],[]
sumX,sumY,sumZ=0,0,0

for i in range(n):
    x,y,z= map(int, input().split())
    arrX.append(x)
    arrY.append(y)
    arrZ.append(z)
    sumX += x
    sumY += y   
    sumZ += z
        
if sumX == 0 and sumY == 0 and sumZ == 0:
    print("YES")
else:
    print("NO")
    
