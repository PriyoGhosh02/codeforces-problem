n, k = map(int, input().split())
a = list(map(int, input().split()))

frem_sum = sum(a[:k])
min_sum = frem_sum
min_ind = 0

for i in range(1, n - k + 1):
    frem_sum = frem_sum - a[i - 1] + a[i + k - 1]
    if frem_sum < min_sum:
        min_sum = frem_sum
        min_ind = i

print(min_ind + 1)
