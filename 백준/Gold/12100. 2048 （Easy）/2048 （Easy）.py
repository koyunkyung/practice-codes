# 백트래킹과 브루트 포스
import sys, copy
input = sys.stdin.readline

n = int(input())
pan = []
ans = 0
for _ in range(n):
    pan.append([int(x) for x in input().rstrip().split()])

def left(board):
    for i in range(n):
        cursor = 0
        for j in range(1, n):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                # 비어있으면 옮긴다
                if board[i][cursor] == 0:
                    board[i][cursor] = tmp
                # 같으면 합친다
                elif board[i][cursor] == tmp:
                    board[i][cursor] *= 2
                    cursor += 1
                # 비어있지도 않고 다른 값일 때 pass, 바로 옆에 붙임
                else:
                    cursor += 1
                    board[i][cursor] = tmp
    return board

def right(board):
    for i in range(n):
        cursor = n - 1
        for j in range(n-1, -1, -1):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[i][cursor] == 0:
                    board[i][cursor] = tmp
                elif board[i][cursor] == tmp:
                    board[i][cursor] *= 2
                    cursor -= 1
                else:
                    cursor -= 1
                    board[i][cursor] = tmp
    return board

def up(board):
    for j in range(n):
        cursor = 0
        for i in range(n):
            if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[cursor][j] == 0:
                    board[cursor][j] = tmp
                elif board[cursor][j] == tmp:
                    board[cursor][j] *= 2
                    cursor += 1
                else:
                    cursor += 1
                    board[cursor][j] = tmp
    return board

def down(board):
    for j in range(n):
        cursor = n - 1
        for i in range(n-1, -1, -1):
             if board[i][j] != 0:
                tmp = board[i][j]
                board[i][j] = 0

                if board[cursor][j] == 0:
                    board[cursor][j] = tmp
                elif board[cursor][j] == tmp:
                    board[cursor][j] *= 2
                    cursor -= 1
                else:
                    cursor -= 1
                    board[cursor][j] = tmp
    return board

def dfs(N, arr):
    global ans
    if N == 5:
        for i in range(n):
            for j in range(n):
                if arr[i][j] > ans:
                    ans = arr[i][j]
        return
    for i in range(4):
        copy_arr = copy.deepcopy(arr)
        if i == 0:
            dfs(N+1, left(copy_arr))
        elif i == 1:
            dfs(N+1, right(copy_arr))
        elif i == 2:
            dfs(N+1, up(copy_arr))
        else:
            dfs(N+1, down(copy_arr))

dfs(0, pan)
print(ans)