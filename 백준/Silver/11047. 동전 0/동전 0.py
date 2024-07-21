import sys
n, k = map(int, sys.stdin.readline().split())
coin = []
for i in range(n):
    coin.append(int(sys.stdin.readline()))

cnt = 0
for j in coin[::-1]:
    if k >= j:
        cnt += k // j
        k %= j
        if k <= 0:
            break
print(cnt)