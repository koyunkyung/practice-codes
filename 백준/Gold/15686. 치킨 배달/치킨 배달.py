# 완전탐색 + dfs (조함) : m개를 무작위로 골라서 모든 경우를 찾아야 함
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

chicken = deque([])
house = deque([])
select = deque([])
for a in range(N):
    for b in range(N):
        if arr[a][b] == 1:
            house.append((a,b))
        elif arr[a][b] == 2:
            chicken.append((a,b))

K = len(chicken)
result = N*2*len(house)

def dfs(n, i):  # n: 고른 치킨집 수, i: 고른 치킨집 번호
    global result
    val = 0
    if n == M:
        for h in house:
            hr, hc = h[0], h[1]
            dist = 2*N

            for c in select:
                cr, cc = c[0], c[1]
                tmp = abs(hr-cr) + abs(hc-cc)
                if tmp < dist:
                    dist = tmp
            val += dist
        
        if val < result:
            result = min(val, result)
            return
    # 고른 치킨집 제외하고 dfs
    for idx in range(i, K):
        select.append(chicken[idx])
        dfs(n+1, idx+1)
        select.pop()

for t in range(K):
    dfs(0, t)
print(result)