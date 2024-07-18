import sys
import math

def isprime(x):
    if x == 1:
        return False
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

m, n = map(int, sys.stdin.readline().split())
for k in range(m, n+1):
    if isprime(k):
        print(k)