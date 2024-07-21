import sys
n, m = map(int, sys.stdin.readline().split())
a = set()
for i in range(n):
    a.add(sys.stdin.readline().strip())
b= set()
for i in range(m):
    b.add(sys.stdin.readline().strip())
result = sorted(list(a&b))

print(len(result))
for i in result:
    print(i)