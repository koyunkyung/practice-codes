# 이분탐색
import sys
input = sys.stdin.readline

n = int(input())
a = [*map(int, input().split())]

lis = [a[0]]

def findPlace(e):
    start = 0
    end = len(lis)-1
    while start <= end:
        mid = (start+end) // 2

        if lis[mid] == e:
            return mid
        elif lis[mid] < e:
            start = mid + 1
        else:
            end = mid - 1
    return start

for item in a:
    if lis[-1] < item:
        lis.append(item)
    else:
        idx = findPlace(item)
        lis[idx] = item

print(len(lis))