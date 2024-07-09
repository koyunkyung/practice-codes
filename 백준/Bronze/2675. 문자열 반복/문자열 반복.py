T = int(input())
for _ in range(T):
    r, s = input().split()
    print("".join([i*int(r) for i in s]))