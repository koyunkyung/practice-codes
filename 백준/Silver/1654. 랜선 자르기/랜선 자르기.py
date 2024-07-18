# 이분탐색
import sys
input = sys.stdin.readline
k, n = map(int, input().split())
length = []
for _ in range(k):
    length.append(int(input()))

s = 1
e = max(length)
while s <= e:
    mid = (s+e)//2
    lan = 0
    for i in length:
        lan += i//mid
    if lan >= n:
        s = mid + 1
    else:
        e = mid - 1
print(e)