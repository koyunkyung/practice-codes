import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
s = list(map(int, input().split()))
num = [0]*10

def tanghuru(start, end, max_num, kind):
    global n
    if end >= n:
        return max_num
    num[s[end]] += 1
    if num[s[end]] == 1:
        kind += 1
    if kind > 2:
        num[s[start]] -= 1
        if num[s[start]] == 0:
            kind -= 1
        start += 1
    max_num = max(max_num, end-start+1)
    return tanghuru(start, end+1, max_num, kind)
print(tanghuru(0,0,0,0))