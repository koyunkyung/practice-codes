# BFS + backtracking
from collections import deque
import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
dx = [0,0,1,-1]
dy = [1,-1,0,0]

# 바이러스가 퍼지는 과정 구현
def bfs():
    queue = deque()
    tmp_graph = copy.deepcopy(graph)
    # 바이러스 큐에 넣기
    for i in range(n):
        for j in range(m):
            if tmp_graph[i][j] == 2:
                queue.append((i,j))
    # 탐색 시작
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0 <= nx < n and 0 <= ny < m and tmp_graph[nx][ny] == 0:  # 감염 가능여부 확인
                tmp_graph[nx][ny] = 2
                queue.append((nx,ny))

    global answer
    cnt = 0
    for i in range(n):
        cnt += tmp_graph[i].count(0)
    answer = max(answer, cnt)

# 벽 세우는 백트래킹 구현
def makeWall(cnt):
    # 벽 3개 세워지면 바이러스 퍼트림
    if cnt == 3:
        bfs()
        return
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:    # 벽 세우기 가능 여부 확인
                graph[i][j] = 1     # 벽 세우기
                makeWall(cnt+1)     # 다시 두번째 벽 세우러 감
                graph[i][j] = 0     # 다시 벽을 허무는 과정 (백트래킹)

for i in range(n):
    graph.append(list(map(int, input().split())))
answer = 0
makeWall(0)
print(answer)