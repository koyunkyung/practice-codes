# 이진탐색
import sys
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
A.sort()

m = int(sys.stdin.readline())
Cp = list(map(int, sys.stdin.readline().split()))

for i in Cp:
    left = 0
    right = n-1
    isExist = False

    while left <= right:
        mid = (left+right)//2
        if i == A[mid]:
            isExist = True
            print(1)
            break
        elif i > A[mid]:
            left = mid + 1
        else:
            right = mid - 1
    if not isExist:
        print(0)