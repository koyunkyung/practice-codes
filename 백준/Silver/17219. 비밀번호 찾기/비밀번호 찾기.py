import sys
n, m = map(int, sys.stdin.readline().strip().split())

program = {}
for _ in range(n):
    site, password = map(str, sys.stdin.readline().strip().split())
    program[site] = password
for _ in range(m):
    site = sys.stdin.readline().strip()
    print(program[site])