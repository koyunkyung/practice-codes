# 에라토스테네스의 체 알고리즘

def getprime(n):
    isprime = [False, False] + [True]*(n-1)
    primes = []
    for i in range(2,n+1):
        if isprime[i]:
            primes.append(i)
            for j in range(i*2, n+1, i):
                isprime[j] = False
    return primes

import sys
m, n = map(int, sys.stdin.readline().split())
primes = getprime(n)
for p in primes:
    if p >= m:
        print(p)