# DFS
import sys
input = sys.stdin.readline

r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
alphas = set()
ans = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x, y, cnt):
    global ans
    ans = max(ans, cnt)

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]

        if 0 <= nx < r and 0 <= ny < c:
            if board[nx][ny] not in alphas:
                alphas.add(board[nx][ny])
                dfs(nx, ny, cnt+1)
                alphas.remove(board[nx][ny])
alphas.add(board[0][0])
dfs(0,0,1)
print(ans)