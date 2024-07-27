import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
s = input().strip()

p = 'IO'*n + 'I'
cnt = 0
for i in range(m):
    if s[i] == 'I':
        if s[i:i+(2*n+1)] == p:
            cnt += 1

print(cnt)