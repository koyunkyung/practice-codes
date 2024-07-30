import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
board = [i for i in range(101)]
visited = [0]*101
for _ in range(n):
    x, y = map(int, input().split())
    board[x] = y
for _ in range(m):
    u, v = map(int, input().split())
    board[u] = v

def bfs(start):
    q = deque([start])
    while q:
        x = q.popleft()
        for nx in range(x+1, x+7):
            if nx > 100:
                continue
            cnt = board[nx]
            if visited[cnt] == 0:
                visited[cnt] = visited[x] + 1
                q.append(cnt)
                if cnt == 100:
                    return visited[100]
    return False

print(bfs(1))