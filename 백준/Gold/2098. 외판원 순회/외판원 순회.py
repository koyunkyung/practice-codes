import sys
input = sys.stdin.readline

n = int(input())
cities = [list(map(int, input().split())) for _ in range(n)]
# (1<<n)-1 ==> 'n개의 비트를 모두 켠다'와 같음
visited_all = (1<<n) - 1

# cache[n][visited]: n번 -> visited에서 방문하지 않은 도시 -> 0번 도시(시작 도시) 경로 저장
cache = [[None]*(1<<n) for _ in range(n)]
Inf = float('inf')
idx = 1

def find_path(last, visited):
    # 마지막 방문 도시 출발 - 0번째(출발 도시) 사이에 경로 존재하면 경로 값 반환.
    # 경로 존재하지 않는다면 무한값을 반환해서 답이 안되게 함.
    if visited == visited_all:
        return cities[last][0] or Inf
    
    # cache값이 None이 아니라는 것은 last와 visited의 계산이 이미 수행되었고, 지금은 중복호출이라는 뜻.
    # 다시 계산하지 않고(중복계산 없애 효율성 높임) 값만 바로 반환하도록 함.
    if cache[last][visited] is not None:
        return cache[last][visited]
    
    tmp = Inf
    for city in range(n):
        if visited & (1<<city) == 0 and cities[last][city] != 0:
            tmp = min(tmp, find_path(city, visited|(1<<city))+cities[last][city])
    cache[last][visited] = tmp
    return tmp

print(find_path(0, 1<<0))