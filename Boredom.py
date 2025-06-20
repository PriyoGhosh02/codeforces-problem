n = int(input())
a = list(map(int, input().split()))

# Step 1: Create a frequency list (up to max value in a)
max_val = max(a)
freq = [0] * (max_val + 2)

for num in a:
    freq[num] += 1

# Step 2: Bottom-up DP
dp = [0] * (max_val + 2)

dp[0] = 0
dp[1] = freq[1] * 1

for i in range(2, max_val + 1):
    dp[i] = max(dp[i-1], dp[i-2] + freq[i] * i)

print(dp[max_val])
