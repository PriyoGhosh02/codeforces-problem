ds = int(input())

stp = 0

if ds > 0:
    for i in range(ds):
        if ds >= 5:
            ds -= 5
            stp += 1
        elif ds >= 4:
            ds -= 4
            stp += 1
        elif ds >= 3:
            ds -= 3
            stp += 1
        elif ds >= 2:
            ds -= 2
            stp += 1
        elif ds >= 1:
            ds -= 1
            stp += 1
        elif ds==0:
            break
        
        

print(stp)
