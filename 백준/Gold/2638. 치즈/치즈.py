from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
cheeze = [list(map(int, input().split())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

# 외부 공기와 접촉하는 부분 탐색
def bfs():
    visited = [[False]* m for _ in range(n)]
    q = deque()
    q.append((0,0))
    visited[0][0] = True

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if cheeze[nx][ny] >= 1:
                    cheeze[nx][ny] += 1
                else:
                    q.append((nx,ny))
                    visited[nx][ny] = True

# 외부 공기와 2변 이상 접촉한 부분 제거
def melt_cheeze():
    melted = 0
    for i in range(n):
        for j in range(m):
            if cheeze[i][j] >= 3:
                cheeze[i][j] = 0
                melted += 1
            elif cheeze[i][j] >= 2:
                cheeze[i][j] = 1
    return melted

time = 0
while True:
    bfs()
    melted = melt_cheeze()
    if melted:
        time += 1
    # 더 이상 녹일 부분이 없다면 시간 반환
    else:
        print(time)
        break