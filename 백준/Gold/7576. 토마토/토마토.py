import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
queue = deque()

def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    queue.append((nx,ny))
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1:
            queue.append((i,j))

cannot_complete = False
day = 0
def solve():
    global cannot_complete, day
    bfs()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                cannot_complete = True
            day = max(day, graph[i][j])
solve()
if cannot_complete:
    print(-1)
else:
    print(day-1)