# dp, 비트마스크
import sys
input = sys.stdin.readline
n = int(input())
num_range = 10  # 0~9
bit_range = 1 << num_range
mod = 10**9
dp = [[[0]*(bit_range) for _ in range(num_range)] for _ in range(n+1)]

# 한자리수부터 시작하려면 한자리수들 다 1로 초기화
for k in range(num_range):
    dp[1][k][1<<k] = 1

for i in range(1, n):
    for j in range(num_range):
        for b in range(bit_range):
            if 0 <= j < 9:
                more = b | 1<<(j+1)
                dp[i+1][j+1][more] += dp[i][j][b]
                dp[i+1][j+1][more] %= mod
            if 0 < j <= 9:
                less = b | 1<<(j-1)
                dp[i+1][j-1][less] += dp[i][j][b]
                dp[i+1][j-1][less] %= mod

total = 0
for k in range(1, num_range):
    total += dp[n][k][0b1111111111]
    total %= mod
print(total)