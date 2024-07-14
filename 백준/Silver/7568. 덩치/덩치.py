import sys
n = int(sys.stdin.readline().strip())
info = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    info.append([x,y])

for person in info:
    rank = 1
    for comp in info:
        if person[0] < comp[0] and person[1] < comp[1]:
            rank += 1
    print(rank, end=' ')