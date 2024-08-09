# BFS
import sys
from collections import deque, defaultdict
input = sys.stdin.readline
n, k = map(int, input().split())

def sol(n, k):
    min, max = 0, 1e5
    will_visit = deque([n])
    visited = [-1]*(int(max+1))
    visited[n] = 0
    answer = 0  # 가능한 가짓수

    while will_visit:
        vx = will_visit.popleft()
        if vx == k:
            answer += 1
        
        for nx in [vx+1, vx-1, 2*vx]:
            if min <= nx <= max and (visited[nx] == visited[vx]+1 or visited[nx] == -1):
                will_visit.append(nx)
                visited[nx] = visited[vx] + 1
    return visited[k], answer

t, m = sol(n, k)
print(t)
print(m)