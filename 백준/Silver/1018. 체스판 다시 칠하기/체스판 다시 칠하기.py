import sys
n, m = map(int, sys.stdin.readline().split())
mtr = []
cnt = []

for _ in range(n):
    mtr.append(sys.stdin.readline())
for a in range(n-7):
    for b in range(m-7):
        idx1 = 0
        idx2 = 0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j)%2 == 0:
                    if mtr[i][j] != "W":
                        idx1 += 1
                    if mtr[i][j] != "B":
                        idx2 += 1
                else:
                    if mtr[i][j] != "B":
                        idx1 += 1
                    if mtr[i][j] != "W":
                        idx2 += 1
        cnt.append(min(idx1,idx2))
print(min(cnt))