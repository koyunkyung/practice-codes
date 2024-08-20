# bisect 모듈 활용
import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input())
a = [*map(int, input().split())]

lis = [a[0]]

for item in a:
    if lis[-1] < item:
        lis.append(item)
    else:
        idx = bisect_left(lis, item)
        lis[idx] = item

print(len(lis))