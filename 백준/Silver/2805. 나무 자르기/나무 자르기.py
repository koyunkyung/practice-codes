# 이진탐색과 Counter

import sys
from collections import Counter
input = sys.stdin.readline
n, m = map(int, input().split())
trees = Counter(map(int, input().split()))

s = 1
e = 10000000000
while s <= e:
    mid = (s+e) // 2
    tot = sum((h-mid)*i for h, i in trees.items() if h > mid)
    if tot < m:
        e = mid - 1
    else:
        s = mid + 1
print(e)