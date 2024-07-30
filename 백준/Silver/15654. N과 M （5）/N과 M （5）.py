import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = [int(x) for x in input().split()]
numbers.sort()
box = []

def backtracking(depth):
    if depth == m:
        print(' '.join(map(str, box)))
        return
    for i in range(n):
        if numbers[i] in box:
            continue
        box.append(numbers[i])
        backtracking(depth+1)
        box.pop()

backtracking(0)