# dp 알고리즘
# dp[i][l][r] = i번째 움직임을 (l,r)의 발 위치로 수행했을 때 드는 힘의 총합
import sys
sys.setrecursionlimit(10**8)
input = lambda: sys.stdin.readline().rstrip()

max = 400000

# 어떤 발이 k -> lr로 갈 때 드는 비용
def get_add(lr, k):
    if k == 0:
        if lr == 0:
            return 0
        else:
            return 2
    elif k == lr:
        return 1
    elif abs(k-lr) == 1 or abs(k-lr) == 3:
        return 3
    else:
        return 4

move = list(map(int, input().split()))
move.pop()
n = len(move)
if n == 0:
    print(0)
    exit()

dp = [[[max+1 for _ in range(5)] for _ in range(5)] for _ in range(n+1)]
dp[-1][0][0] = 0

for i in range(n):
    # l = move[i], 왼발로 이번 위치 누를 때, 즉 이번에 왼발이 움직일 것
    # 왼발이 움직이니 오른발은 고정. k는 왼발의 이전 위치.
    for r in range(5):
        for k in range(5):
            add = get_add(move[i], k)
            dp[i][move[i]][r] = min(dp[i][move[i]][r], dp[i-1][k][r]+add)
    
    # r = move[i], 오른발로 이번 위치 누를 때, 즉 이번에 오른발이 움직일 것
    # 오른발이 움직이니 왼발은 고정. k는 오른발의 이전 위치.
    for l in range(5):
        for k in range(5):
            add = get_add(move[i], k)
            dp[i][l][move[i]] = min(dp[i][l][move[i]], dp[i-1][l][k]+add)

m = max+1
for l in range(5):
    for r in range(5):
        m = min(m, dp[n-1][l][r])
print(m)