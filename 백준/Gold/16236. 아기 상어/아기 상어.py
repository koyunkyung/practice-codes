import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
Inf = 1e9
shark_size = 2
now_x, now_y = 0, 0

# 아기 상어 초기 위치 확인
for i in range(n):
    for j in range(n):
        if graph[i][j] == 9:
            now_x, now_y = i, j
            graph[i][j] = 0

# 현재 위치에서 각 물고기까지의 거리를 반환, 지나는 경로마다 값을 저장
def bfs():
    queue = deque([(now_x, now_y)])
    visited = [[-1] * n for _ in range(n)]
    visited[now_x][now_y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                # 상어가 이동 가능한지 확인
                if shark_size >= graph[nx][ny] and visited[nx][ny] == -1:
                    visited[nx][ny] = visited[x][y] + 1
                    queue.append((nx, ny))
    return visited

# 먹을 물고기 찾기
def solve(visited):
    x, y = 0, 0
    min_distance = Inf
    for i in range(n):
        for j in range(n):
            # bfs에서 지나지 않는 경로는 최단 경로가 아님 + 아기 상어가 먹을 수 있는지 확인
            if visited[i][j] != -1 and 1 <= graph[i][j] < shark_size:
                if visited[i][j] < min_distance:
                    min_distance = visited[i][j]
                    x, y = i, j
    # 모두 탐색해도 그대로 Inf이면 먹을 물고기가 없다는 것
    if min_distance == Inf:
        return False
    else:
        return x, y, min_distance

answer = 0
food = 0
while True:
    result = solve(bfs())
    if not result:
        print(answer)
        break
    else:
        now_x, now_y = result[0], result[1]
        answer += result[2]
        graph[now_x][now_y] = 0
        food += 1

    if food >= shark_size:
        shark_size += 1
        food = 0