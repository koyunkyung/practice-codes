# BFS
import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
queue = deque()
queue.append(n)
way = [0]*100001
cnt, result = 0, 0
while queue:
    a = queue.popleft()
    temp = way[a]
    if a == k:
        result = temp
        cnt += 1
        continue

    for i in [a-1, a+1, 2*a]:
        # 범위 안에 있고 방문하지 않았거나, 다음 방문이 이전 방문+1이면
        if 0 <= i < 100001 and (way[i] == 0 or way[i] == way[a]+1):
            way[i] = way[a] + 1
            queue.append(i)

print(result)
print(cnt)