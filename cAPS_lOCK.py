str=input()

uppercase = 0
lowercase = 0

for i in range(len(str)):
    if str[i].isupper():
        uppercase += 1
    elif str[i].islower():
        lowercase += 1

if uppercase == len(str):
    print(str.lower())
elif str[0].islower() and lowercase==1:
    print(str.capitalize())
else:
    print(str)
    