import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

num = []
visited = [False]*n
def dfs():
    if len(num) == m:
        print(*num)
        return
    overlap = 0
    for i in range(n):
        if not visited[i] and overlap != a[i]:
            visited[i] = True
            num.append(a[i])
            overlap = a[i]
            dfs()
            visited[i] = False
            num.pop()
dfs()