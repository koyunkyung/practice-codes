import sys

n, m = map(int, sys.stdin.readline().split())
poketmon = dict()
number = dict()
for i in range(1, n+1):
    po = sys.stdin.readline().strip()
    poketmon[i] = po
    number[po] = i
for i in range(m):
    find = sys.stdin.readline().strip()
    if find[0].isalpha():
        print(number[find])
    else:
        print(poketmon[int(find)])