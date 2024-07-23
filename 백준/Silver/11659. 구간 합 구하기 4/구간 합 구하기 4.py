import sys
input = sys.stdin.readline

m, n = map(int, input().split())
numbers = list(map(int, input().split()))
sum = [0]
tmp = 0
for i in numbers:
    tmp += i
    sum.append(tmp)
for _ in range(n):
    i, j = map(int, input().split())
    print(sum[j] - sum[i-1])