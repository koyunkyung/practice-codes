# 분할 정복
import sys
input = sys.stdin.readline

N, B = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

def multi(a, b):
    X = [[0]*N for _ in range(N)]
    for i in range(N):  # 행렬
        for j in range(N):
            for k in range(N):
                X[i][j] += a[i][k]*b[k][j] % 1000   # 곱셈 연산
    return X

def square(x, n):
    if n == 1:
        return x
    temp = square(x, n//2)
    if n % 2 == 0:
        return multi(temp, temp)
    else:
        return multi(multi(temp,temp),x)
    
result = square(A, B)
for i in range(N):
    for j in range(N):
        result[i][j] %= 1000

for k in result:
    print(*k)