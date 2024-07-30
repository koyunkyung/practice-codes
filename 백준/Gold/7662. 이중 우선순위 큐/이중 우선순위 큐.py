import sys
input = sys.stdin.readline
import heapq

t = int(input())
for _ in range(t):
    min_heap, max_heap = [], []
    visit = [False] * 1000001

    order_num = int(input())
    for key in range(order_num):
        order = input().rsplit()
        if order[0] == 'I':
            heapq.heappush(min_heap, (int(order[1]), key))
            heapq.heappush(max_heap, (int(order[1]) * -1, key))
            visit[key] = True
        elif order[0] == 'D':
            if order[1] == '-1':
                # 삭제 연산시, key값을 기준으로 해당 노드가 하른 힙에서 삭제된 노드인지 먼저 판단
                # 이미 상대 힙에 의해 삭제된 노드인 경우 삭제되지 않은 노드가 나올 때까지 버리다가 삭제 대상 노드가 나오면 삭제
                while min_heap and not visit[min_heap[0][1]]:
                    heapq.heappop(min_heap) # 버림 (상대 힙에서 이미 삭제된 노드임)
                if min_heap:
                    visit[min_heap[0][1]] = False
                    heapq.heappop(min_heap)
            elif order[1] == '1':
                while max_heap and not visit[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visit[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
    while min_heap and not visit[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visit[max_heap[0][1]]:
        heapq.heappop(max_heap)
    
    if min_heap and max_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')