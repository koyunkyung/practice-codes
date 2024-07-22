# DFS
import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
v = int(input())
graph = [[] for i in range(n+1)]
visited = [0]*(n+1)
cnt = -1
for i in range(v):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
def dfs(v):
    visited[v] = 1
    global cnt
    cnt += 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)
dfs(1)
print(cnt)