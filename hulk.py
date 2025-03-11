n = int(input())
hate = "I hate"
love = "I love"
arr = []

for i in range(1, n + 1):
    if i % 2 != 0:
        arr.append(hate)
    elif i % 2 == 0:
        arr.append(love)

str=" that ".join(arr)
print(str+ " it")

