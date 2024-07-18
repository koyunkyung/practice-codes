import sys
input = sys.stdin.readline
n = int(input())
lst = [int(input()) for i in range(n)]

print(round(sum(lst)/n))

lst.sort()
print(lst[n//2])

from collections import Counter
cnt = Counter(lst)
mode = cnt.most_common()
if len(mode)==1 or mode[0][1] != mode[1][1]:
    print(mode[0][0])
else:
    print(mode[1][0])

print(max(lst)-min(lst))