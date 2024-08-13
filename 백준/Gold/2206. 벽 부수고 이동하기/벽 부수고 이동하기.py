import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
# index 0층: 벽은 안 부수고 가는 경로 / index 1층: 벽을 부수고 가는 경로
visited = [[[0]*2 for _ in range(m)] for _ in range(n)]
visited[0][0][0] = 1
dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y,z):
    queue = deque()
    queue.append((x,y,z))

    while queue:
        a, b, c = queue.popleft()
        if a == n-1 and b == m-1:
            return visited[a][b][c]
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            # 다음 이동할 곳이 벽이고, 벽 파괴 기회를 사용하지 않은 경우
            if graph[nx][ny] == 1 and c == 0:
                visited[nx][ny][1] = visited[a][b][0] + 1
                queue.append((nx,ny,1))
            # 다음 이동할 곳이 벽이 아니고, 아직 한번도 방문하지 않은 곳인 경우
            elif graph[nx][ny] == 0 and visited[nx][ny][c] == 0:
                visited[nx][ny][c] = visited[a][b][c] + 1
                queue.append((nx,ny,c))
    return -1

print(bfs(0,0,0))