# 에라토스테네스의 체
import sys
input = sys.stdin.readline

n = int(input())
x = list(map(int, input().split()))

s = set(x)
m = max(x)
sieve = [0 for _ in range(m+1)]
for i in x:
    if i == m:
        continue
    for j in range(2*i, m+1, i):
        if j in s:
            sieve[i] += 1
            sieve[j] -= 1

for i in x:
    print(sieve[i], end=' ')