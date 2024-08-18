# 누적합, 이분탐색
import bisect
import sys
input = sys.stdin.readline

t = int(input())
n = int(input())
Aarr = list(map(int, input().split()))
m = int(input())
Barr = list(map(int, input().split()))

Asum = []
Bsum = []

for i in range(n):
    for j in range(i+1, n+1):
        Asum.append(sum(Aarr[i:j]))

for i in range(m):
    for j in range(i+1, m+1):
        Bsum.append(sum(Barr[i:j]))

Asum.sort()
Bsum.sort()

answer = 0
for i in range(len(Asum)):
    l = bisect.bisect_left(Bsum, t-Asum[i])
    r = bisect.bisect_right(Bsum, t-Asum[i])
    answer += (r-l)
print(answer)