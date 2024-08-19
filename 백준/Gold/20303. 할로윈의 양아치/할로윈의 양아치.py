import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

# union-find
# x노드의 부모 노드가 무엇인지 find
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# a, b 부모 중 더 작은 쪽으로 합쳐주어 합집합 연산
def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m, k = map(int, input().split())
k -= 1
values = [0] + list(map(int, input().split()))

parent = [x for x in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    union(a, b)

groups = [0] * (n+1)
for i in range(1, n+1):
    if i != parent[i]:
        I = find(i)
        values[I] += values[i]
        groups[I] += 1
    else:
        groups[i] += 1

# knapsack
# 친구관계가 서로소집합으로 나누어짐. 각각의 집단에 대해서 인원수가 weight, 각 인원이 갖고 있는 사탕 수의 합이 value
table = [0] * (k+1)

for i in range(1, n+1):
    if groups[i] != 0:
        w = groups[i]
        v = values[i]
        if w > k:
            continue
        for j in range(k, 0, -1):
            if j+w <= k and table[j] != 0:
                table[j+w] = max(table[j+w], table[j]+v)
        table[w] = max(table[w], v)

print(max(table))