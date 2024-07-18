import sys
input = sys.stdin.readline

def myround(n):
    if n - int(n) >= 0.5:
        return int(n) + 1
    else:
        return int(n)

n = int(input())
if n:
    opinion = sorted([int(input()) for _ in range(n)])
    nn = myround(n*0.15)
    score = opinion[nn:(n-nn)]
    print(myround(sum(score)/len(score)))
else:
    print(0)