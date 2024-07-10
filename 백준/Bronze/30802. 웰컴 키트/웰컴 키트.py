n = int(input())
tsize = list(map(int, input().split()))
t, p = map(int, input().split())

import math
tnum = 0
for i in tsize:
    tnum += math.ceil(i/t)
print(tnum)
print(n//p, n%p)