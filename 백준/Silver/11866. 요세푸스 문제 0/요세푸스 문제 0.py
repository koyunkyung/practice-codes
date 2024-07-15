import sys
n, k = map(int, sys.stdin.readline().split())

from collections import deque
deq = deque([i for i in range(1,n+1)])
order = []
while len(deq) != 0:
    for _ in range(k-1):
        deq.append(deq.popleft())
    order.append(str(deq.popleft()))
print('<'+', '.join(order)+'>')