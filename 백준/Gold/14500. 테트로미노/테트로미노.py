import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[False]*m for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]
maximum = 0

# ㅗ 모양을 제외한 나머지 모양 탐색
def dfs(x, y, tmp, cnt):
    global maximum
    if cnt == 4:
        maximum = max(maximum, tmp)
        return
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n or visited[ny][nx]:
            continue
        visited[ny][nx] = True
        dfs(nx, ny, tmp+graph[ny][nx], cnt+1)
        visited[ny][nx] = False
# ㅗ 모양 탐색
def fy(x, y):
    global maximum
    tmp = graph[y][x]
    arr = []
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        arr.append(graph[ny][nx])
    length = len(arr)
    if length == 4: # 만약 4방향 모두 n*m에 들어간다면 그 중 가장 작은 값 제거 후 sum
        arr.sort(reverse=True)
        arr.pop()
        maximum = max(maximum, sum(arr)+graph[y][x])
    elif length == 3: # 3방향만 n*m에 들어가기 때문에 바로 sum
        maximum = max(maximum, sum(arr)+graph[y][x])
    return

for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(j, i, graph[i][j], 1)
        fy(j, i)
        visited[i][j] = False

print(maximum)