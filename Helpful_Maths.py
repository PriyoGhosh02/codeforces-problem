eq= input()

tem=list(eq.split('+'))
sort=[]
for i in range(len(tem)):
    sort.append(tem[i])

sort.sort()   
print('+'.join(sort)) 
