# BFS
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
result = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(graph, a, b):
    queue = deque()
    queue.append([a, b])
    graph[a][b] = 0
    cnt = 1
    while queue:
        x, y = queue.popleft()
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph):
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append([nx, ny])
                cnt += 1
    return cnt

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            cnt = bfs(graph, i, j)
            result.append(cnt)
result.sort()
print(len(result))
for k in result:
    print(k)