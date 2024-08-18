# 위상정렬 알고리즘
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for i in range(n+1)]
inDegree = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    inDegree[b] += 1

q = deque()
for s in range(1, n+1):
    if inDegree[s] == 0:
        q.append(s)

ans = []
while q:
    s = q.popleft()
    ans.append(s)
    for adj_s in graph[s]:
        inDegree[adj_s] -= 1
        if inDegree[adj_s] == 0:
            q.append(adj_s)

print(*ans, sep = ' ')