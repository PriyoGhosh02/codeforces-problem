a=input()
b=input()
# xor logic
result = bin(int(a, 2) ^ int(b, 2))[2:]
gap= len(a) - len(result)

if gap > 0:
    result = '0' * gap + result
print(result)