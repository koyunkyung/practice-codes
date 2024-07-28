import sys, heapq
input = sys.stdin.readline

abs_heap = []
n = int(input())
for i in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(abs_heap, (abs(num), num))
    else:
        try:
            print(heapq.heappop(abs_heap)[1])
        except:
            print(0)