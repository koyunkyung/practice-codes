n, k = map(int, input().split())

def factorial(x):
    if (x > 1):
        return x * factorial(x-1)
    else:
        return 1

print(factorial(n)//(factorial(k)*factorial(n-k)))