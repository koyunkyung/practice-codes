import sys
n = int(sys.stdin.readline())
stack = []
answer = []
flag = False
cur = 1

for _ in range(n):
    num = int(sys.stdin.readline())
    while cur <= num:
        stack.append(cur)
        answer.append('+')
        cur += 1
    if stack[-1] == num:
        stack.pop()
        answer.append('-')
    else:
        flag = True
        print('NO')
        break
if not flag:
    print('\n'.join(answer))