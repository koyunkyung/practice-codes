n = int(input())
for i in range(1, n+1):
    num = sum(map(int, str(i))) + i
    if num == n:
        print(i)
        break
else:
    print(0)