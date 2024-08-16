# dp, 점화식
import sys
input = sys.stdin.readline

n = int(input())
num_arr = [int(x) for x in input().split()]
m = int(input())

dp = [[0]*n for _ in range(n)]
# len == 1
for i in range(n):
    dp[i][i] = 1
# len == 2
for i in range(n-1):
    if num_arr[i] == num_arr[i+1]:
        dp[i][i+1] = 1
# len >= 3
for num_len in range(2, n):
    for start in range(n-num_len):
        end = start + num_len
        if num_arr[start] == num_arr[end]:
            if dp[start+1][end-1] == 1:
                dp[start][end] = 1

for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])