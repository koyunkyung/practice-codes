from collections import deque

dr = [-1,0,1,0]     # 상 우 하 좌
dc = [0,1,0,-1]     # 상 우 하 좌

def bfs(visited):
    global ans
    queue = deque([[0, 0]])
    visited[0][0] = True
    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            # 범위를 벗어나거나 벽이거나 이미 방문했다면 continue
            if nc < 0 or nc >= w+2 or nr < 0 or nr >= h+2 or miro[nr][nc] == '*' or visited[nr][nc]:
                continue
            
            # 대문자라면(문이라면), 해당 문을 열 수 있는 키가 없다면 continue
            if 'A' <= miro[nr][nc] <= 'Z':
                if chr(ord(miro[nr][nc]) + 32) not in key:
                    continue
            # 만약 소문자이고 아직 키에 없다면 해당 키를 저장 후 방문체크 초기화
            elif 'a' <= miro[nr][nc] <= 'z':
                if miro[nr][nc] not in key:
                    key[miro[nr][nc]] = True
                    visited = [[False] * (w+2) for _ in range(h+2)]
            # 비밀문서이고 아직 방문하지 않았다면 찾은 개수 1개 층가. 해당 위치는 더이상 방문하면 안되기 때문에 저장
            elif miro[nr][nc] == '$' and (nr, nc) not in visited_doc:
                ans += 1
                visited_doc.append((nr, nc))
            
            # 방문처리, 다음 위치를 큐에 삽입
            visited[nr][nc] = True
            queue.append([nr, nc])

t = int(input())
for _ in range(1, t+1):
    h, w = map(int, input().split())

    miro = ['.' + input() + '.' for _ in range(h)]
    miro = ['.' * (w+2)] + miro + ['.' * (w+2)]
    visited = [[False] * (w+2) for _ in range(h+2)]
    key = {}
    visited_doc = []    # 방문한 키 위치 저장

    for i in input():
        # 만약 알파벳이면 키로 저장
        if i.isalpha():
            key[i] = True
    
    ans = 0
    bfs(visited)
    print(ans)