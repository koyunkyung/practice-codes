import heapq
import sys
input = sys.stdin.readline

n, m, x = map(int, input().split())
city = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, t = map(int, input().split())
    city[a].append([b,t])

def dijkstra(s):
    D = [float('inf')] * (n+1)
    D[s] = 0
    q = []
    heapq.heappush(q, (0,s))
    while q:
        dist, now = heapq.heappop(q)
        if D[now] >= dist:
            for v, val in city[now]:
                if dist + val < D[v]:
                    D[v] = dist + val
                    heapq.heappush(q, (dist+val, v))
    return D

ans = dijkstra(x)
ans[0] = 0
for i in range(1, n+1):
    if i != x:
        res = dijkstra(i)
        ans[i] += res[x]
    
print(max(ans))