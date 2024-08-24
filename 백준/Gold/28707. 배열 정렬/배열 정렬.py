# 다익스크라 알고리즘
import sys
input = sys.stdin.readline
from heapq import heappop, heappush

N = int(input())
# 주어지는 배열을 하나의 노드로 이용하기 위해 문자열로 만들어줌
A = ''
for c in input().split():
    A += str(int(c)-1)
M = int(input())
Q = [tuple(map(int, input().split())) for _ in range(M)]

pq = [(0, A)]
dist = dict()
dist[A] = 0

while pq:
    cost, now = heappop(pq)
    if dist[now] < cost:
        continue
    for l, r, c in Q:
        # 조작 결과
        nxt = now[:l-1] + now[r-1] + now[l:r-1] + now[l-1] + now[r:]
        # 조작 결과인 키가 dist에 있는지부터 확인
        if nxt not in dist or dist[nxt] > cost+c:
            dist[nxt] = cost+c
            heappush(pq, (cost+c, nxt))

# 주어진 배열을 정렬한 다음, 결과가 저장되어 있는지 확인
A = ''.join(sorted(A))
if A not in dist:
    print(-1)
else:
    print(dist[A])