n = int(input())
arr = []
count_dict = {}

for _ in range(n):
    word = input()
    arr.append(word)

for word in arr:
    if word not in count_dict:
        print("OK")
        count_dict[word] = 1
    else:
        print(f"{word}{count_dict[word]}")
        count_dict[word] += 1
