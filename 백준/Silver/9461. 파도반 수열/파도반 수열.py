import sys
input = sys.stdin.readline

P = [1,1,1,2,2]
for _ in range(95):
    P.append(P[-1] + P[-5])

T = int(input())
for _ in range(T):
    N = int(input())
    print(P[N-1])