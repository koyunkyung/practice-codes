# DFS 풀이

import sys
sys.setrecursionlimit(10000)

def dfs(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0<=nx<n) and (0<=ny<m):
            if field[nx][ny] == 1:
                field[nx][ny] = -1
                dfs(nx,ny)
for _ in range(int(sys.stdin.readline())):
    m,n,k = map(int, sys.stdin.readline().split())
    field = [[0]*m for _ in range(n)]
    cnt = 0
    for _ in range(k):
        x,y = map(int, sys.stdin.readline().split())
        field[y][x] = 1
    for x in range(n):
        for y in range(m):
            if field[x][y] > 0:
                dfs(x,y)
                cnt += 1
    print(cnt)