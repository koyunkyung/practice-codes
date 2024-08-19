import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maps = [list(input()) for _ in range(n)]

visited = [[0 for _ in range(m)] for _ in range(n)]
safe_zone = 0

def dfs(x, y):
    global safe_zone

    # 현재 위치 방문 처리, 사이클에 현재 위치 추가
    visited[y][x] = True
    cycle.append([x, y])

    if maps[y][x] == 'U' and y > 0:
        y -= 1
    elif maps[y][x] == 'D' and y < n-1:
        y += 1
    elif maps[y][x] == 'L' and x > 0:
        x -= 1
    elif maps[y][x] == 'R' and x < m-1:
        x += 1
    
    # 이동한 위치를 이미 방문한 경우
    if visited[y][x]:
        # 사이클에 이 위치가 포함되어 있다면
        if [x, y] in cycle:
            safe_zone += 1
    # 방문 안했으면 다음 위치로
    else:
        dfs(x, y)

for x in range(m):
    for y in range(n):
        if not visited[y][x]:
            cycle = []
            dfs(x, y)

print(safe_zone)