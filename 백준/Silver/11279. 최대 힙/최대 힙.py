import sys
input = sys.stdin.readline
import heapq

numbers = int(input())
heap = []
for _ in range(numbers):
    num = int(sys.stdin.readline()) * (-1)
    if num != 0:
        heapq.heappush(heap,num)
    else:
        try:
            print(heapq.heappop(heap)* (-1))
        except:
            print(0)