import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split())
max = 10**5
array = [0] * (max+1)

def bfs(v):
    q = deque([v])
    while q:
        v = q.popleft()
        if v == k:
            return array[v]
        for i in (v-1, v+1, 2*v):
            if 0 <= i <= max and not array[i]:
                array[i] = array[v] + 1
                q.append(i)
print(bfs(n))