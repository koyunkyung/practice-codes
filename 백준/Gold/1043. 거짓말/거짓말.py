import sys
input = sys.stdin.readline

n, m = map(int, input().split())
knowList = set(input().split()[1:])
parties = []
for _ in range(m):
    parties.append(set(input().split()[1:]))

for _ in range(m):
    for party in parties:
        if party & knowList:
            knowList = knowList.union(party)

cnt = 0
for part in parties:
    if part & knowList:
        continue
    cnt += 1

print(cnt)