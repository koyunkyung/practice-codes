import sys
K = int(sys.stdin.readline())
ST = []

for _ in range(K):
    num = int(sys.stdin.readline())

    if ST and num == 0:
        ST.pop()
    else:
        ST.append(num)
print(sum(ST))