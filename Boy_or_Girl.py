s = input()

unique_chars = set(s)  # Get unique characters

n = len(unique_chars)
if n % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
