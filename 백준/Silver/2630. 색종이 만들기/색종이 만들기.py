import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
white = 0
blue = 0
def valid(arr):
    global white
    global blue
    l = len(arr)
    total = l**2

    s = 0
    for row in arr:
        s += sum(r for r in row)
    if s == 0 or s == total:
        if arr[0][0]:
            blue += 1
        else:
            white += 1
    else:
        valid([a[:l//2] for a in arr[:l//2]])
        valid([a[l//2:] for a in arr[:l//2]])
        valid([a[:l//2] for a in arr[l//2:]])
        valid([a[l//2:] for a in arr[l//2:]])
valid(arr)
print(white)
print(blue)