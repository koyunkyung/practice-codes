import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(2)]

    dp = [[0]*n for _ in range(2)]

    # 스티커 길이가 1일 경우
    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]
    if n == 1:
        print(max(dp[0][0], dp[1][0]))
        continue

    # 스티커 길이가 2일 경우
    dp[0][1] = arr[1][0] + arr[0][1]
    dp[1][1] = arr[0][0] + arr[1][1]
    if n == 2:
        print(max(dp[0][1], dp[1][1]))
        continue

    # 스티커 길이가 3 이상일 경우
    for i in range(2, n):
        dp[0][i] = max(dp[1][i-2], dp[1][i-1]) + arr[0][i]
        dp[1][i] = max(dp[0][i-2], dp[0][i-1]) + arr[1][i]

    print(max(dp[0][-1], dp[1][-1]))