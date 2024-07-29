import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(input()) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
ans = [0,0]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        dx, dy = [1,-1,0,0], [0,0,1,-1]
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n and graph[x][y] == graph[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = 1
                q.append((nx, ny))

# 정상인이 볼 때의 그룹 개수
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            ans[0] += 1
# 적록색맹이 볼 때의 그룹 개수_초록색을 빨간색으로 바꿈
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'
visited = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            ans[1] += 1

print(' '.join(map(str, ans)))