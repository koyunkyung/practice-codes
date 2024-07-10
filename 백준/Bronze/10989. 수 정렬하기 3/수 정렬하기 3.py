# 계수 정렬 Counting Sort
import sys
input = sys.stdin.readline

n = int(input())
csort = [0]*(10001)

for _ in range(n):
    num = int(input())
    csort[num] += 1

for i in range(1, 10001):
    if csort[i] != 0:
        for k in range(csort[i]):
            print(i)