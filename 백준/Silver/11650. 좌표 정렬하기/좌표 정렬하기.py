import sys
n = int(sys.stdin.readline())

dots = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    dots.append([x,y])
dots.sort(key = lambda x: x[1])
dots.sort(key = lambda x: x[0])

for i in dots:
    print(i[0], i[1])