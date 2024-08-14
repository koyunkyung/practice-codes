# dfs 알고리즘
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, r, q = map(int, input().split())

m = [[] for _ in range(n+1)]
visit = [-1 for _ in range(n+1)]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    m[a].append(b)
    m[b].append(a)

def dfs(now):
    global visit
    visit[now] = 1
    for i in m[now]:
        if visit[i] == -1:     # 방문하지 않은 방문 가능 노드가 있다면
            visit[now] += dfs(i)    # 방문하며 그 노드의 서브트리 개수를 더해준다
    return visit[now]   # 내 서브트리 개수 리턴

dfs(r)
for _ in range(q):
    get = int(input())
    print(visit[get])