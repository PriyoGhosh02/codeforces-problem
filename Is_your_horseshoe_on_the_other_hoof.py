shoe=list(map(int, input().split()))
shoe_unq=set(shoe)
need=len(shoe)-len(shoe_unq)
print(need)