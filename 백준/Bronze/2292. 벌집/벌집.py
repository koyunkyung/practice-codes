n = int(input())
numbox = 1
cnt = 1

while numbox < n:
    numbox += 6 * cnt
    cnt += 1
print(cnt)