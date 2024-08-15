# Kruskal Algorithm
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
edges.sort(key = lambda x: x[2])    # c(cost)가 적은 것부터 정렬

# Union-Find
parent = [i for i in range(v+1)]

def get_parent(x):
    if parent[x] == x:
        return x
    parent[x] = get_parent(parent[x])   # get_parent 거슬러 올라가면서 parent[x] 값도 갱신
    return parent[x]

def union_parent(a, b):
    a = get_parent(a)
    b = get_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def same_parent(a, b):
    return get_parent(a) == get_parent(b)

answer = 0
for a, b, cost in edges:
    if not same_parent(a, b):
        union_parent(a, b)
        answer += cost
print(answer)