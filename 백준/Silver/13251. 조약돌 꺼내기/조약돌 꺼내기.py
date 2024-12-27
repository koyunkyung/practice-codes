import sys
import math

M = int(sys.stdin.readline())
stones = list(map(int, sys.stdin.readline().split()))
K = int(sys.stdin.readline())

N = sum(stones)
total = math.comb(N, K)

same_color = 0
for s in stones:
    same_color += math.comb(s, K)

print(same_color/total)