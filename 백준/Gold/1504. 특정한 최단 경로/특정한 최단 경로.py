import heapq
import sys
input = sys.stdin.readline
Inf = int(1e9)

v, e = map(int, input().split())
graph = [[] for _ in range(v+1)]
for _ in range(e):
    x, y, cost = map(int, input().split())
    graph[x].append((y, cost))
    graph[y].append((x, cost))

def dijkstra(start):
    distance = [Inf] * (v+1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance

v1, v2 = map(int, input().split())
original_dist = dijkstra(1)
v1_dist = dijkstra(v1)
v2_dist = dijkstra(v2)

v1_path = original_dist[v1] + v1_dist[v2] + v2_dist[v]
v2_path = original_dist[v2] + v2_dist[v1] + v1_dist[v]

result = min(v1_path, v2_path)
print(result if result < Inf else -1)