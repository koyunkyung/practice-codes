from collections import deque

def solution(n, edge):
    edge = sorted(edge)
    distance = [0] * (n+1) # 각 노드까지의 거리 저장 리스트
    queue = deque() # BFS
    graph = [[] for _ in range(n+1)]
    answer = 0
    
    # 인접 리스트 그래프
    for i in edge:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])
    
    # 시작 노드 1번
    queue.append(1)
    distance[1] = 1
    
    while queue:
        current = queue.popleft()
        # 현재 내가 관심 있는 노드(1번)과 연결된 노드 모두 찾아서 거리 1씩 더해주기
        for node in graph[current]:
            if distance[node] == 0:
                queue.append(node)
                distance[node] = distance[current] + 1
    
    max_distance = max(distance)
    for j in distance:
        if j == max_distance:
            answer += 1
    return answer