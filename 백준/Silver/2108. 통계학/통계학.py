import sys
input = sys.stdin.readline
n = int(input())
lst = [int(input()) for i in range(n)]

print(round(sum(lst)/n))

lst.sort()
print(lst[n//2])

cnt = dict()
for i in lst:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1
mx = max(cnt.values())
mxlst = []
for i in cnt:
    if cnt[i] == mx:
        mxlst.append(i)
mxlst.sort()
if len(mxlst) == 1:
    print(mxlst[0])
else:
    print(mxlst[1])

print(max(lst)-min(lst))