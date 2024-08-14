# dfs 탐색 알고리즘
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n, r, q = map(int, input().split())
tree = [[] for _ in range(n+1)]
count = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

def countPoint(x):
    count[x] = 1
    for i in tree[x]:
        if not count[i]:
            countPoint(i)
            count[x] += count[i]

countPoint(r)
for i in range(q):
    u = int(input())
    print(count[u])