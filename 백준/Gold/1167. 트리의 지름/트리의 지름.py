# bfs
import sys
from collections import deque
input = sys.stdin.readline

v = int(input())
tree = [[] for _ in range(v+1)]
for _ in range(v):
    info = list(map(int, input().split()))
    for n in range(1, len(info)-2, 2):
        tree[info[0]].append((info[n], info[n+1]))  # (연결노드, 거리)

def bfs(start):
    visited = [-1] * (v+1)
    visited[start] = 0
    q = deque()
    q.append(start)

    while q:
        cur = q.popleft()
        for next, next_d in tree[cur]:
            if visited[next] == -1:
                q.append(next)
                visited[next] = visited[cur] + next_d
    
    m = max(visited)
    return [visited.index(m), m]

print(bfs(bfs(1)[0])[1])