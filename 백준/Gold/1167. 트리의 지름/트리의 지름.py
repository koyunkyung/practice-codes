# dfs
import sys
input = sys.stdin.readline

v = int(input())
tree = [[] for _ in range(v+1)]
for _ in range(v):
    info = list(map(int, input().split()))
    for n in range(1, len(info)-2, 2):
        tree[info[0]].append((info[n], info[n+1]))  # (연결노드, 거리)

visited = [-1] * (v+1)
visited[1] = 0

def dfs(start, distance):
    for next, next_d in tree[start]:
        if visited[next] == -1:
            visited[next] = distance + next_d
            dfs(next, distance + next_d)

dfs(1, 0)
last_Node = visited.index(max(visited))
visited = [-1] * (v+1)
visited[last_Node] = 0
dfs(last_Node, 0)

print(max(visited))