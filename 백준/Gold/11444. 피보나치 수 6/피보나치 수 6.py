from collections import defaultdict
n = int(input())
memo = defaultdict(int)
memo[1], memo[2] = 1, 1

def F(num):
    if num <= 2:
        return memo[num]
    elif memo[num] > 0:
        return memo[num]
    else:
        half = num // 2
        if num % 2 == 0:
            h0 = F(half)
            h1 = F(half-1)
            memo[num] = ((2*h1 + h0) * h0) % 1000000007
            return memo[num]
        else:
            h0 = F(half+1)
            h1 = F(half)
            memo[num] = (h0**2 + h1**2) % 1000000007
            return memo[num]

print(F(n))