def reverse_string(s):
    return s[::-1]


s = input()
t = input()

r = reverse_string(s)
if r == t:
    print("YES")
else:
    print("NO")
