from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    
    currentWeight = 0
    while len(truck_weights) > 0:
        time = time + 1
        currentWeight = currentWeight - bridge.popleft()
        if currentWeight + truck_weights[0] <= weight:
            currentWeight = currentWeight + truck_weights[0]
            bridge.append(truck_weights.popleft())
            
        else:
            bridge.append(0)
            
    # 모든 트럭이 다리 건넜으면 마지막 트럭이 다리 건너는 시간 더해주기
    time = time + bridge_length
    return time