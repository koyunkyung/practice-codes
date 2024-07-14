n = int(input())
nums = []
import sys
for _ in range(n):
    nums.append(int(sys.stdin.readline()))
nums.sort()
for i in nums:
    print(i)