# 위상정렬, dp 알고리즘
import sys
from collections import deque
input = sys.stdin.readline

t = int(input().rstrip())
for _ in range(t):
    n, k = map(int, input().rstrip().split())    # 건물수, 건설순서
    time = [0] + list(map(int, input().rstrip().split()))    # 건물들의 건설시간
    seq = [[] for _ in range(n+1)]  # 건설순서규칙
    inDegree = [0 for _ in range(n+1)]  # 진입차수
    dp = [0 for _ in range(n+1)]    # 해당 건물까지 걸리는 시간

    # 건설순서규칙 저장
    for _ in range(k):
        a, b = map(int, input().rstrip().split())
        seq[a].append(b)
        inDegree[b] += 1

    q = deque()
    # 진입차수 0인 것 찾아서 큐에 넣기
    for i in range(1, n+1):
        if inDegree[i] == 0:
            q.append(i)
            dp[i] = time[i]
    
    while q:
        a = q.popleft()
        for i in seq[a]:
            inDegree[i] -= 1    # 진입차수 줄이고
            dp[i] = max(dp[a]+time[i], dp[i])   # dp을 이용해 건설비용 계산
            if inDegree[i] == 0:
                q.append(i)

    ans = int(input().rstrip())
    print(dp[ans])