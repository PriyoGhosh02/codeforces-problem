arr = list(map(int, input().split()))

dis=max(arr) - min(arr)
print(dis)


#wrong process trying

# import math
# arr = list(map(int, input().split()))

# sum = arr[0] + arr[1] + arr[2]
# avg = sum / 3
# cill = 0
# flor = 0
# meet = 0
# dis = 0

# if avg != int(avg):  
#     for i in range(3):
#         if arr[i] >= avg:
#             cill += 1
#         else:
#             flor += 1
#     if flor > cill:
#         meet = math.floor(avg)
#     else:
#         meet = math.ceil(avg)
#     for i in range(3):
#         dis += abs(arr[i] - meet)
    
# else:
#     dis= max(arr) - min(arr)


# print(dis,meet)