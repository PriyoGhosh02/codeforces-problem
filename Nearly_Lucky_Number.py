n = input()
count = 0

for i in range(len(n)):
    if n[i] == "4" or n[i] == "7":
        count += 1
    
if count == 4 or count == 7:
    print("YES")
else:
    print("NO")





# wrong but first check
# n=input()
# flag=0

# for i in range(len(n)):
#     if n[i] != "4" and n[i] != "7":
#         flag += 1
#         break
    
# if flag >= 1:
#     print("NO")
# else:
#     print("YES")