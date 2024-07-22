import sys
h = int(sys.stdin.readline())

stair = [0] + [int(sys.stdin.readline()) for i in range(1, h+1)]
if h < 2:
    print(stair[h])
else:
    dp = [0]*(h+1)
    dp[1] = stair[1]
    dp[2] = dp[1] + stair[2]
    for k in range(3, h+1):
        dp[k] = max(dp[k-2], dp[k-3]+stair[k-1]) + stair[k]
    print(dp[h])