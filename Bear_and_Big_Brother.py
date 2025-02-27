lim,bob = map(int, input().split())

if 1<=lim<=bob<=10 and lim<=bob:
    for i in range(1,10):
        lim=lim*3
        bob=bob*2
        if lim>bob:
            print(i)
            break
